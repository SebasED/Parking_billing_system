import json


def get_ticket(license_plate):
    with open(".\src\data\ ticket.json") as file:
        tickets = json.dump(file)
        ticket = [element for element in tickets if element.license_plate == license_plate]
        if ticket:
            return ticket
        else:
            return "The license plate does not exist"
    
def get_tickets():
    with open(".\src\data\ ticket.json") as file:
        tickets = json.dump(file)
        return tickets

def create_ticket(license_plate, type_vehicle):
    num_ticket = 0
    tickets = []
    with open(".\src\data\ ticket.json") as file:
        tickets = json.dump(file)
        num_ticket = len(tickets)
    
    data = {
        "num_ticket": num_ticket,
        "license_plate": license_plate,
        "type": type_vehicle
    }
    
    tickets.append(data)
    
    with open(".\src\data\ ticket.json", "w") as file:
        json.dump(tickets, file, indent=4)


def delete_ticket(license_plate):
    with open(".\src\data\ ticket.json") as file:
        tickets = json.dump(file)
        
        ticket = [element for element in tickets if element.license_plate == license_plate]
        if ticket:
            del tickets[ticket.num_ticket]
        else:
            return "The license plate does not exist" 

def show_ticket(license_plate):
    ticket = get_ticket(license_plate)
    print(ticket)