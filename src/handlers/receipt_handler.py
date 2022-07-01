import json


def get_receipt(license_plate):
    with open(".\src\data\\receipt.json") as file:
        receipts = json.load(file)
        receipt = [element for element in receipts if element["license_plate"] == license_plate]
        if receipt:
            return receipt
        else:
            return "There is not receipt for that license plate"

def get_receipts():
    with open(".\src\data\\receipt.json") as file:
        receipts = json.load(file)
        return receipts

def create_receipt(num_receipt, parking_lot, employee, license_plate, check_in_time, departure_time, total):
    receipts = []
    with open(".\src\data\\receipt.json") as file:
        try:
            receipts = json.load(file)
        except json.JSONDecodeError:
            pass 
    
    data = {
        "num_receipt": num_receipt,
        "Parking_lot": parking_lot,
        "employee": employee,
        "license_plate": license_plate,
        "check_in_time": str(check_in_time),
        "departure_time": str(departure_time),
        "total": total
    }
    
    receipts.append(data)
    
    with open(".\src\data\\receipt.json", "w") as file:
        json.dump(receipts, file, indent=4)
    
    print(json.dumps(data, indent=4))

def delete_receipt(license_plate):
    receipts = []
    with open(".\src\data\\receipt.json", "r") as file:
        receipts = json.load(file)
    
    with open(".\src\data\\receipt.json", "w") as file:    
        receipt = [element for element in receipts if element["license_plate"] == license_plate]
        if receipt:
            for index, item in enumerate(receipts):
                if item["license_plate"] == license_plate:
                    del receipts[index]
                    json.dump(receipts, file, indent=4)
                    print("The receipt eliminated was: ")
                    print(json.dumps(item, indent=4)) 
        else:
            return "There is not receipt for that license plate"
    
    