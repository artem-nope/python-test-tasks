# house(add flats, delete flat, add new owner, delete owner) and flats(price, floor, square, count on floor)
class House:
    def __init__(self, street, house_number):
        self.street = street
        self.house_numer = house_number
        self.flats = []

    def add_flat(self, number, price, floor, square, count_on_floor, owner):
        flat = Flat(number, price, floor, square, count_on_floor, owner)
        self.flats.append(flat)
        return 'A new flat has been added'

    def remove_flat(self, number):
        for f in self.flats:
            if f.get('number') == number:
                self.flats.remove(f)
        return 'The flat has been removed'

    def update_flat_owner(self, number, owner):
        for f in self.flats:
            if f.get('number') == number:
                f.set_owner(owner)
        return 'The flats owner has been updated'

    def remove_owner(self, number, owner):
        for f in self.flats:
            if f.get('number') == number:
                f.set_owner(None)
        return 'The flats owner has been deleted'

    def get_all_flats(self):
        result_lst = []
        for i in self.flats:
            result_lst.append(i.get_info_to_dict())
        return result_lst

    def get_all_flats_cnt(self):
        return len(self.flats)


class Flat:
    def __init__(self, number, price, floor, square, count_on_floor, owner):
        self.number = number
        self.price = price
        self.floor = floor
        self.square = square
        self.count_on_floor = count_on_floor
        self.owner = owner

    def get_info_to_dict(self):
        return {
            'numer': self.number,
            'price': self.price,
            'floor': self.floor,
            'square': self.square,
            'count_on_floor': self.count_on_floor,
            'owner': self.owner
        }

    def get_info_to_str(self):
        return f'{self.number} - {self.price} - {self.floor} - {self.square} - {self.count_on_floor}'

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_floor(self):
        return self.floor

    def set_floor(self, floor):
        self.floor = floor

    def get_square(self):
        return self.square

    def set_square(self, square):
        self.square = square

    def get_count_on_floor(self):
        return self.count_on_floor

    def set_count_on_floor(self, count_on_floor):
        self.count_on_floor = count_on_floor

    def get_owner(self):
        return self.owner

    def set_owner(self, owner):
        self.owner = owner

house = House('street', 123)
house.add_flat(1, 10000, 1, 50, 5, "owner")
house.add_flat(2, 11000, 1, 50, 5, "owner1")
print(house.get_all_flats())