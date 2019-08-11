from operator import itemgetter

users = [
    {'fname': 'Bucky', 'lname': 'Roberts'},
    {'fname': 'Tom', 'lname': 'Roberts'},
    {'fname': 'Bernie', 'lname': 'Zunks'},
    {'fname': 'Jenna', 'lname': 'Hayes'},
    {'fname': 'sally', 'lname': 'Jones'},
    {'fname': 'Amanda', 'lname': 'Roberts'},
    {'fname': 'Tom', 'lname': 'Williams'},
    {'fname': 'Dean', 'lname': 'Hayes'},
    {'fname': 'Bernie', 'lname': 'Barbie'},
    {'fname': 'Tom', 'lname': 'Jones'}
]

# How to sort when there are more than 1 keys

for x in sorted(users, key = itemgetter('fname')):     # keyword 'sorted' takes in 3 values: 1. the dictionary 2. the key 3. reverse = True/False
    # 'itemgetter' allows us to fetch the keyword with which we want to sort the items in the given dictionary

    print(x)        # But the problem here is it sorts the 1st name accordingly bt the last names aren't sorted

print('______________________________________\n')

# How to fix this problem

for  x in sorted(users, key = itemgetter('fname', 'lname')):    # Here we can even use 2 keys, but the 1st one will be given preference
    print(x)
