# import math
# print("The Square root of 16 is",math.sqrt(16))


# from math import pi
# print("pi is",pi)

# import random as r
# print(r.randint(100,200))

try:
    from tabulate import tabulate
    data=[["Product","Price","Stock"],["Laptop",999.99,45],["Mouse",24.99,128],["Keyboard",59.99,89]]
    print(tabulate(data, headers="firstrow",tablefmt="fancy_grid"))
except ImportError:
    print("tabulate module not installed. Install it using: pip install tabulate")

