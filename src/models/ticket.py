from vehicle import Vehicle
import datetime

class Ticket:

    def __init__(self, num_ticket, license_plate, type_vehicle):
        self.__NUM_TICKET = num_ticket
        self.__INGRESS_DATE = datetime.datetime.now()
        self.__vehicle = Vehicle(license_plate, type_vehicle)
    
    @property
    def num_ticket(self):
        return self.__NUM_TICKET
    
    @property
    def ingress_date(self):
        return self.__INGRESS_DATE
    
    @property
    def vehicle(self):
        return self.__vehicle