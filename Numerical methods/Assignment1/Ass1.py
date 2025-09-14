# %% [markdown]
# # Assignment 1
# **Author:** Lan Stare
# **Date:** 14. 9. 2025

# %% [markdown]
# 
# ### (a)

# %%
import numpy as np
import matplotlib.pyplot as plt

N = 5000

x = np.linspace(10**(-9), 10**(-6), N)
y = (1 - np.cos(x)) / (x**2)
plt.semilogx(x, y, label='f(x)')
plt.grid(True)

plt.show()

# %% [markdown]
# ### (b)
# 
# The result is different from the function (1), because for very small values of x, (1 - cos(x)) is close to 0 but the x^2 is even smaller (x^2 is approximately 10^(-18) when x is 10^(-9)). This means that the function (1) is very large for small values of x. This is a problem because the computer has limited precision and cannot represent very small numbers accurately. When we compute (1 - cos(x)), we are subtracting two numbers that are very close to each other, which leads to a loss of precision called (cancellation). This produces the plateau in the graph. The oscillations are due to the fact that when x is very small, small changes in x lead to large changes in the evaluation of cos(x) and the subtraction (1 - cos(x)). Sometimes the rounded value of cos(x) is slightly less and sometimes slightly more than the true value, leading to oscillations in the result.

# %% [markdown]
# 
# ### (c)

# %%
N = 5000

x = np.linspace(10**(-9), 10**(-6), N)
y2 = 0.5 * (np.sin(x/2) / (x/2))**2
plt.semilogx(x, y2, label='f(x)')
plt.grid(True)

plt.show()

# %%



