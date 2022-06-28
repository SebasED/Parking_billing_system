class Employee:
    """Employee class"""

    def __init__(self, name, last_name, id) -> None:
        self.__name = name
        self.__last_name = last_name
        self.__id = id
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value == "" or type(value) != str:
            print("Enter a valid value for the name")
        self.__name = value
    
    @property
    def last_name(self):
        return self.__last_name
    
    @name.setter
    def last_name(self, value):
        if value == "" or type(value) != str:
            print("Enter a valid value for the last name")
        self.__last_name = value

    @property
    def id(self):
        return self.__id
    
    @name.setter
    def id(self, value):
        if value == "" or type(value) != int:
            print("Enter a valid value for the id")
        self.__last_name = value