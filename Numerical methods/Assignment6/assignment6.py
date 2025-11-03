# %% [markdown]
# # Assignment 6
# **Author:** Lan Stare
# **Date:** 2. 11. 2025

# %% [markdown]
# ### (a)

# %%
from IPython.display import Image, display

# Replace with your file path
image_path = "ex_a.jpeg"

display(Image(filename=image_path))

# %% [markdown]
# ### (b)

# %%
import numpy as np
import math

def Newton(F, JF, u0, max_iter, max_err):
    uk = np.array(u0)
    errors = []
    for k in range(max_iter):
        delta = np.linalg.solve(JF(uk), -F(uk)) 
        uk_new = uk + delta
        err = np.linalg.norm(uk_new - uk)
        errors.append(err)
        
        if err < max_err:
            return uk_new, k + 1, np.array(errors)
        uk = uk_new
    return uk, max_iter, np.array(errors)

# %% [markdown]
# ### (c)

# %%
#computation of example
F = lambda u: np.array([-u[0] * math.exp(-(u[0]**2 + u[1]**2)/2),
    -u[1] * math.exp(-(u[0]**2 + u[1]**2)/2)])

JF = lambda u: math.exp(-(u[0]**2 + u[1]**2)/2) * np.array([[u[0]**2 - 1, u[0]*u[1]],
    [u[0]*u[1], u[1]**2 - 1]])

x0 = (0.25, 0.25)
max_iterations = 1000
max_tolerance = 10**-8
solution_f, iters_f, errs_f = Newton(F, JF, x0, max_iterations, max_tolerance)
print(solution_f, iters_f, errs_f)

#plotting the graph
import matplotlib.pyplot as plt

plt.figure()
plt.semilogy(range(1, len(errs_f)+1), errs_f, 'o-', label="f(x)")
plt.xlabel("Iteration number")
plt.ylabel("Absolute error (log scale)")
plt.title("Newton's Method convergence for f(x)")
plt.legend()
plt.savefig("newton_error_f.png", dpi=200)
plt.show()

# %% [markdown]
# ### (d)

# %%
#calculation
F_logf = lambda u: np.array([-u[0], -u[1]])
JF_logf = lambda u: np.array([[-1, 0],[0, -1]])

#plotting
solution_logf, iters_logf, errs_logf = Newton(F_logf, JF_logf, x0, max_iterations, max_tolerance)

plt.figure()
plt.semilogy(range(1, len(errs_logf)+1), errs_logf, 'o-', label="log(f(x))", color='orange')
plt.xlabel("Iteration number")
plt.ylabel("Absolute error (log scale)")
plt.title("Newton's Method convergence for log(f(x))")
plt.legend()
plt.grid(True)
plt.savefig("newton_error_logf.png", dpi=200)
plt.show()

# %% [markdown]
# For f, Newton's method converges in 4 iterations while for log(f), it converges in 1 iteration. This is because the Hessian is -I (so it's constant). That's because in the first loop, our update is: $u_{k+1} = u_{k} - (-I)^{-1}(-u_{k}) = 0$


