import datetime
import math    


class Receipt:
    VALOR = 2500
    
    def __init__(self, num_receipt, parking_nit, parking_name, parking_address, employee_name, employee_last_name, employee_id, ingress_date):
        self.__num_receipt = num_receipt
        self.__parking_nit = parking_nit
        self.__parking_name = parking_name
        self.__parking_address = parking_address
        self.__employee_name = employee_name
        self.__employee_last_name = employee_last_name
        self.__employee_id = employee_id
        self.__ingress_date = ingress_date
        self.__departure_date = datetime.datetime.now()
        
    @property
    def num_receipt(self):
        return self.__num_receipt
    
    @num_receipt.setter
    def num_receipt(self, value):
        if not value:
            print("Enter a valid value for number receipt")
        else:
            self.__num_receipt = value 
    
    @property
    def parking_nit(self):
        return self.__parking_nit
    
    @property
    def parking_name(self):
        return self.__parking_name
    
    @property
    def parking_address(self):
        return self.__parking_address
    
    @property
    def employee_name(self):
        return self.__employee_name
    
    @property
    def employee_last_name(self):
        return self.__employee_last_name
    
    @property
    def employee_id(self):
        return self.__employee_id
    
    @property
    def ingress_date(self):
        return self.__ingress_date
    
    @property
    def departure_date(self):
        return self.__departure_date
    
    def get_total(self):
       ingress_hour = self.ingress_date.hour()
       exit_hour = self.departure_date()
       
       if exit_hour - ingress_hour < 1:
           return self.VALOR 
       else:
           return self.VALOR * math.ceil(exit_hour - ingress_hour)