foods = ['bacon' , 'tuna' , 'ham' , 'chicken' , 'fish']

for f in foods:
    print(f)
    print(len(f))


numbers = [1,2,3,4,5]

for i in numbers:
    for j in numbers[:i]:
        print(j, end=" ")
    print('\r')
