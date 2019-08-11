from operator import attrgetter             # attribute getter


class User:

    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    def __repr__(self):             # This is an in built function used to convert an object into a string variable
        return self.name + " : " + str(self.user_id)

users = [
    User('Bucky', 43),
    User('Sally', 5),
    User('Tuna', 61),
    User('Brain', 2),
    User('Joby', 77),
    User('Amanda', 9)
]                               # above is a ist of class 'User' objects

for user in users:
    print(user)

print('________________________________')

# Sorting:

print("By User ID:\n")
for user in sorted(users, key = attrgetter('user_id')):     # attrgetter is used when there is no key given, but only an object is passed like 'user_id'
    print(user)

print('________________________________')

print("By name:\n")
for user in sorted(users, key = attrgetter('name')):     # attrgetter is used when there is no key given, but only an object is passed like 'name'
    print(user)
