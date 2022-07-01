class Vehicle:
    
    def __init__(self, license_plate, type_vehicle):
        self.__license_plate = license_plate
        self.__type_vehicle = type_vehicle
        
    @property
    def license_plate(self):
        return self.__license_plate
    
    @license_plate.setter
    def license_plate(self, value):
        if not value:
                print("Enter a value for the license plate")
        else:
            self.__license_plate = value
    
    @property
    def type_vehicle(self):
        return self.__type_vehicle
    
    @type_vehicle.setter
    def license_plate(self, value):
        if not value:
                print("Enter a value for the type vehicle")
        else:
            self.__type_vehicle = value