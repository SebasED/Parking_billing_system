import datetime
from enum import Enum


class Rate(Enum):
    HALF_HOUR = 30
    HOUR = 60
    MIDDAY = 720
    DAY = 1440
    

class Receipt:

    def __init__(self, num_receipt, parking_nit, parking_name, parking_address, employee_name, employee_id, ingress_date):
        self.__NUM_RECEIPT = num_receipt
        self.__parking_nit = parking_nit
        self.__parking_name = parking_name
        self.__parking_address = parking_address
        self.__employee_name = employee_name
        self.__employee_id = employee_id
        self.__ingress_date = ingress_date
        self.__DEPARTURE_DATE = datetime.datetime.now()
        
    @property
    def num_receipt(self):
        return self.__NUM_RECEIPT  
    
    @property
    def departure_date(self):
        return self.__DEPARTURE_DATE
    
    