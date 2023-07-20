import numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
amount = [1, 5, 20, 450, 700]

plt.plot(days, amount)
plt.show()

plt.plot(days, amount, 'bs')
plt.show()

# ============================================================================

months = numpy.arange(1, 12, 1)

income = []
for m in months:
    income.append(100 + 3 * m)

print(income)

plt.plot(months, income, 'go')
plt.show()

cost = 50 + 10 * months
print(cost)

plt.plot(months, income, 'go', months, cost, 'r^')
plt.show()

# ============================================================================


x = np.arange(-5, 5, 0.1)
plt.xlabel('arguments')
plt.ylabel("values")
plt.plot(x, pow(2, x))
plt.show()
