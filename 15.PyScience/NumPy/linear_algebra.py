'''
Let's solve 4x + 5y = 20
x + 2y = 13
'''
import numpy as np
coefficients = np.array([[4, 5], [1, 2]])
dependents = np.array([20, 13])
answers = np.linalg.solve(coefficients, dependents)
print(answers)

product = np.dot(coefficients, answers)
print(product)