class Employee:
    """Employee class"""

    def __init__(self, name, last_name, id):
        self.__name = name
        self.__last_name = last_name
        self.__ID = id
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value:
            print("Enter a valid value for the name")
        else:
            self.__name = value
    
    @property
    def last_name(self):
        return self.__last_name
    
    @name.setter
    def last_name(self, value):
        if not value:
            print("Enter a valid value for the last name")
        else:
            self.__last_name = value

    @property
    def id(self):
        return self.__ID