class Vehicle:
    def __init__(self, fare, capacity):
        self.fare = fare
        self.capacity = capacity

class Bus(Vehicle):
    def __init__(self, fare, capacity):
        super().__init__(fare, capacity)

    def totalFare(self):
        return self.fare * self.capacity

bus = Bus(20, 35)
print("The total bus fare is", bus.totalFare())
