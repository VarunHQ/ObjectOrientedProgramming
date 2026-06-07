class Car:
    type = "car"

    def __init__(self, name, age):
        self.name = name
        self.age = age


toyota = Car("Toyota", 89)
bmw = Car("BMW", 110)

print("Toyota is a {}".format(toyota.type))
print("BMW is also a {}".format(bmw.type))
print("{} is {} years old".format(toyota.name, toyota.age))
print("{} is {} years old".format(bmw.name, bmw.age))
