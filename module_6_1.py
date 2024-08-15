class Plant:
    edible = False

    def __init__(self, name_plant):
        self.name_plant = name_plant


class Animal:
    alive = True
    fed = False

    def __init__(self, name_animal):
        self.name_animal = name_animal

    def eat(self, food: Plant):
        if food.edible:
            self.fed = True
            print(f'{self.name_animal} съел {food.name_plant}')
        else:
            self.alive = False
            print(f'{self.name_animal} не съел {food.name_plant}')


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True
    pass


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name_animal)
print(p1.name_plant)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

