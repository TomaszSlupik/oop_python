# 1. Klasa i instacja klasy 
# z przepisu powstaje spaghetti 
# W OOP z klas powstaje obiekty czyli juz istniejący 
class MyClass:
    pass

class Human:
    pass
# KLASA jest szablonem, przepisem. Metoda __init__ tez jest szablonem 
# v1
class Food:
    pass

myFood = Food ()
yourFood = Food()

print(myFood)
print(yourFood)

print('---')

# v2 
class Drink():
    pass

tomDrink = Drink()

if isinstance(tomDrink, object):
    print('Obiket jest instancją klasy')
else:
    print('Instancja nie jest')

# OBIEKT zwany instacją klasy (czyli takie danie ugotowowane z przepisu)
humanFirst  = Human()

# Klasa, atrybut i instancja klasy czyli obiekt 
class Human():
    # Atrybut klasy
    kind = 'homo sapiens'

humanOne = Human()
humanTwo = Human()

print(humanOne.kind, humanTwo.kind)
print(id(humanOne))
print(id(humanTwo))

print("---")

print('---')

# 2. METODA, a FUNKCJA
class Audi:
    def drive(self):
        return("jedziemy")
    def turn(self, direction):
        return (f"Skręcam w {direction}")
    def fuel(self, amount=10):
        return f"Pali {amount}"
        

myCar = Audi()

print(myCar.drive())
print(myCar.turn('prawo'))
print(myCar.fuel())

print('---')

# 3. Self - można z różnych metod odpalać inne metody 
# Self - odwołujej się do konkretnej instancji klasy 
class Coffee:
    def drink(self):
        return "Pijemy"
    def kind(self):
        return f"{self.drink()} dzisiaj costę"
    
myCoffee = Coffee()

print(myCoffee.kind())
    

print('---')

# 4. Self zawsze musi byc bo będzie błąd
class Calc:
    def addNumber (a, b):
        return a + b
    
    def num(a, b):
        return b
    
myCalc = Calc()
# print(myCalc.addNumber(10, 2))  --tutaj bedzie błąd

# W tym przypadku a bedzie selfem a b = 2 
print(myCalc.num(2))

print('---')

# 5. Magiczne metody: 
# Magiczna metoda __name__ nazywa główny plik
print(__name__)
print("---")

# __str__ - od razu zwróci nam Stringa 
class Drink():
    def __str__(self):
        return 'Piję coca cole'
    
myDrink = Drink()
print(myDrink)

print('---')

# 6. Magiczna metoda __init__
# Metoda __init__ czyli Konstruktor - Funkcja Inicjalizująca - do przechowywania atrybutów 

class Human():
    def __init__(self, kind) -> None:
        self.kind = kind

humamThree = Human('Homo sapiens')
print(humamThree.kind)

class Cook():
    def __init__(self, cook) -> None:
        self.cook = cook
        print(self.cook)


cook = Cook('Pierogi ruskie')

print(cook)
print('---')

# 7. Pola statyczne - properties

# Pola statyczne zawsze to samo da dla różnych instancji klas. Potwierdzenie to wynik tego samego ID
class Swim ():
    kind = 'grzbiet'
    def swimming():
        return f'Pływamy'

swim1 = Swim()
swim2 = Swim()

print(swim1.kind)
print(swim2.kind)
print(id((swim1.kind)))
print(id((swim2.kind)))
print('---')

# a tutaj sa 2 różne instacje bo korzystamy z self i właściwości przepisujemy do __init__
class Phone():
    def __init__(self, kind):
        self.kind = kind

phone1 = Phone('Iphone')
phone2 = Phone('Iphone')

print(id(phone1))
print(id(phone2))
print('---')

# 8. Metoda z właściowściami: 
class Sleep():
    def __init__(self, time) -> None:
        self.time = time
    def sleeping(self):
        return f"Dzisiaj śpimy {self.time}"
    
mySleep = Sleep(10)

print(mySleep.sleeping())
print('---')

# 9. Dziedziczenie - łączenie obiektów w Pythonie - czyli JEST 
class Food:
    def __init__(self, weight) -> None:
        self.weight = weight

    def eat(self):
        return f"Jemy"

class Fruit(Food):
    def __init__(self, kind, weight) -> None:
        self.kind = kind
        super().__init__ (weight)
    

myFood = Fruit('Pomarańcz', 20)

print(myFood.kind)
print(myFood.eat())
print(myFood.weight)

