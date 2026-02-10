"""Flask-AppBuilder views that provide CRUD web interfaces for the models."""

# See https://fontawesome.com/icons for icon names.

from views import base, charts, forms, queries, tables


def setup_menu(appbuilder):
    # --------------------------------------------------------------------------
    # Tables Menu (in an order that makes sense for the GUI)
    # --------------------------------------------------------------------------
    appbuilder.add_view(
        tables.Address,
        "Addresses",
        icon="fa-database",
        category="Tables",
        category_icon="fa-database",
    )

    appbuilder.add_view(
        tables.AppUser,
        "App Users",
        icon="fa-database",
        category="Tables",
    )

    appbuilder.add_view(
        tables.DatesUnavailable,
        "Dates Unavailable",
        icon="fa-database",
        category="Tables",
    )

    appbuilder.add_view(
        tables.EventDatetime,
        "Event Dates and Times",
        icon="fa-database",
        category="Tables",
    )

    appbuilder.add_view(
        tables.EventInfo,
        "Event Info",
        icon="fa-database",
        category="Tables",
    )

    appbuilder.add_view(
        tables.EventOrganizer,
        "Event Organizers",
        icon="fa-database",
        category="Tables",
    )

    # appbuilder.add_view(
    #     Event_performers,
    #     "Event_performerss",
    #     icon="fa-database",
    #     category="Admin",
    # )

    appbuilder.add_view(
        tables.Performer,
        "Performers",
        icon="fa-database",
        category="Tables",
    )

    appbuilder.add_view(
        tables.Ticket,
        "Tickets",
        icon="fa-database",
        category="Tables",
    )

    appbuilder.add_view(
        tables.Venue,
        "Venues",
        icon="fa-database",
        category="Tables",
    )

    # --------------------------------------------------------------------------
    # Views Menu (in an order that makes sense for the GUI)
    # --------------------------------------------------------------------------
    appbuilder.add_view(
        queries.event_time_location,
        "Event Time and Location",
        icon="fa-database",
        category="Views",
        category_icon="fa-database",
    )
    appbuilder.add_view(
        queries.performer_total_income,
        "Performer Total Income",
        icon="fa-database",
        category="Views",
        category_icon="fa-database",
    )
    appbuilder.add_view(
        queries.cheap_available_tickets,
        "Cheap Available Tickets",
        icon="fa-database",
        category="Views",
        category_icon="fa-database",
    )
    appbuilder.add_view(
        queries.performer_unsold_tickets,
        "Performer Unsold Tickets",
        icon="fa-database",
        category="Views",
        category_icon="fa-database",
    )

    # --------------------------------------------------------------------------
    # Chart Menu (in an order that makes sense for the GUI)
    # --------------------------------------------------------------------------
    appbuilder.add_view(
        charts.Tickets_Sold,
        "Tickets Sold by Event",
        category_icon="fa-chart-simple",
        icon="fa-chart-simple",
        category="Charts",
    )

    appbuilder.add_view(
        charts.CalendarView,
        "Venue Events",
        icon="fa-calendar",
        category="Charts",
    )

    # --------------------------------------------------------------------------
    # Custom Views (some might not be in the menu)
    # --------------------------------------------------------------------------
    appbuilder.add_view_no_menu(base.AboutView())

    # --------------------------------------------------------------------------
    # Form Views
    # --------------------------------------------------------------------------
    appbuilder.add_view(
        forms.PerformerRegistrationView,
        "Performer Registration",
        category_icon="fa-file-text",
        icon="fa-id-card",
        category="Forms",
    )

    appbuilder.add_view(
        forms.EventFormView, "Event Form", icon="fa-id-card", category="Forms"
    )
