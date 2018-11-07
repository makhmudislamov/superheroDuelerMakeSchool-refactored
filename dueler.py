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


my_dog = Dog("Spot")
print(my_dog.name)
