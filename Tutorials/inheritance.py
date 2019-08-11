class Parent():             # parenthesis is generally not given except in this case
    def last_name(self):
        print('Gupta')

class Child(Parent):         # this is how inheritance works in python, instead of typing 'extends'
    def first_name(self):
        print('Aousnik')

    def last_name(self):
        print('Snitch')      # Function overriding

name = Child()
name.first_name()
name.last_name()

# name inherited from both Child and Parent class

print('\n')
name1 = Parent()
name.first_name()
name1.last_name()