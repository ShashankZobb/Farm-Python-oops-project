import farm_model
import animal_model
import random
import datetime


while True:
    print("Enter 1 To create a farm.")
    print("Enter 2 exit the program.")
    choice = int(input().rstrip())
    if choice == 1:
        farm = farm_model.Farm()
        today = datetime.date.today()
        for counter in range(100):
            animal_type = random.choice(["Cow", "Dog", "Horse"])
            if animal_type == "Cow":
                weight_in_killogram = random.randint(150, 400)
                year_birth = random.randint(1950, today.year-1)
                new_animal = animal_model.Cow(weight_in_killogram, year_birth)
                farm.Animals_in_farm.append(new_animal)
            elif animal_type == "Dog":
                weight_in_killogram = random.randint(12, 40)
                year_birth = random.randint(1990, today.year-1)
                new_animal = animal_model.Dog(weight_in_killogram, year_birth)
                farm.Animals_in_farm.append(new_animal)
            else:
                weight_in_killogram = random.randint(300, 1000)
                year_birth = random.randint(1920, today.year-1)
                new_animal = animal_model.Horse(
                    weight_in_killogram, year_birth)
                farm.Animals_in_farm.append(new_animal)
        total_animals = farm.show_number_total_animals()
        number_of_cows = farm.show_number_total_animals("Cow")
        number_of_dogs = farm.show_number_total_animals("Dog")
        number_of_horse = farm.show_number_total_animals("Horse")
        number_of_animal_without_food = farm.show_number_animals_without_food()
        number_of_animal_collected = farm.show_number_animals_recollected()
        number_of_malnourished_animal = farm.show_animals_with_smaller_weight()
        print(f"The total number of animals in farm is {total_animals}.")
        print(
            f"The total number of animal of each type is Cow = {number_of_cows}, Dog: {number_of_dogs}, Horse: {number_of_horse}.")
        print(
            f"The total number of animals withour food is {number_of_animal_without_food}.")
        print(
            f"The total number of animals collected is {number_of_animal_collected}.")
        print(
            f"The total number of malnourished animals is {number_of_malnourished_animal}.")
        print()
        print("Enter 0 to go back.")
        choice = input().rstrip()
    else:
        break
