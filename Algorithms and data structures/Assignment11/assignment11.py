# %% [markdown]
# # Assignment 11
# 
# **Author:** Lan Stare
# 
# **Date:** 28. 11. 2025

# %% [markdown]
# 
# ### Question 1
# 

# %% [markdown]
# __Remark:__ I sincerely apologize to the person reading and judging my handwritten notes, I tried to make them better this week.

# %% [markdown]
# ![solution to the question 1](1ex.jpeg)

# %% [markdown]
# When we run the algorithm for i = 5, nothing changes so our shortest distances are stable.

# %% [markdown]
# ### Question 2
# 

# %% [markdown]
# Since we have the starting and ending vertex given, we'll modify the Bellman-Ford algorithm, since it's faster for that particular case.
# 
# In the lecture we mentioned that we can optimize the algorithm to be of complexity $O(|V||E|)$ by iterating through edges for each $i \in {1, \ldots, n}$. Since our shortest path between any two edges has at most $k$-edges, our algorithm will stabilize after at most $k$-iterations. So if we know that our graph doesn't have a negative cycle, we don't need to change the algorithm to have complexity $O(k |E|)$ otherwise we add a stopping criterion that terminates after the $k$-th iteration.

# %% [markdown]
# ### Question 3

# %% [markdown]
# ![solution to the question 3](3ex.jpeg)

# %% [markdown]
# ### Question 4
# 

# %% [markdown]
# If there is a negative cycle present in our graph, we can easily detect it with Floyd-Warshall's algorithm. If there is a negative cycle, there exists a vertex i, such that $D^{n}_{(i, i)} < 0$ for n vertices. This holds because in the n-th step we are free to use any vertex to get to any other vertex so if for example vertex u is an element of the negative cycle we can traverse the cycle to get back to u, which gives a negative weight (by definition of a negative cycle).
# 
# 
# A little further thinking:  we can even be sure that if in $D^{n - 1}$ we have no vertex i such that $D^{n - 1}_{(i, i)} < 0$ holds, we can only check n-th element in the next step since if a nex cycle showed itself it definitely included vertex n.

# %% [markdown]
# ### Question 5
# 

# %% [markdown]
# EXPLANATION:
# 
# If I understand the task correctly than we need to build a matrix that keeps track of the current predecessors (where we're only using vertices 1 to k at step k).
# 
# To do this we just need to also remember which predecessor changed the entry in the matrix. My implementation will not keep 2 seperate matrices but will include both informations about shortest path and the predecessor in space the [i][j] of each matrix.

# %%
#implementation:
import numpy as np

def print_paths(matrix):
    """ prints the shortest paths between all pairs of vertices (one path per line) """
    n = len(matrix)
    D = []
    
    for k in range(n + 1):     #|V| x |V| matrix (assuming its a list of rows)
        D[k] = []
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if k == 0:      #our base case
                    D[k][i][j] = [[matrix[i][j], i] if matrix[i][j] != np.infty else [np.infty, 0]]      #at first we need to change the adjacency matrix to include the initial weight value in the first spot and the predecessor (which is i when i and j are connected and 0 otherwise) in the second spot
                new_possible_w = D[k - 1][i][k][0] + D[k - 1][k][j][0]
                old_possible_w = D[k - 1][i][j][0]
                if new_possible_w < old_possible_w:
                    D[k][i][j] = [new_possible_w, D[k - 1][k][j][1]]    #we update the new predecessor of j as the predecessor of j when we look at path from k to j (at step k - 1)
                else:
                    D[k][i][j] = [D[k - 1][k][j]]       #we can just keep the old duo
            
    #now we need to print first all the rows (while checking that there is a path):
    for i in range(1, n + 1):      #we only want to know what it is in the last matrix
        list_of_vertices_for_i = []        #we initiate the path starting from i
        for j in range(1, n + 1):         #for every column (vertex) we need to print the shortest path
            predecessor = D[n][i][j][1]
            if predecessor == 0:
                raise ValueError("There are no paths from {i} to {j} :3.")  #error message in case no such path exists
            list_of_vertices_for_i.append(predecessor)      #we add the predecessor of j to the list
            if predecessor == j:
                list_of_vertices_for_i.append(i)    #at last we append the first element so that it'll be the first element after reversing:
                list_of_vertices_for_i.reverse()    #since we were building it backwards it needs to be reversed
                print(list_of_vertices_for_i)
                print("\n")
                continue
            else:
                list_of_vertices_for_i.append(D[n][i][predecessor])     #the recursive step where we take and add the predecessor(predecessor(j)) to the list



