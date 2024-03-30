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

class Car ():
    # atrybut klasowy 
    # kind = 'skoda'

    def __init__(self, kind) -> None:
        self.kind = kind

    def driving (self):
        return 'Jedziemy'
    
# instncja klasy
carOne = Car('skoda')
carTwo =Car('skoda')

print(id(carOne))
print(id(carTwo))

# II przykład 

class Runner():
    def __init__(self, suit) -> None:
        self.suit = suit

class Shoes():
    def __init__(self, kind) -> None:
        self.kind = kind

shoes = Shoes('Nike')
runner = Runner(shoes)

print(runner.suit.kind)

# dekoratory 
def upperCase (func):
    def wrapper (*args, **kwargs):
        return func (*args, **kwargs).upper()
    return wrapper

@upperCase
def hello (name):
    return f"Cześć, {name}"

@upperCase
def today():
    return 'Dziś jest super pogoda'

print(today())
print(hello('Tomek'))

