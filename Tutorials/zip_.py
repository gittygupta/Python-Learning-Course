first = ['Aousnik', 'Ronodeep', 'Anirban']
last = ['Gupta', 'Gupta', 'Chaudhuri']

names = zip(first, last)        # joins the first and last list in the tuples 'names'

for a, b in names:
    print(a, b)

''' this function just basically makes a list of tuples like:
    [('Aousnik', 'Gupta'), ('Ronodeep', Gupta), ('Anirban', 'Chaudhuri')]   just like tuples
'''

