import models
from datetime import timedelta
from collections import defaultdict
from flask_appbuilder import BaseView, expose
from flask_appbuilder.models.group import aggregate_count
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.charts.views import GroupByChartView
from config import SQLALCHEMY_DATABASE_URI
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from models import * 


class Tickets_Sold(GroupByChartView):
    datamodel = SQLAInterface(models.Ticket)
    chart_title = "Number of Tickets Sold"
    definitions = [
        {"group": "event_id", "series": [(aggregate_count, "ticket_sold")]},
        # can add other groupings
    ]

class CalendarView(BaseView):
    route_base = "/"

    @expose("/calendar")
    def list(self):
        engine = create_engine(SQLALCHEMY_DATABASE_URI)
        with Session(engine) as session:
            stmt = select(Venue.name, DatesUnavailable.start_date, DatesUnavailable.end_date).join(Venue).order_by(DatesUnavailable.venue_id, DatesUnavailable.end_date)
            dates = session.execute(stmt)
            
        # build unavailability dictionary
        availability = defaultdict(list)
        delta = timedelta(days=1)
        for item in dates:
            curr = item[1]
            while (curr <= item[2]):
                availability[item[0]].append(curr.strftime("%Y-%m-%d"))
                curr += delta
        return self.render_template("calendar.jinja", availability=availability, keys=availability.keys())