from handlers import ticket_handler
from handlers import receipt_handler
from models.parking_lot import ParkingLot

def menu(parking_lot):
    option = ""
    values = ["1","2","3","4","5"]
    while True:
        print("""
            Welcome to Shield Code Parking
            select a option:
            1 - Ingress vehicle
            2 - Exit vehicle
            3 - Manage tickets
            4 - Manage receipts
            5 - Exit
            """)

        option = input()
        if option not in values:
            print(" select a correct option between 1 and 5")
        elif option == "1":
            license_plate = input("Enter the license plate: ")
            type_vehicle = input("Enter the type vehicle: ")
            parking_lot.vehicle_entry(license_plate, type_vehicle)
        elif option == "2":
            license_plate = input("Enter the license plate: ")
            parking_lot.vehicle_exit(license_plate)
        elif option == "3":
            menu_ticket()
        elif option == "4":
            menu_receipt()
        elif option == "5":
            print("Exiting...")
            exit()   
                

def menu_receipt():
    option = ""
    values = ["1","2","3","4"]
    while True:
        print("""
            Shield Code Parking
            select a option:
            1 - show a receipt
            2 - show all receipts
            3 - delete a receipt
            4 - Exit
            """)

        option = input()
        if option not in values:
            print(" select a correct option between 1 and 4")
        elif option == "1":
            license_plate = input("Enter the license plate: ")
            receipt = receipt_handler.get_receipt(license_plate)
            print(receipt)
        elif option == "2":
            receipts = receipt_handler.get_receipts()
            print(receipts)
        elif option == "3":
            license_plate = input("Enter the license plate: ")
            receipt_handler.delete_receipt(license_plate)
            print(f"The receipt of the car with license plate {license_plate} was deleted")
        elif option == "4":
            break        
            
        
def menu_ticket():
    option = ""
    values = ["1","2","3","4"]
    while True:
        print("""
            Welcome to Shield Code Parking
            select a option:
            1 - Show a ticket
            2 - Show all tickets
            3 - delete a ticket
            4 - Exit
            """)

        option = input()
        if option not in values:
            print(" select a correct option between 1 and 4")
        elif option == "1":
            license_plate = input("Enter the license plate: ")
            receipt = ticket_handler.get_ticket(license_plate)
            print(receipt)
        elif option == "2":
            receipts = ticket_handler.get_tickets()
            print(receipts)
        elif option == "3":
            license_plate = input("Enter the license plate: ")
            ticket_handler.delete_ticket(license_plate)
            print(f"The ticket of the car with license plate {license_plate} was deleted")
        elif option == "4":
            break 

def main():
    parking = ParkingLot(11145454545, "Shield Code", "Medellin", "Sebas", "Estrada", 10203)
    menu(parking)

if __name__=="__main__":
    main() 