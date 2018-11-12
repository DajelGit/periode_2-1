class Vehicle:
    def __init__(self, id, location):
        self.id = id
        self.location = location
        self.target_location = (-1, -1)

    def set_target_location(self, target_location):
        self.target_location = target_location

    def pickup(self, passenger):
        pass

class Taxi(Vehicle):
    def __init__(self, id, location):
        super().__init__(id, location)

    def pickup(self, passenger):
        self.set_target_location(passenger.target_location)

class Minibus(Vehicle):
    def __init__(self, id, location):
        super().__init__(id, location)

    def pickup(self, passenger):
        self.set_target_location(passenger.target_location)

class TaxiCompany:
    def __init__(self):
        self.vehicles = []
        self.assignments = {} # k,v = (vehicle_id, passenger_name)

    def register(self, vehicle):
        self.vehicles.append(vehicle)

    def request_pickup(self, passenger):
        v = self.schedule_vehicle(passenger)
        if v:
            self.assignments[v.id] = passenger.name
            v.pickup(passenger);
            return True
        else:
            return False

    def schedule_vehicle(self, p):
        for v in self.vehicles:
            if v.target_location == (-1,-1):
                if abs(v.location[0] - p.location[0]) < 10 and abs(v.location[1] - p.location[1]) < 10:
                    return v

class Passenger:
    def __init__(self, name, location, target_location):
        self.name = name
        self.location = location
        self.target_location = target_location

# main
tc = TaxiCompany()
t1 = Taxi('taxi-one', (1, 1))
t2 = Taxi('taxi-two', (2, 2))
m1 = Minibus('bus-one', (0, 0))
m2 = Minibus('bus-two', (0, 0))

tc.register(t1)
tc.register(t2)
tc.register(m1)
tc.register(m2)

p1 = Passenger('John', (4,4), (5,0))
p2 = Passenger('Mary', (5,5), (6,0))
p3 = Passenger('Ann',  (2,2), (7,0))
p4 = Passenger('Paul', (11,3), (7,0))
p5 = Passenger('Sue',  (13,8), (7,0))

for p in (p1, p2, p3, p4, p5):
    if tc.request_pickup(p):
        print(p.name, 'is picked-up by a taxi')
    else:
        print('No taxi available for passenger', p.name)

print()
for v, p in tc.assignments.items():
    print(p, "will be served by", v)

