"""
An animal shelter, which holds only dogs and cats, operates on a strictly "first in first out" basis. People must adopt either the oldest of all animals at the shelter
or they can select whether they would prefer a dog or a cat(and will receive the oldest animal of that type). They cannot select which specific animal they would like. Create
the data structure to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the build-in LinkedList data structure.
"""
class Dog:
    def __init__(self):
        self.time = 0
    
    def __repr__(self):
        return "Dog " + str(self.time)
    
    def setTime(self, time):
        self.time = time

class Cat:
    def __init__(self):
        self.time = 0
    
    def __repr__(self):
        return "Cat " + str(self.time)
    
    def setTime(self, time):
        self.time = time

class Animals:
    def __init__(self, dogs = [], cats = []):
        self.dogs = dogs
        self.cats = cats
    
    def enqueue(self, cats = [], dogs = []):
        if cats:
            time = 0
            for cat in cats:
                cat.setTime(time)
                time += 1
                (self.cats).append(cat)
        if dogs:
            time = 0
            for dog in dogs:
                dog.setTime(time)
                time += 1
                (self.dogs).append(dog)

    def dequeueAny(self):
        if len(self.cats) > len(self.dogs):
            self.cats.pop(0)
        else:
            self.dogs.pop(0)
    
    def dequeueDog(self):
        self.dogs.pop(0)
    
    def dequeueCat(self):
        self.cats.pop(0)


d_1 = Dog()
d_2 = Dog()
d_5 = Dog()
c_1 = Cat()
c_3 = Cat()
c_6 = Cat()

dogs = []
dogs.append(d_1)
dogs.append(d_2)
dogs.append(d_5)

cats = []
cats.append(c_1)
cats.append(c_3)
cats.append(c_6)

animals = Animals()

animals.enqueue(dogs = dogs, cats = cats)
print(animals.dogs, animals.cats)
animals.dequeueAny()
print(animals.dogs, animals.cats)
animals.dequeueCat()
print(animals.dogs, animals.cats)
animals.dequeueDog()
print(animals.dogs, animals.cats)