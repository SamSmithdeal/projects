import datetime
from flask import flash, redirect
from flask_appbuilder import PublicFormView
from wtforms import IntegerField, SelectField, StringField, SelectMultipleField
from wtforms.validators import Email, InputRequired, Length, Regexp, NumberRange
from flask_appbuilder.forms import DynamicForm
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget, Select2Widget
from wtforms.validators import ValidationError
import psycopg
import socket

try:
    socket.gethostbyname("data.cs.jmu.edu")
    DSN = "host=data.cs.jmu.edu user=team24 dbname=team24"
except:
    DSN = "host=localhost user=team24 dbname=team24"

def new_performer(name, phone_number, email, band_name, performer_type, crewsize):
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                        INSERT INTO app_user(name, phone_number, email, is_admin, venue_owner)
                        VALUES (%s, %s, %s, false, false)""", (name, phone_number, email))
            cur.execute("""
                        INSERT INTO performer (user_id, band_name, type, crewsize)
                        VALUES (lastval(), %s, %s, %s)""",
                        (band_name, performer_type, crewsize))
            cur.execute("SELECT lastval()")
            performer_id = cur.fetchone()[0]
            conn.commit()
            return performer_id

class PerformerRegistrationForm(DynamicForm):
    name = StringField(
        "Name",
        validators=[InputRequired(), Length(max=100)],
        widget=BS3TextFieldWidget(),
    )
    phone_number = StringField(
        "Phone Number",
        validators=[InputRequired(),Regexp(
                r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$",
                message="Please enter a valid phone number.",
            ), ],
        widget=BS3TextFieldWidget(),
    )
    email = StringField(
        "Email",
        validators=[InputRequired(), Email()],
        widget=BS3TextFieldWidget(),
    )
    band_name = StringField(
        "Stage Name",
        validators=[InputRequired(), Length(max=50)],
        widget=BS3TextFieldWidget(),
    )
    performer_type = SelectField(
        "Performer Type",
        validators=[InputRequired()],
        choices=[("", ""), ("musician", "musician"), ("comedian", "comedian")],
        widget=Select2Widget(),
        default=None,
    )
    crew_size = IntegerField(
        "Crew Size",
        validators=[InputRequired(), NumberRange(min=0)],
        widget=BS3TextFieldWidget(),
    )
    
class PerformerRegistrationView(PublicFormView):
    route_base = "/register"
    form = PerformerRegistrationForm
    form_title = "Performer Registration Form"

    def form_post(self, form):
        performer = new_performer(
            form.name.data,
            form.phone_number.data,
            form.email.data,
            form.band_name.data,
            form.performer_type.data,
            form.crew_size.data
        )

        flash("Thank you for registering!", "success")
        return redirect(self.get_redirect())
    
class Select2MultipleWidget(Select2Widget):
    def __call__(self, field, **kwargs):
        kwargs.setdefault("multiple", "multiple")
        return super().__call__(field, **kwargs)

    
def choosePerformer():
    with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT user_id, band_name FROM performer ORDER BY band_name;")
                performers = cur.fetchall()
                choices = [(str(p[0]), p[1]) for p in performers]
                return choices

def choose_venue():
    with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT venue_id, name FROM venue ORDER BY name;")
                venues = cur.fetchall()
                choices = [(str(v[0]), v[1]) for v in venues]
                return choices


def validate_date(form, field):

    # Parse dates
    try:
        start = datetime.datetime.strptime(form.start_date.data, "%Y-%m-%d").date()
        end = datetime.datetime.strptime(form.end_date.data, "%Y-%m-%d").date()
    except ValueError:
        raise ValidationError("Dates must be in YYYY-MM-DD format.")

    if start > end:
        raise ValidationError("Start date cannot be after end date.")
    if (end - start) > datetime.timedelta(days=7):
        raise ValidationError("Event cannot last longer than 7 days.")

    # makes sure a venu is selected
    if not form.venue.data:
        raise ValidationError("Please select a venue first.")

    venue_id = int(form.venue.data)

    # makes sure that venue is available
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT start_date, end_date
                FROM dates_unavailable
                WHERE venue_id = %s
                  AND %s <= end_date
                  AND %s >= start_date;
            """, (venue_id, start, end))

            conflict = cur.fetchone()

    if conflict:
        raise ValidationError("This venue is unavailable for the selected date range.")

    
def new_event(name, description, venue_id, organizer_id, performer_ids, start_date, end_date, start_time, end_time):
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                        INSERT INTO event_info (venue_id, name, description, organizer)
                        VALUES (%s, %s, %s, %s)""",
                        (venue_id, name, description,organizer_id))
            cur.execute("SELECT lastval()")
            event_id = cur.fetchone()[0]

            cur.execute("""
                INSERT INTO event_datetime (event_id, start_date, end_date, start_time, end_time)
                VALUES (%s, %s, %s, %s, %s)
            """, (event_id, start_date, end_date, start_time, end_time))

            cur.execute("""
                INSERT INTO dates_unavailable (venue_id, start_date, end_date)
                        VALUES (%s, %s, %s)""",
                        (venue_id, start_date, end_date))
            
            for pid in performer_ids:
                cur.execute("""
                    INSERT INTO event_performers (event_id, performer_id)
                    VALUES (%s, %s)
                """, (event_id, pid))
            

            conn.commit()
            return event_id
        
def validate_time(form, field):
    try:
        datetime.datetime.strptime(field.data, "%H:%M")
    except ValueError:
        raise ValidationError("Time must be in HH:MM format (00–23 for hours, 00–59 for minutes).")

def validate_person_id(form, field):
    with psycopg.connect(DSN) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT user_id FROM event_organizer
                WHERE user_id = %s;
            """, (form.organizer.data,))

            exist = cur.fetchone()

    if not exist:
        raise ValidationError("There are no organizers with this id")

class EventForm(DynamicForm):
    name = StringField(
        "Event Name",
        default="WoodStock 28",
        validators=[InputRequired(), Length(max=100)],
        widget=BS3TextFieldWidget(),
    )

    description = StringField(
        "Event Description",
        default="Yup we're trying it again",
        validators=[Length(max=500)],
        widget=BS3TextFieldWidget(),
    )

    venue = SelectField(
    "Venue",
    validators=[InputRequired()],
    choices=choose_venue(), 
    widget=Select2Widget()
    )

    performers = SelectMultipleField(
    "Performers",
    validators=[InputRequired()],
    choices=choosePerformer(),
    widget=Select2MultipleWidget()
    )

    start_date = StringField(
    "Start Date (YYYY-MM-DD)",
    default="2028-01-01",
    validators=[InputRequired(), validate_date],
    widget=BS3TextFieldWidget(),
    )

    end_date = StringField(
    "End Date (YYYY-MM-DD)",
    default="2028-01-03",
    validators=[InputRequired(), validate_date],
    widget=BS3TextFieldWidget(),
    )

    start_time = StringField(
    "Start Time (HH:MM)",
    default="12:00",
    validators=[InputRequired(), validate_time],
    widget=BS3TextFieldWidget(),
    )

    end_time = StringField(
    "End Time (HH:MM)",
    default="15:00",
    validators=[InputRequired(), validate_time],
    widget=BS3TextFieldWidget(),
    )

    organizer = IntegerField(
        "Organizer ID (Your ID)",
        default=60,
        validators=[InputRequired(), validate_person_id],
        widget =BS3TextFieldWidget(),
    )

class EventFormView(PublicFormView):
    route_base = "/events"
    form = EventForm
    form_title = "Schedule Event"
    def form_post(self, form):
        # Parse dates
        start = datetime.datetime.strptime(form.start_date.data, "%Y-%m-%d").date()
        end = datetime.datetime.strptime(form.end_date.data, "%Y-%m-%d").date()

        # Insert event
        event_id = new_event(
            form.name.data,
            form.description.data,
            int(form.venue.data),
            int(form.organizer.data),
            form.performers.data,
            start,
            end,
            form.start_time.data,
            form.end_time.data

        )

        flash("Event scheduled successfully!", "success")
        return redirect(self.get_redirect())

 

    def form_get(self, form):
        # Populate venue dropdown
        with psycopg.connect(DSN) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT venue_id, name FROM venue ORDER BY name;")
                venues = cur.fetchall()
                form.venue.choices = [(str(v[0]), v[1]) for v in venues]
