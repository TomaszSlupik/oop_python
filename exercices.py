class Person():
    def __init__(self, name) -> None:
        self.name = name
        print(f'Powstaje nowy człowiek: {self.name}')

personOne = Person('Tomek')
personeTwo = Person('Aga')

print("---")
# Metoda 
class Coffee():
    def __init__(self, kind) -> None:
        self.kind = kind

    def go(self):
        return(f"Czas na {self.kind}")
coffeOne = Coffee('Costę')
print(coffeOne.go())

print('---')

# Dziedziczenie - JEST czyli łączenie obiektów, zeby unikać kopiowania 
class OldPerson:
    def __init__(self, age) -> None:
        self.age = age

class Children (OldPerson):
    def __init__(self, age, toy) -> None:
        super().__init__(age)
        self.toy = toy

    def play(self):
        return f"Bawimy sie. Mam dzisiaj {self.toy}"


myChild = Children(2, 'klocki lego')

print(f"Wiek {myChild.age}, Metoda : {myChild.play()}")
print(type(myChild))

print('---')

# __str__ - Metoda specjalna, wydrukowanie 
class Drink():
    def __str__(self) -> str:
        return f'Piję colę zero'
    
mydrink = Drink()
print(mydrink)

print(dir(mydrink))

print('---')

# 
