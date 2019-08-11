# Using map fumction:
income = [10, 30, 75]

def double_money(dollars):
    return dollars * 2

# What we can do is use a for loop to double the value of all the items in the list but MAP FUNCTION becomes handy

new_income = list(map(double_money, income))        # It takes in 2 variables. one is the function that we want to run and the
                                                    # 2nd is the list we want to iterate through
print(new_income)                                   # 'list' functions converts the numbers into a list
