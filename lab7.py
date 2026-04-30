class Vehicle:
    def __init__(self, vid, model, year):
        self.vid = vid
        self.model = model
        self.year = year

    def __str__(self):
        return f"VID: {self.vid} | {self.model} ({self.year})"

    def is_new(self, n):
        return self.year >= 2026 - n

    def __eq__(self, other):
        return self.vid == other.vid

class Car(Vehicle):
    def __init__(self,vid,model,year,fuel,doors):
        super().__init__(vid,model,year)
        self.fuel= fuel
        self.doors=doors

    def __str__(self):
        return f"[Car] {self.vid }|{self.model} |{self.year} | {self.fuel} | {self.doors}doors"

class Truck(Vehicle):
    def __init__(self,vid, model,year,load,axles):
        super().__init__(vid, model, year)
        self.load=load
        self.axles=axles

    def __str__(self):
        return f"[Truck] {self.vid} | {self.model} | {self.year} | {self.load}kg | {self.axles}axles "

class Motorcycle(Vehicle) :
    def __init__(self,vid,model,year,cc,motortype):
        super().__init__(vid,model,year)
        self.cc=cc
        self.motortype=motortype

    def __str__(self):
        return f"[Motorcycle] {self.vid}|{self.model}|{self.year} | {self.cc}cc |{self.motortype} "



def load_fleet_from_file(filename):
    vehicles = []
    file = open(filename, "r")

    for line in file:
        data = line.strip().split(",")

        if data[0] == "Car":
            vehicles.append(Car(data[1], data[2], int(data[3]), data[4], int(data[5])))

        elif data[0] == "Truck":
            vehicles.append(Truck(data[1], data[2], int(data[3]), int(data[4]), int(data[5])))

        elif data[0] == "Motorcycle":
            vehicles.append(Motorcycle(data[1], data[2], int(data[3]), int(data[4]), data[5]))

    file.close()
    return vehicles
