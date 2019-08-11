def health(age, apples, cigs):
    life = (100 - age) + (apples * 3.5) - (cigs * 1.5)
    print(life)

my_data = [18, 2, 0]
health(my_data[0], my_data[1], my_data[2])
'''
the above method is very tedious so the lower method is used which
effectively reduces coding and puts the values in the given list accordingly 
'''
health(*my_data)