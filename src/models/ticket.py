from models.vehicle import Vehicle
import datetime

class Ticket:

    def __init__(self, num_ticket, license_plate, type_vehicle):
        self.__num_ticket = num_ticket
        self.__ingress_date = datetime.datetime.now()
        self.__vehicle = Vehicle(license_plate, type_vehicle)
    
    @property
    def num_ticket(self):
        return self.__num_ticket
    
    @num_ticket.setter
    def num_ticket(self, value):
        if not value:
            print("Enter a valid value for the ticket number")
        else:
            self.__num_ticket = value 
            
    @property
    def ingress_date(self):
        return self.__ingress_date
    
    @property
    def vehicle(self):
        return self.__vehicle
