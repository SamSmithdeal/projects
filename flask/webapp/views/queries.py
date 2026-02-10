from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
import models

class event_time_location(ModelView):
    datamodel = SQLAInterface(models.event_time_location)
    route_base = '/event_time_location'
    list_title = 'Event Time and Location'
    list_columns = ['Event','venue','start_date','start_time','end_date','end_time']
    base_permissions = ['can_list']


class performer_total_income(ModelView):
    datamodel = SQLAInterface(models.performer_total_income)
    route_base = '/performer_total_income'
    list_title = 'Performer Total Income'
    list_columns = ['name','total']
    base_permissions = ['can_list']

class cheap_available_tickets(ModelView):
    datamodel = SQLAInterface(models.cheap_available_tickets)
    route_base = '/cheap_available_tickets'
    list_title = 'Cheap Available Tickets'
    list_columns = ['price','ticket_id','event_name','venue_name','band_name']
    base_permissions = ['can_list']

class performer_unsold_tickets(ModelView):
    datamodel = SQLAInterface(models.performer_unsold_tickets)
    route_base = '/performer_unsold_tickets'
    list_title = 'Performer Unsold Tickets'
    list_columns = ['name','event_name','venue_name','unsold_tickets']
    base_permissions = ['can_list']
