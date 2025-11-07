# %% [markdown]
# # Assignment 8
# 
# **Author:** Lan Stare
# 
# **Date:** 7. 11. 2025

# %% [markdown]
# 
# ### Question 1
# 

# %% [markdown]
# ![solution to the question 1](1ex.jpeg)

# %% [markdown]
# ### Question 2
# 
# Note: If my writing at the bottom is too hard to read, I rewrote it below the picture.

# %% [markdown]
# ![solution to the question 2](2ex.jpeg)

# %% [markdown]
# EXPLANATION:
# This isn't a useful application of D&C, because the complexity if O(n), which is the same if we just traversed the array, adding the numbers up as we go.
# 
# The D&C is worse in this case, because it assumes that $n = 2^k ; k \geq 0$

# %% [markdown]
# ### Question 3

# %%
def slow_sort(A):
    B = []      #O(1) because size of the list is 0
    while A:    #O(1) because len(list) is O(1)
        current_max = A[0]      #O(1) because list slice is constant
        for element in A:       
            if element > current_max:
                current_max = element       #O(n) bc this happens at most n times AKA when A is sorted increasingly
        B.append(current_max)       #O(n) bc we'll need to append n elements
        A.remove(current_max)       #O(n) because 
    return B
    
example_A = [3, 5, 1, 7, 2, 4, 6, 5]
print(slow_sort(example_A))

# %% [markdown]
# ![solution to the question 3](3ex.jpeg)

# %% [markdown]
# ### Question 4
# 

# %% [markdown]
# If n = 1; we return 0.
# If n > 1; we first devide array A of lenght n into 2 subarrays of lenght n/2 (assuming n = $2^k$ for $k \geq 1$).
# 
# Each array of size n/2 we then further separate into n/4 subarrays, getting 4 arrays of size n/4. We keep splitting until we get to n/2 arrays of size 2.
# 
# At this point, we calculate the difference/distance between the two elements in each array, which means we do n/2 constnat calculations -> O(n). We also need to save the information which element is smaller and which bigger, which happens in constant time because we only need to check whether the difference is positive or negative.
# 
# We then merge back the neighbouring arrays of 2, making n/4 arrays of 4. At this step, we need to do $n/4 + 3$ calculations, because we only need to compare the smallest element in the 'left' array to the biggest element in the 'right' array and also the new difference to both previous differences so we can take the biggest one.
# 
# We continue in this fashion until we reach the original array, where we again compare the smallest element of the left array to the smallest element of the right array and then compare the 3 distances to each other (3 comparisons).
# 
# We can derive the following formula: $T(n) \leq 2T{n/2} + 3 \implies T(n) \in O(n)$

# %% [markdown]
# ### Question 5
# 
# #### (a)

# %% [markdown]
# We need to construct an algorithm that successfully installs a max subset of P.
# 
# For n = 1, we need just 1 call to the 'install' function.
# For n > 1, we first need 1 call to check whether the whole set is already a success. If it isn't, we can devide it to get two sets of lenght n/2. For each of them we again check whether they are successfull or not. So we call the function twice. If one of them is successful, we can stop deviding it and only continue D&C on the other half. In case they are both unsuccessful, we keep deviding both. This process in worst case continues until we have (d + 1) subsets in total or reach maximum depth log(n) (when n = k). Before reaching level $\log(d)$ there's no guarantee that even one subset will be successful, but after we surpass level $\log(d)$, there will be at least one subset that will yield successful. This is because in worst case scenario, there will be exactly d defected packages that are each contained in their own subset. After level $\log(d)$, there are always at most d calls to 'instal' function, since if we split one subset, we again get d + 1 subsets in total. We continue until we reach level log(n). At that point we will call 'install' function at most d times at every level. At level log(n), each package will be their own subset, meaning they will all be defected (at most d packages). Summing to the overall complexity: O(d*log(n)).
# 
# Note: whether or not d is a power of 2 does not change this reasoning.

# %% [markdown]
# #### (b)

# %% [markdown]
# The resulting algorithm is almost the same as the one in (a) with the main difference being that at every step before calling the 'install' function, you check whether for every $q \in Q$ there exists $p \in Q$ for subset Q. If the implication in met, you call function 'install'. If it's not, you remove all q's from the subset and add them to a seperate subset. Before you call 'install' on them, you have to do the same for all the other subsets in the level. That way you only need to call once more per level. In worst case scenario, there will be log(n) additional calls, which would mean our function would be of complexity $O(d*log(n) + log(n)) \in O(d*log(n))$.


