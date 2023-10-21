class Person:
    def __init__(self, name):
        self.name = name

    def Talk(self):
        print(f"Talk to me {self.name}")

# The objects
hala = Person("Hilina Shambel")
mighty = Person("Mighty Shambel")
witty = Person("Witty Shambel")
hala.Talk()
mighty.Talk()
witty.Talk()
print(mighty.name)