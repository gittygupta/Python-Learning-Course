items = ['July, 2018', 'Chicken', 200]

# UNPACKING:

date, item, price = ['July, 2018', 'Chicken', 200]
# this is called unpacking a list of items

print(date)
print(price)

def drop_first_last(grades):
    first, *middle, last = grades
    # What this does is, it stores the 1st element and the last element and the "*" sign before "middle" ensures that "middle" stores all the rest of the variables, other than first and last
    avg = sum(middle) / len(middle)
    print(avg)

drop_first_last([10, 20, 30, 40, 50, 60, 70, 80, 90])

