def chicken(*args): # this is used as a notation to use as many number of arguments as we want
    # for the time being chicken() is used to add as many numbers as we want
    # basically *args is the notation used to add as many arguments as we want to use in the function chicken
    total = 0
    for x in args:
        total += x

    print(total)

chicken(3)
chicken(3, 32)
chicken(3, 32, 567, 78223, 4513)
