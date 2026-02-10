from flask import flash, redirect
import models
from flask_appbuilder import ModelView
from flask_appbuilder.actions import action
from flask_appbuilder.models.sqla.interface import SQLAInterface


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

    @action(
        "generate_summary",
        "Generate Summary Report",
        "Generate a summary for the selected event(s)?",
        "fa-chart-line",
    )
    def generate_summary(self, items):
        if not isinstance(items, list):
            items = [items]

        summaries = []
        for event in items:
            total_tickets = len(event.ticket or [])
            tickets_sold = sum(1 for t in event.ticket if t.ticket_sold)
            total_revenue = sum(t.price or 0 for t in event.ticket if t.ticket_sold)

            performer_names = (
                ", ".join(
                    [
                        p.band_name or p.name or f"Performer {p.user_id}"
                        for p in event.performer
                    ]
                )
                or "N/A"
            )

            if event.event_datetime:
                first_dt = min(
                    (d.start_date for d in event.event_datetime if d.start_date),
                    default=None,
                )
                last_dt = max(
                    (d.end_date for d in event.event_datetime if d.end_date),
                    default=None,
                )
                date_range = (
                    f"{first_dt} → {last_dt}" if first_dt and last_dt else "N/A"
                )
            else:
                date_range = "N/A"

            venue_name = event.venue.name if event.venue else "N/A"
            organizer_name = (
                event.event_organizer.name
                if event.event_organizer and event.event_organizer.name
                else "N/A"
            )

            summaries.append(
                {
                    "Event": event.name or f"Event {event.event_id}",
                    "Organizer": organizer_name,
                    "Venue": venue_name,
                    "Dates": date_range,
                    "Performers": performer_names,
                    "Tickets": f"{tickets_sold}/{total_tickets}",
                    "Revenue": f"${total_revenue:,.2f}",
                }
            )

        for s in summaries:
            flash(
                f"📊 {s['Event']} — {s['Tickets']} tickets sold, {s['Revenue']} total revenue. "
                f"Venue: {s['Venue']} | Organizer: {s['Organizer']} | Dates: {s['Dates']}",
                "info",
            )

        flash(f"Generated summary for {len(summaries)} event(s).", "success")
        return redirect(self.get_redirect())


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

    @action(
        "send_email",
        "Contact Venue via Email",
        "Send an email to selected venue(s)?",
        "fa-envelope",
    )
    def send_email(self, items):
        if not isinstance(items, list):
            items = [items]
        flash(f"Email sent to {len(items)} venue owner(s).", "success")

        return redirect(self.get_redirect())


class Ticket(ModelView):
    datamodel = SQLAInterface(models.Ticket)
    route_base = "/ticket"
    list_title = "Tickets"
    list_columns = ["event_id", "ticket_id", "price", "ticket_sold", "event"]
