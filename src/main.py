from models.parking_lot import ParkingLot


def main():
    parking = ParkingLot(111, "Shield Code", "Medellin", "Sebas", "Estrada", 10203)
    print(type(parking))
    parking.vehicle_entry("RQX95B", "Motorcycle")

if __name__=="__main__":
    main() 