class Mammal:
     def Eat(self):
         print("Animals Eat!")


class Dog(Mammal):
    def barks(self):
        print("ROOOF ROOF")

class Cat(Mammal):
    def Meow(self):
        print("Meow Meow")
# Objects
print("Dog")
D = Dog()
D.Eat()
D.barks()

print("Cat")
C = Cat()
C.Eat()
C.Meow()
