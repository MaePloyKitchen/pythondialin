#Explore the Dot Operator in Python

class Person:

    num_of_persons = 0

    def __init__(self, name):
        self.name = name

    def shout(self):
        print(f"Hey! I'm {self.name}")

p = Person('John')
p.shout()
# Hey I'm John.

print(p.num_of_persons)
# 0

print(p.name)
# 'John'

print(vars(p))
#vars function prints all the self variables in a class definition 
