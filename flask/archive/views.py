# Old file for webapp/views.py, replaced by webapp/views folder

from flask import flash, redirect
import models
from app import appbuilder
from flask_appbuilder import ModelView, BaseView, expose
from flask_appbuilder.actions import action
from flask_appbuilder.models.group import aggregate_count
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.charts.views import GroupByChartView
from markdown import markdown
from pathlib import Path


class Address(ModelView):
    datamodel = SQLAInterface(models.Address)
    route_base = "/address"
    list_title = "Addresses"
    list_columns = [
        "address_id",
        "street_address",
        "address_line2",
        "city",
        "state_province",
        "postal_code",
        "country",
    ]


class AppUser(ModelView):
    datamodel = SQLAInterface(models.AppUser)
    route_base = "/app_user"
    list_title = "App Users"
    list_columns = [
        "user_id",
        "name",
        "phone_number",
        "email",
        "is_admin",
        "venue_owner",
    ]


class EventInfo(ModelView):
    datamodel = SQLAInterface(models.EventInfo)
    route_base = "/event_info"
    list_title = "Event Info"
    list_columns = [
        "event_id",
        "venue_id",
        "name",
        "description",
        "organizer",
        "venue",
        "performer",
        "event_datetime",
        # "ticket",
    ]

class DatesUnavailable(ModelView):
    datamodel = SQLAInterface(models.DatesUnavailable)
    route_base = "/dates_unavailable"
    list_title = "Dates Unavailable"
    list_columns = [
        "availability_id",
        "venue_id",
        "start_date",
        "end_date",
        "venue",
    ]


class EventDatetime(ModelView):
    datamodel = SQLAInterface(models.EventDatetime)
    route_base = "/event_datetime"
    list_title = "Event Dates and Times"
    list_columns = [
        "dt_id",
        "event_id",
        "start_date",
        "end_date",
        "start_time",
        "end_time",
        "event",
    ]


class EventOrganizer(ModelView):
    datamodel = SQLAInterface(models.EventOrganizer)
    route_base = "/event_organizers"
    list_title = "Event Organizers"
    list_columns = [
        "user_id",
        "speciality",
    ]
    add_exclude_columns = edit_exclude_columns = ["event_info"]
    related_views = [EventInfo]


class Performer(ModelView):
    datamodel = SQLAInterface(models.Performer)
    route_base = "/performer"
    list_title = "Performers"
    list_columns = [
        "user_id",
        "band_name",
        "type",
        "crewsize",
    ]
    add_exclude_columns = edit_exclude_columns = ["event"]
    related_views = [EventInfo]


class Venue(ModelView):
    datamodel = SQLAInterface(models.Venue)
    route_base = "/venue"
    list_title = "Venues"
    list_columns = [
        "venue_id",
        "address_id",
        "name",
        "capacity",
        "owner_id",
        "address",
        "owners",
    ]
    add_exclude_columns = edit_exclude_columns = ["dates_unavailable", "event_info"]
    related_views = [DatesUnavailable, EventInfo]

    @action("myaction", "Contact Venue via email", "Are you sure?", "fa-email")
    def send_email(self, items):
        # items may be a single Venue object or a list of Venue objects
        if not isinstance(items, list):
            items = [items]
        flash(f"{len(items)} emails sent!", "success")
        return redirect(self.get_redirect())


class Ticket(ModelView):
    datamodel = SQLAInterface(models.Ticket)
    route_base = "/ticket"
    list_title = "Tickets"
    list_columns = ["event_id", "ticket_id", "price", "ticket_sold", "event"]


appbuilder.add_view(
    Address,
    "Addresses",
    icon="fa-database",
    category="Admin",
)

appbuilder.add_view(
    AppUser,
    "App Users",
    icon="fa-database",
    category="Admin",
)

appbuilder.add_view(
    DatesUnavailable,
    "Dates Unavailable",
    icon="fa-database",
    category="Admin",
)

appbuilder.add_view(
    EventDatetime,
    "Event Dates and Times",
    icon="fa-database",
    category="Admin",
)

appbuilder.add_view(
    EventInfo,
    "Event Info",
    icon="fa-database",
    category="Admin",
)

appbuilder.add_view(
    EventOrganizer,
    "Event Organizers",
    icon="fa-database",
    category="Admin",
)

# appbuilder.add_view(
#     Event_performers,
#     "Event_performerss",
#     icon="fa-database",
#     category="Admin",
# )

appbuilder.add_view(
    Performer,
    "Performers",
    icon="fa-database",
    category="Admin",
)

appbuilder.add_view(
    Ticket,
    "Tickets",
    icon="fa-database",
    category="Admin",
)

appbuilder.add_view(
    Venue,
    "Venues",
    icon="fa-database",
    category="Admin",
)


def md_to_html(filename: str) -> str:
    """Render a markdown file as html."""
    path = Path("templates") / filename
    text = path.read_text(encoding="utf-8")
    return markdown(text, extensions=["attr_list"])


class AboutView(BaseView):
    route_base = "/about"

    @expose("/")
    def about(self):
        return self.render_template("about.jinja", content=md_to_html("about.md"))


class Tickets_Sold(GroupByChartView):
    datamodel = SQLAInterface(models.Ticket)
    chart_title = "Number of Tickets Sold"
    definitions = [
        {"group": "event_id", "series": [(aggregate_count, "ticket_sold")]},
        # can add other groupings
    ]


appbuilder.add_view(
    Tickets_Sold,
    "Tickets Sold by Event",
    icon="fa-chart-simple",
    category="Charts",
)


appbuilder.add_view_no_menu(AboutView())
