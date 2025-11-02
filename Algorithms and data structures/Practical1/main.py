# PRACTICAL 1
### Author: Lan Stare, s1169977

###############################################################################################

# Our first step is to open our files and extract the input information
""" def read_dat(file): #This function traverses the given file and produces a new list where each element (a list of integers) represents the first vertex, the second vertex and the type of edge it is with an exception of the first element, which is constructed of |V| and |E|.
    new_list = []
    with open(f"samples-practice/{file}", "r") as dat:
        for line in dat:
            new_list.append(tuple(map(int, line.split())))
    return new_list

file_2 = "2.in"
file_14 = "14.in"
a = read_dat(file_2)
a14 = read_dat(file_14)
a """
##############################################################################################


# Now that we have the inputs neatly in a list of tuples, we will work on our main function. With a double union-find structure (one for the pedestrian graph and one for the bus graph), we will iterate through all the edges and choose to which new spanning tree to add them to (if they don't form a cycle). This is done by Kruskal's algorithm.

def max_roads_to_remove(n, edges):
    # INITIALIZATION
    parent_bus = list(range(n)) #this will keep track of connectivity of the bus_graph
    parent_ped = list(range(n)) #this will do the same for the pedestrian graph
    
    bus_components = n #initiating the number of components which will be useful to check whether the solution is possible. So if a minimal spanning tree doesn't exist for either the busses or the pedestrians, due to deficiency in roads, we return -1. At initiation each vertex is in its own component.
    ped_components = n

        #this operation (Find) of Union-find finds the name of the set that contains x (root)
    def find(parent, x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

        #let's construct union function: it merges two sets into a single set if they are not already connected
    def union(parent, a, b):
        pa, pb = find(parent, a), find(parent, b)
        if pa != pb:
            parent[pa] = pb #if they are in different sets, we connect them
            return True
        return False #if they are already in the same set, we would get a cycle by adding it so we return false

    edges.sort(key=lambda e: 1 if e[2] == 2 else 2)  #we want to make sure to prioritize the "lower-weighted" roads which are the combined roads(identified by the attribute 2)

    kept_edges = 0 #we want to know how many roads we keep while iterating so we don't have to check it at the end, which reduces complexity
    
    # MAIN LOOP
    for u, v, t in edges:
        added = False
        if t == 1 or t == 2: #so if the road is in the bus graph
            if union(parent_bus, u, v): #we try to connect u and v with union-find (like we described in lectures)
                bus_components -= 1 #by connecting two vertices, we reduce the number of components by 1
                added = True
        if t == 0 or t == 2: #so if the road is in the pedestrian graph
            if union(parent_ped, u, v):
                ped_components -= 1
                added = True
        if added:
            kept_edges += 1 #so only if the road contributed to either graphs, we count it :)
        if bus_components == 1 and ped_components == 1:
            break #checking for components can now work also as a stopping criterion which reduces complexity. If the graph is connected, the function stops iterating.
    if bus_components != 1 or ped_components != 1:
        return -1 #this is the optimized way of checking whether the solution is possible
            
    return len(edges) - kept_edges #lastly, we return the difference between the starting and the kept edges (if they exist)

""" max_roads_to_remove(a14[0][0], a14[1:]) """

# Great! The code works fine on our examples. Now all we have to do is make it usable for DomJudge.

import sys

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split())) #we first read all the data and save it as a separate list of integers. This function uses sys library so we can easily split the flattened row into integers due to different formats of .in files
    
    n, m = data[0], data[1] #we then extract |V| and |E| from the list of integers
    edges = [tuple(data[i : i + 3]) for i in range(2, 2 + 3 * m, 3)] #and then we build a list of edge tuples :)
    
    print(max_roads_to_remove(n, edges))
    
