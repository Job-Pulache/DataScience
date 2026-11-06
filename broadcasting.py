import numpy as np
prices = np.array([100, 200, 300])
discount = np.array([0.9])
discount_prices = prices * discount
print(discount_prices)

prices = np.random.randint(100, 500, size=(3,3))
discount = np.array([10,20,30])
discount_prices = prices + discount
print(prices)
print(discount_prices)
