from pet import Pet
from pet_shelter import PetShelter
from manager import Manager


def main():
    cat1 = Pet("Cat", 10)
    dog1 = Pet("Dog", 20)

    shelter = PetShelter("Shelter")
    print(shelter.get_number_of_pets())
    shelter.add_pet(cat1)
    shelter.add_pet(dog1)
    print(shelter.get_number_of_pets())
    manager = Manager("Ari", shelter)

    manager.feed_all_pets()



if __name__ == "__main__":
    main()