class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hunger = 80
        self.happiness = 0
        self.is_vaccinated = False
        self.is_adopted = False

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Hunger: {self.hunger}\n"
            f"Happiness: {self.happiness}"
        )

    def eat(self):
        self.hunger -= 20
        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name} ate.")

    def play(self):
        self.happiness += 15
        self.hunger += 10

        if self.hunger > 100:
            self.hunger = 100

        if self.happiness > 100:
            self.happiness = 100

        print(f"{self.name} is playing!")

    def sleep(self):
        self.hunger += 5
        self.happiness += 5

        if self.hunger > 100:
            self.hunger = 100

        if self.happiness > 100:
            self.happiness = 100

        print(f"{self.name} is sleeping.")

    def time_passes(self):
        self.hunger += 20
        if self.hunger > 100:
            self.hunger = 100

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "hunger": self.hunger,
            "happiness": self.happiness
        }

    def vaccinate(self):
        if not self.is_vaccinated:
            self.is_vaccinated = True

    def adopt(self):
        if not self.is_adopted:
            self.is_adopted = True

    # @classmethod
    # def from_dict(cls, pet_dict):
    #     pet = cls(
    #         pet_dict["name"],
    #         pet_dict["age"]
    #     )
    #
    #     pet.hunger = pet_dict["hunger"]
    #     pet.happiness = pet_dict["happiness"]
    #
    #     return pet