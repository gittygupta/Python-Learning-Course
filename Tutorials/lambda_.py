# lambda function is used to create a small function without any name

answer = lambda x: x*7      # it takes variable x, multiplies by 7 and prints in the variable 'answer'
print(answer(5))

#Another method

def answer(x):
    x = x * 7
    print(x)

answer(5)

# thus using lambda we can short down coding this way into 1 single line
