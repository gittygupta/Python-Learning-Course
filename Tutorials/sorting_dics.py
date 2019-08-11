stocks = {  "GOOG": 520.54,
            "YHOO": 54.23,
            "APPL": 300.33,
            "REDT": 450.02,
            "AMZN": 500.65
            }

# We cannot sort dictionaries together, but we can sort two lists
# When python sorts lists, it sorts it through the first element of the list
# While zipping, it either sorts through the name or the price, depending on the one that we put first

# Sorting through values
print('Min:', min(zip(stocks.values(), stocks.keys())))        # to get the minimum value in the list
print('Max:', max(zip(stocks.values(), stocks.keys())))
# it gave us the minimum price, because the 1st list consisted of values and not keys

print('\n', 'Sorting by values:')
print(sorted(zip(stocks.values(), stocks.keys())))      # sorting by values

print('\n', 'Sorting by keys:')
print(sorted(zip(stocks.keys(), stocks.values())))      # sorting by keys