# class Dog:
#     def bark(self):
#         print("Woof!")

# my_dog = Dog()
# my_dog.bark()

# print(__name__)


class Dog:
    greeting = "Woof!"

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.greeting)


# creating dogs
my_dog = Dog("Spot")
dog1 = Dog("Ajax")
dog2 = Dog("Cookie")

# printing dog names
print(my_dog.name)
print(dog1.name)
print(dog2.name)

my_dog.bark()
dog1.bark()
dog2.bark()






