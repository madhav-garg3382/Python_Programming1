class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def dog_info(self):
        return f"{self.name} is a {self.species}"
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def dog_info(self):
        return f"{self.name} is a {self.breed} breed of {self.species}"