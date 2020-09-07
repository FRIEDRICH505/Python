class Car:
    def __init__(self, make, model, year,manufacturer):
        self.make = make
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()
    def read_odometer(self):
            print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        def increment_odometer(self, miles):
            self.odometer_reading += miles
class ElectricCar(Car):
        def __init__(self, make, model, year,manufacturer):
            super().__init__(make, model, year, manufacturer)
my_tesla = ElectricCar('tesla', 'model s', 2019, 'tesla')
print(my_tesla.get_descriptive_name())
