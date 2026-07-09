class Manager:
    def __init__(self, name, shelter):
        self.name = name
        self.shelter = shelter

    def feed_all_pets(self):
        pets = self.shelter.get_all_pets()
        if len(pets) == 0:
            print("There were no pets to feed.")
        else:
            for pet in pets:
                pet.eat()