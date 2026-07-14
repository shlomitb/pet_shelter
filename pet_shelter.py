import json
from pet import Pet

class PetShelter:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def __str__(self):
        pets_string = ""

        for pet in self.pets:
            pets_string += str(pet) + "\n"

        return (
            f"Shelter: {self.name}\n"
            f"Pets:\n"
            f"{pets_string}"
        )

    def add_pet(self, pet):
        """
        Add a new pet to the shelter
        :param pet:
        :return:
        """
        if self.find_pet(pet.name) is None:
            self.pets.append(pet)
        else:
            print(f"A pet with this name {pet.name} already exists.")

    def remove_pet(self, name):
        """
        Remove a pet from the shelter
        :param name:
        :return:
        """
        pet = self.find_pet(name)
        if pet is not None:
            self.pets.remove(pet)

    def find_pet(self, name):
        for pet in self.pets:
            if pet.name == name:
                return pet
        return None

    def get_all_pets(self):
        return self.pets

    def get_number_of_pets(self):
        if len(self.pets) == 0:
            print("There are no pets in the shelter.")
            return 0

        return len(self.pets)

    def show_all_pets(self):
        for pet in self.pets:
            print(pet)

    def feed_all_pets(self):
        for pet in self.pets:
            pet.feed()

    def play_with_all_pets(self):
        for pet in self.pets:
            pet.play()

    def find_hungriest_pet(self):
        if len(self.pets) == 0:
            return None

        hungriest_pet = self.pets[0]
        for pet in self.pets:
            if pet.hunger > hungriest_pet.hunger:
                hungriest_pet = pet

        return hungriest_pet

    def to_dict(self):
        return {
            "name": self.name,
            "pets": [pet.to_dict() for pet in self.pets]
        }

    def save(self, filename):
        shelter_dict = {
            "name": self.name,
            "pets": []
        }

        for pet in self.pets:
            shelter_dict["pets"].append(pet.to_dict())

        with open(filename, "w") as file:
            json.dump(shelter_dict, file, indent=4)
    # def save(self, filename):
    #     with open(filename, "w") as file:
    #         json.dump(self.to_dict(), file, indent=4)


    def load(self, filename):
        with open(filename, "r") as file:
            shelter_dict = json.load(file)

        self.name = shelter_dict["name"]
        self.pets = []

        for pet_dict in shelter_dict["pets"]:
            pet = Pet(
                pet_dict["name"]
            )

            pet.hunger = pet_dict["hunger"]
            pet.happiness = pet_dict["happiness"]

            self.pets.append(pet)



    def vaccinate_all_pets(self):
        for pet in self.pets:
            pet.vaccinate()

    def remove_adopted_pets(self):
        for pet in self.pets:
            if pet.is_adopted:
                pets.remove(pet)



    """
    Optonal later methods:
    pet_exists()

find_oldest_pet()

find_youngest_pet()

sort_by_name()

sort_by_age()

    """

pet1 = ""
pet2 = ""
pet3 = ""

pets = [pet1, pet2, pet3]

