# HW
# class Garage
# add car
# count price
# del car by index
# del car by val
# find by model
# find max price car
# find min price car
# menu
class Garage:
    def __init__(self):
        self.cars = []

    def add_car(self, id, model, number, price):
        self.cars.append({
            'id': id,
            'model': model,
            'number': number,
            'price': int(price)
        })
        return 'Car has been added'

    def get_all_cars(self):
        for car in self.cars:
            print(car)

    def remove_car_by_id(self, id):
        for car in self.cars:
            if car.get('id') == id:
                self.cars.remove(car)
        return f'Car by id = {id} has been removed'

    def remove_car_by_number(self, number):
        for car in self.cars:
            if car.get('number') == number:
                self.cars.remove(car)
        return f'Car by number {number} has been removed'

    def remove_car_by_index(self, idx):
        if int(idx) < 0 or int(idx) > len(self.cars) - 1:
            return 'Car not found'
        self.cars.pop(int(idx))
        return f'Car by index {idx} has been removed'

    def find_car_by_gap_price(self, price_start, price_end):
        for car in self.cars:
            if int(price_start) <= int(car.get('price')) <= int(price_end):
                return car

    def find_car_by_max_price(self):
        car_max_price = self.cars[0]
        for car in self.cars:
            if int(car.get('price')) > car_max_price.get('price'):
                car_max_price = car
        return car_max_price

    def find_car_by_min_price(self):
        car_min_price = self.cars[0]
        for car in self.cars:
            if int(car.get('price')) < car_min_price.get('price'):
                car_min_price = car
        return car_min_price

    def get_all_cars_price(self):
        all_price = 0
        for car in self.cars:
            all_price += int(car.get('price'))
        return all_price

    def find_car_by_model(self, model):
        cars_by_model = []
        for car in self.cars:
            if car.get('model') == model:
                cars_by_model.append(car)
        return cars_by_model


garage = Garage()
while True:
    command = input('Command: ')
    if command == 'add car':
        id, model, number, price = input('Enter id, model, number, price: ').split()
        print(garage.add_car(id, model, number, price))
    elif command == 'get cars':
        garage.get_all_cars()
    elif command == 'delete car by id':
        id = input('Enter car id')
        print(garage.remove_car_by_id(id))
    elif command == 'delete car by number':
        number = input('Enter a car number: ')
        print(garage.remove_car_by_number(number))
    elif command == 'delete car by index':
        idx = input('Enter a car index: ')
        print(garage.remove_car_by_index(idx))
    elif command == 'find cars by prices':
        price1 = input('Enter a start price')
        price2 = input('Enter a end price')
        print(garage.find_car_by_gap_price(price1, price2))
    elif command == 'find cars by max prices':
        print(garage.find_car_by_max_price())
    elif command == 'find cars by min prices':
        print(garage.find_car_by_min_price())
    elif command == 'find all prices':
        print(garage.get_all_cars_price())
    elif command == 'find car by model':
        model = input('Enter a car model')
        print(garage.find_car_by_model(model))
    elif command == 'end':
        break
