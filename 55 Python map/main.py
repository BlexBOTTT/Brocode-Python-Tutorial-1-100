# map() =   applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function,iterable)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

# converting to different currencies
#to_euros = lambda data: (data[0], data[1] * 0.82)
to_dollars = lambda data: (data[0], round(data[1] / 0.82))    # to dollars

#store_euros = list(map(to_euros, store))        # using list() to make map object to list iterable
store_dollars = list(map(to_dollars, store))           # to dollars

for i in store_dollars:
    print(i)