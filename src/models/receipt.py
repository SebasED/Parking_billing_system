import datetime
import math    


class Receipt:
    VALOR = 2500
    
    def __init__(self, num_receipt, parking_nit, parking_name, parking_address, employee_name, employee_id, ingress_date):
        self.__NUM_RECEIPT = num_receipt
        self.__PARKING_NIT = parking_nit
        self.__parking_name = parking_name
        self.__parking_address = parking_address
        self.__employee_name = employee_name
        self.__EMPLOYEE_ID = employee_id
        self.__ingress_date = ingress_date
        self.__DEPARTURE_DATE = datetime.datetime.now()
        
    @property
    def num_receipt(self):
        return self.__NUM_RECEIPT  
    
    @property
    def departure_date(self):
        return self.__DEPARTURE_DATE
    
    def get_total(self, ingress, exit):
       ingress_hour = ingress.hour()
       exit_hour = exit.hour()
       
       if exit_hour - ingress_hour < 1:
           return self.VALOR 
       else:
           return self.VALOR * math.ceil(exit_hour - ingress_hour)