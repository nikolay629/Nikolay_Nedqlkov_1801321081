import json


class Cars:
    with open('carList.json') as json_data:
        cars = json.load(json_data)

    def get_available_cars(self):
        for car in self.cars:
            if self.cars[car]['available']:
                print(car + " " + json.dumps(self.cars[car]))

    def set_unavailable_cars(self, car_number):
        self.cars[car_number]['available'] = False
        return self.cars[car_number]

    def is_available(self, car_number):
        if car_number in self.cars and self.cars[car_number]['available']:
            return True
        return False
