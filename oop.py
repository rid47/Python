#Defining a class
class Dog():
    #instance variable, used to initialize an object also called properties
    def __init__(self,name="Tom",age=0,furcolor=""):
        self.name=name
        self.age = age
        self.furcolor=furcolor
    # Method inside a class
    def bark(self,s):
        print(f"BARK! {s}")

    # defining what's going to return when class object is called
    def __str__(self):
        return self.name

# Creating an object (member of a class) from class; also known as instance of
# the class
defaultDog = Dog()
mydog = Dog("fido",13,"brown")
print(defaultDog)
print(mydog)
defaultDog.bark("Kkkkk")
mydog.bark("Grrrrrr")
