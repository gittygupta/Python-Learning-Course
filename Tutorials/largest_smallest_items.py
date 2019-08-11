import heapq
# It allows to sort stuff really easily
# Specifically you don't need to sort the list, in fact you can print the first 3 largest integers maybe

grades = [32, 43, 654, 34, 132, 66, 99, 532]
print(heapq.nlargest(3, grades))         # it takes in the number of largest/smallest things we want to find and the list.

# Another older way, and complicated, but i think its easier and rememberable

sorted_list = list(sorted(grades, reverse =True))
print(sorted_list)

for i in range(3):
    print(sorted_list[i], " ", end = "")

'''
In the image provided it is explained how to print or sort in a dictionary, according to the keyword we want to sort
'''
