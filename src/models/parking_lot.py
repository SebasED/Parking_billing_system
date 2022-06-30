from employee import Employee
from ticket import Ticket
from handlers import ticket_handler
from handlers import receipt_handler
import datetime

class ParkingLot:
    
    def __init__(self, nit, name, address, employee_name, employee_last_name, employee_id):
        self.__NIT = nit
        self.__name = name
        self.__address = address
        self.__employee = Employee(employee_name, employee_last_name, employee_id)
    
    @property
    def nit(self):
        return self.__NIT
            
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value:
            print("Enter a valid value for parking's name")
        else:
            self.__name = value
    
    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, value):
        if not value:
            print("Enter a valid value for parking's address")
        else:
            self.__address = value
    
    @property
    def employees(self):
        return self.__employees
    
    @employees.setter
    def employees(self, value):
        if not value:
            print("Enter a valid employee")
        else:
            self.__employees.append(value)
    
    @property
    def tickecs(self):
        return self.__tickets
    
    @property
    def Reciepts(self):
        return self.__receipts
    
    def vehicle_entry(self, license_plate, type_vehicle):
        num_ticket = ticket_handler.get_num_ticket()
        ticket = Ticket(num_ticket, license_plate, type_vehicle)
        ticket_handler.create_ticket(ticket.num_ticket, ticket.license_plate, ticket.type_vehicle, ticket.ingress_date)
        ticket_handler.show_ticket()
        
        
    def vehicle_exit(self, license_plate):
        ticket = ticket_handler.get_ticket(license_plate)
        parking = {
            "NIT":self.__NIT,
            "name": self.__name,
            "address": self.__address
        }
        employee = {
            "id": self.__employee.id,
            "name":self.__employee.name,
            "last_name":self.__employee.last_name
        }
        departure_date =  datetime.datetime.now()
        