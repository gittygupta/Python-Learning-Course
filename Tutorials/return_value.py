def allowed(age):
    girls_age = age/2 + 7
    return girls_age

allowed(30) # does not print anything

limit = allowed(30)
print('I can date girls with age ', limit, 'or older')