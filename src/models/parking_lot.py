from employee import Employee
from ticket import Ticket
class ParkingLot:
    
    def __init__(self, nit, name, address, employee_name, employee_last_name, employee_id):
        self.__NIT = nit
        self.__name = name
        self.__address = address
        self.__employees = [Employee(employee_name, employee_last_name, employee_id)]
        self.__tickets = []
        self.__receipts = []
    
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
        ticket = Ticket(self.__tickets.len(), license_plate, type_vehicle)
        self.__tickecs.append(ticket) 
        