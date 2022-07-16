
'''
Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
'''

class Vehicle:
    def __init__(self, max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        print(max_speed,mileage)


modelX = Vehicle(240,180)
