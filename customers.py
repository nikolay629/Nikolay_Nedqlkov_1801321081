class Customers:
    name = ''
    cars = {}

    def __init__(self, name):
        self.name = name

    def add_customer_cars(self, car, hours):
        self.cars[len(self.cars) + 1] = [car, hours]

    def get_customer_cars(self):
        return self.cars

    def get_customer_name(self):
        return self.name

    def clear_cars(self):
        self.cars.clear()
