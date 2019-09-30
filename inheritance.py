class Bird:
    def intro(self):
        print("There are many types of birds.")
    def flight(self):
        print("Most of the birds can fly but some can not")

# Bird is parent class & Sparrow is child class; All propertis of 'Bird'
# will be inherited by 'sparrow'; this is knows as inheritance in programming
class Sparrow(Bird):
    def size(self):
        print("Sparrows are smaller in size")
    # Method overriding:Overridding the method of parent class
    def flight(self):
        print("Sparrow can fly")


sparrow_obj = Sparrow()

sparrow_obj.intro()
sparrow_obj.flight()
sparrow_obj.size()

bird_obj = Bird()
bird_obj.flight()

# polymorphism: Having many forms, 2 different classes have same method
# https://www.geeksforgeeks.org/polymorphism-in-python/
