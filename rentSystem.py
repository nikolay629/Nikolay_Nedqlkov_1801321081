import json
from customers import Customers
from cars import Cars


def addCustomer(customer):
    car_list = Cars()
    car_list.get_available_cars()

    car_number = input("Enter number of car, which you want to take: ")
    hours = input("And enter hours for rent: ")
    while car_number is not '' and hours is not '':
        if car_list.is_available(car_number):
            car = car_list.set_unavailable_cars(str(car_number))
            customer.add_customer_cars(car, hours)
            car_list.get_available_cars()
            # print(car_number + " " + json.dumps(car, indent=4))
        else:
            print("This cart is unavailable, please choose another car!")

        car_number = input("If you want to get another car enter its number, or just press Enter: ")
        if car_number is '':
            break

        hours = input("And enter hours for rent: ")

    return customer.get_customer_cars()


def calculatePrice(cars):
    print(json.dumps(cars, indent=4))
    all_price = 0
    for car in cars:
        hour = int(cars[car][1])
        price = 0
        while hour > 0:
            if hour >= 168:
                price += getPricePerWeek(cars[car][0])
                hour -= 168
            elif hour >= 24:
                price += getPricePerDay(cars[car][0])
                hour -= 24
            else:
                price += getPricePerHour(cars[car][0], hour)
                break
        all_price += price
    if len(cars) >= 3:
        print(f"You rent cars for which you owe price: {all_price}")
        discount = all_price * 0.3
        print("But because you take 3 or more than 3 cars, we give you 30% discount for rent from price")
        print(f"Which value is {discount}")
        print(f"Now you should pay: {all_price - discount}")
    else:
        print(f"You should pay: {all_price}")


def getPricePerHour(car, hour):
    price_per_hour = int(car['price per hour'])
    return price_per_hour * hour


def getPricePerDay(car):
    price_per_day = int(car['price per day'])
    return price_per_day


def getPricePerWeek(car):
    price_per_week = int(car['price per week'])
    return price_per_week


class Rent:
    while True:
        customer = Customers(
            name=input('Enter your name: ')
        )
        customer_car = addCustomer(customer)
        print(customer.get_customer_name())
        calculatePrice(customer_car)
        customer.clear_cars()
        if input("If you want to add another customer insert 'yes' or 'no' (default 'no')") == "yes":
            continue
        break
