class Flight:

    counter = 1

    def __init__(self, origin, destination, duration):
        
        self.id = Flight.counter
        Flight.counter += 1
        self.passengers = []

        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f"Origin: {self.origin}")
        print(f"Destination: {self.destination}")
        print(f"Duration: {self.duration}")
        print("Passengers:")
        for passenger in self.passengers:
            print(f"{passenger.name}")

    def add_passenger(self, pa):
        pa.flight_id = self.id
        self.passengers.append(pa)

class Passenger:
 
 
    def __init__(self, name):
        self.name = name

def main():
    f1 = Flight(origin = "Ha Noi", destination = "Lao Cai", duration = 120)
    p1 = Passenger("Dang Thi Thuy")
    p2 = Passenger("Dang Van Duc")
    f1.add_passenger(p1)
    f1.add_passenger(p2)
    f1.print_info()

    
if __name__=="__main__":
    main()