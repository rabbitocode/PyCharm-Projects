

def add (*args):
    total = 0
    for number in args:
        total += number
    print(total)
add(1,5,7,1,2)



def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)


calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)