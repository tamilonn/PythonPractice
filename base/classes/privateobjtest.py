from privateobj import Computer


c = Computer()

# Original selling price
c.sell()

# Attempting to change the price directly (This won't work because __maxprice is a private attribute)
c.__maxprice = 1000
print(c.__maxprice)