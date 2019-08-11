# Exception handling

while True:
    try:
        x = int(input('Enter your fav number: \n'))
        print(8/x)      # it can cause a ZeroDivisionError
        break

    except ValueError:          # "ValueError" means an exception
        print("ok dude you gotta try again")

    except ZeroDivisionError:
        print("Dude dont use 0")

    except:
        # this basically exits your program. Used in a wider angle to handle exceptions. Takes all exceptions
        break

    finally:        # the prog executes this line every time no matter what exception it encounters
        print("sorry dude you're dumb")
        