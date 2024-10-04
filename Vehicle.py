class Vehicle:
    wheel = 4


    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

tesla = Vehicle(180, 0)
lambo = Vehicle(350, 3)

print("Tesla Max Speed:", tesla.max_speed)
print("Tesla Mileage:", tesla.mileage)

print("Lambo Max Speed:", lambo.max_speed)
print("Lambo Mileage:", lambo.mileage)

print(f"Tesla and Labo Wheel: {tesla.wheel}, {lambo.wheel}")