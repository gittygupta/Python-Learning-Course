class Girl:

    gender = 'female'       # class variable which is common to all

    def __init__(self, name):
        self.name = name        # instance variable which is unique to a name

a = Girl('Rachel')      # this is the way to assign a value to the function when a parameter is present
b = Girl('Stanky')

print(a.gender)
print(b.gender)
print(a.name)
print(b.name)
 


