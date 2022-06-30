import json


def get_ticket(license_plate):
    with open(".\src\data\\ticket.json") as file:
        tickets = json.load(file)
        ticket = [element for element in tickets if element["license_plate"] == license_plate]
        if ticket:
            return json.dumps(ticket[0], indent=4)
        else:
            return "The license plate does not exist"
    
def get_tickets():
    with open(".\src\data\\ticket.json") as file:
        tickets = json.load(file)
        return json.dumps(tickets, indent=4)

def create_ticket(num_ticket, license_plate, type_vehicle, ingress_date):
    tickets = []
    with open(".\src\data\\ticket.json") as file:
        try:
            tickets = json.load(file)
        except json.JSONDecodeError:
            pass  
    
    data = {
        "num_ticket": num_ticket,
        "license_plate": license_plate,
        "type": type_vehicle,
        "ingress_date": str(ingress_date)
    }
    
    tickets.append(data)
    with open(".\src\data\\ticket.json", "w") as file:
        json.dump(tickets, file, indent=4)

    print(json.dumps(data, indent=4))

def delete_ticket(license_plate):
    tickets = []
    with open(".\src\data\\ticket.json") as file:
        tickets = json.load(file)
    
    with open(".\src\data\\ticket.json","w") as file:    
        ticket = [element for element in tickets if element["license_plate"] == license_plate]
        if ticket:
            del tickets[ticket[0]["num_ticket"]]
            json.dump(tickets, file, indent=4)
            print("The ticket eliminated was: ")
            print(json.dumps(ticket[0], indent=4))
        else:
            return "The license plate does not exist" 
    
    
def get_num_ticket():
    with open(".\src\data\\ticket.json") as file:
        try:
            tickets = json.load(file)
            return len(tickets) 
        except json.JSONDecodeError:
            return 0
        