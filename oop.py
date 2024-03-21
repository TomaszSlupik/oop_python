# 1. Klasa i instacja klasy 
class Food:
    pass

myFood = Food ()
yourFood = Food()

print(myFood)
print(yourFood)

print('---')


# 2. Metoda, a Funkcja 
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
# __str__ - od razu zwróci nam Stringa 
class Drink():
    def __str__(self):
        return 'Piję coca cole'
    
myDrink = Drink()
print(myDrink)

print('---')
# 6. Pola statyczne - properties

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

# Metoda z właściowściami: 