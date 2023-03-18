class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hunger = 0
        self.energy = 100
        self.mood = "happy"

    def meow(self):
        print("Meow!")
        self.hunger += 10
        self.energy -= 5
        self.update_mood()

    def eat(self, food):
        print("Yum, thanks for the " + food + "!")
        self.hunger -= 20
        self.energy += 10
        self.update_mood()

    def nap(self):
        print("Zzz...")
        self.energy += 30
        self.hunger += 5
        self.update_mood()

    def update_mood(self):
        if self.hunger >= 50 or self.energy <= 20:
            self.mood = "grumpy"
        else:
            self.mood = "happy"

    def __str__(self):
        return f"{self.name} " \
               f"is a {self.age} " \
               f"year old cat. They are {type(self).__name__} " \
               f"and their energy level is {self.energy}. " \
               f"Their hunger level is {self.hunger}. " \
               f"Their mood is {self.mood}."


if __name__ == '__main__':
    a = int(12)
    cat = Cat("Barsik", 12)

    print(cat.name)
    print(cat.age)
    print(cat.hunger)
    print(cat.energy)
    print(cat.mood)

    cat.meow()

    print(cat.name)
    print(cat.age)
    print(cat.hunger)
    print(cat.energy)
    print(cat.mood)
    print(cat)
