import random
import datetime


class Animal:
    def __init__(self, name, weight_in_killogram, year_birth, weight_tope_desnutricion):
        self.name = name
        self.weight_in_killogram = weight_in_killogram
        self.year_birth = year_birth
        self.weight_tope_desnutricion = weight_tope_desnutricion


class Cow(Animal):
    def __init__(self, weight_in_killogram, year_birth):
        super().__init__("Cow", weight_in_killogram, year_birth, 200)
        self.is_carnivore = False
        self.is_hervivoro = True
        self.is_mamifero = True
        self.minimum_weight_in_killogram = 150
        self.maximum_weight_in_killogram = 400

    def is_collected(self):
        return random.randint(0, 1) == 1

    def has_food(self):
        return random.randint(0, 1) == 1

    def show_age(self):
        current_date_object = datetime.date.today()
        current_year = current_date_object.year()
        print(f"This cow is {current_year- self.year_birth} years old")

    def yell(self):
        print("MOO")

    def weight(self):
        self.weight_in_killogram = random.randint(
            self.minimum_weight_in_killogram, self.maximum_weight_in_killogram)


class Dog(Animal):
    def __init__(self, weight_in_killogram, year_birth):
        super().__init__("Dog", weight_in_killogram, year_birth, 16)
        self.is_carnivore = True
        self.is_hervivoro = True
        self.is_mamifero = True
        self.minimum_weight_in_killogram = 12
        self.maximum_weight_in_killogram = 40

    def is_collected(self):
        return random.randint(0, 1) == 1

    def has_food(self):
        return random.randint(0, 1) == 1

    def show_age(self):
        current_date_object = datetime.date.today()
        current_year = current_date_object.year()
        return current_year - self.year_birth

    def yell(self):
        print("WOOF WOOF")

    def weight(self):
        self.weight_in_killogram = random.randint(
            self.minimum_weight_in_killogram, self.maximum_weight_in_killogram)


class Horse(Animal):
    def __init__(self, weight_in_killogram, year_birth):
        super().__init__("Horse", weight_in_killogram, year_birth, 400)
        self.is_carnivore = False
        self.is_hervivoro = True
        self.is_mamifero = True
        self.minimum_weight_in_killogram = 300
        self.maximum_weight_in_killogram = 1000

    def is_collected(self):
        return random.randint(0, 1) == 1

    def has_food(self):
        return random.randint(0, 1) == 1

    def show_age(self):
        current_date_object = datetime.date.today()
        current_year = current_date_object.year()
        print(f"This cow is {current_year- self.year_birth} years old")

    def yell(self):
        print("NEIGH")

    def weight(self):
        self.weight_in_killogram = random.randint(
            self.minimum_weight_in_killogram, self.maximum_weight_in_killogram)
