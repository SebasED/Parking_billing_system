from posixpath import split
from models.employee import Employee
from models.ticket import Ticket
from models.receipt import Receipt
from handlers import ticket_handler
from handlers import receipt_handler
from datetime import datetime


class ParkingLot:
    
    def __init__(self, nit, name, address, employee_name, employee_last_name, employee_id):
        self.__nit = nit
        self.__name = name
        self.__address = address
        self.__employee = Employee(employee_name, employee_last_name, employee_id)
    
    @property
    def nit(self):
        return self.__nit
    
    @nit.setter
    def nit(self, value):
        if not value:
            print("Enter a valid value for parking's nit")
        else:
            self.__nit = value
            
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
    def employee(self):
        return self.__employee
    
    @employee.setter
    def employee(self, value):
        if not value:
            print("Enter a valid employee")
        else:
            self.__employee = value
    
    def vehicle_entry(self, license_plate, type_vehicle):
        num_ticket = ticket_handler.get_num_ticket()
        ticket = Ticket(num_ticket, license_plate, type_vehicle)
        ticket_handler.create_ticket(ticket.num_ticket, 
                                     license_plate, 
                                     ticket.vehicle.type_vehicle, 
                                     ticket.ingress_date)
        
    def vehicle_exit(self, license_plate):
        ticket = ticket_handler.get_ticket(license_plate)
        index = ticket["ingress_date"].find(".")
        date = ticket["ingress_date"].replace("-","/")[0:index]
        ingress_date = datetime.strptime(date,'%Y/%m/%d %H:%M:%S')
        receipt = Receipt(ticket["num_ticket"], 
                          self.nit, 
                          self.name, 
                          self.address, 
                          self.employee.name, 
                          self.employee.last_name, 
                          self.employee.id, 
                          ingress_date)
        total = receipt.get_total()
        parking = {
            "NIT": receipt.parking_nit,
            "name": receipt.parking_name,
            "address": receipt.parking_address
        }
        employee = {
            "id": receipt.employee_id,
            "name": receipt.employee_name,
            "last_name":receipt.employee_last_name
        }
        
        receipt_handler.create_receipt(receipt.num_receipt, 
                                        parking, employee, 
                                        license_plate, 
                                        receipt.ingress_date, 
                                        receipt.departure_date, 
                                        total)
        
        ticket_handler.delete_ticket(license_plate)
        