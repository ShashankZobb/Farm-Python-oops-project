import animal_model


class Farm:
    def __init__(self):
        self.Animals_in_farm = []

    def create_new_animal(self):
        print("Name of the animal: ")
        name = input().rstrip().lower()
        print("Year of birth of the animal: ")
        year_birth = int(input().rstrip())
        print("Weight of the animal in killogram: ")
        weight_in_killogram = int(input().rstrip())
        if name == "cow":
            new_animal = animal_model.Cow(weight_in_killogram, year_birth)
            self.Animals_in_farm.append(new_animal)
        elif name == "dog":
            new_animal = animal_model.Dog(weight_in_killogram, year_birth)
            self.Animals_in_farm.append(new_animal)
        elif name == "horse":
            new_animal = animal_model.Horse(weight_in_killogram, year_birth)
            self.Animals_in_farm.append(new_animal)
        else:
            print("Sorry this animal is not registered in the farm")

    def show_number_total_animals(self, animal_type=None):
        if animal_type is None:
            return len(self.Animals_in_farm)
        else:
            animal_type = animal_type.title()
            no_of_animal = 0
            for animals in self.Animals_in_farm:
                if animals.name == animal_type:
                    no_of_animal += 1
            return no_of_animal

    def show_number_animals_without_food(self, animal_type=None):
        number_of_animal_without_food = 0
        if animal_type is None:
            for animals in self.Animals_in_farm:
                if animals.has_food() == False:
                    number_of_animal_without_food += 1
        else:
            animal_type = animal_type.title()
            for animals in self.Animals_in_farm:
                if animals.name == type:
                    if animals.has_food() == False:
                        number_of_animal_without_food += 1
        return number_of_animal_without_food

    def show_number_animals_recollected(self, animal_type=None):
        number_of_collected_animal = 0
        if animal_type is None:
            for animals in self.Animals_in_farm:
                if animals.is_collected() == True:
                    number_of_collected_animal += 1
        else:
            animal_type = animal_type.title()
            for animals in self.Animals_in_farm:
                if animals.name == type:
                    if animals.is_collected() == True:
                        number_of_collected_animal += 1
        return number_of_collected_animal

    def show_old_animals(self, year, animal_type=None):
        no_of_animals = 0
        if animal_type is None:
            for animals in self.Animals_in_farm:
                if animals.show_age() > year:
                    no_of_animals += 1
        else:
            animal_type = animal_type.title()
            for animals in self.Animals_in_farm:
                if animals.name == animal_type:
                    if animals.show_age() > year:
                        no_of_animals += 1
        return no_of_animals

    def show_animals_with_smaller_weight(self, weight=None, animal_type=None):
        no_of_animals = 0
        if animal_type is None:
            for animals in self.Animals_in_farm:
                if weight is None:
                    if animals.weight_in_killogram < animals.weight_tope_desnutricion:
                        no_of_animals += 1
                else:
                    if animals.weight_in_killogram < weight:
                        no_of_animals += 1
        else:
            animal_type = animal_type.title()
            for animals in self.Animals_in_farm:
                if animals.name == animal_type:
                    if weight is None:
                        if animals.weight_in_killogram < animals.weight_tope_desnutricion:
                            no_of_animals += 1
                    else:
                        if animals.weight_in_killogram < weight:
                            no_of_animals += 1
        return no_of_animals
