# %% [markdown]
# # Assignment 10
# **Author:** Lan Stare
# **Date:** 25. 11. 2025

# %% [markdown]
# ### (a)

# %% [markdown]
# Remark: We chose the coefficient of $t * p_{n - 1}$ to be 1, so we don't have to prove that $\delta_{n} = 1$.

# %% [markdown]
# ![solution to the exercise a](ex_a.jpeg)

# %% [markdown]
# ### (b)

# %%
import numpy as np

#first we need to compute the gamma_k:
def gamma(k):
    if k == 1:
        return 0
    return (k - 1) / np.sqrt(4 * (k - 1)**2 - 1)


def get_gaussian_nodes_and_weights(n):
    main_diag = np.zeros(n) #elements in the diagonal AKA delta(n) = 0
    off_diag = np.array([gamma(k) for k in range(2, n+1)]) #The elements beside the diagonal AKA gamma(n). We are using gamma2, gamma3, ..., gamma(n)
    
    Jn = np.diag(main_diag) + np.diag(off_diag, k=1) + np.diag(off_diag, k=-1) # this is how the np combines the diagonal matrices
    
    #getting eigenvalues and eigenvectors:
    eigen_values, eigen_vectors = np.linalg.eig(Jn)     #so now eigen_values = nodes
    
    #calculating the weights:
    v1 = eigen_vectors[0, :]    # first row contains first components of each eigenvector
    lenght = np.sum(v1 ** 2) #we need to normalize the vectors
    
    weights = 2 * v1 ** 2 / lenght  #calculating the weights by the formula
        
    calculated_nodes_and_weights = list(zip(eigen_values, weights))     #combine the nodes and their weights
    
    #built in function check:
    generated_nodes_and_weights = np.polynomial.legendre.leggauss(n)
    return calculated_nodes_and_weights, generated_nodes_and_weights

print(get_gaussian_nodes_and_weights(4))

# %% [markdown]
# ### (c)

# %%
n = 4

#first we translate f like we learnt in the lecture:
def g(t):
    return np.sin(np.pi / 2 * (1 + t))      #this was done by hand on paper

#now let's calculate the QR:
J_tilda = 0
nodes_with_weights_lst = get_gaussian_nodes_and_weights(n)[0]
for i in range(n):
    ci, bi = nodes_with_weights_lst[i]
    J_tilda += bi * g(ci)
    
J_tilda

# %% [markdown]
# Comment: The absolute value is approximately 0.237 when n = 4


