import sys
import math
import numpy as np

#Exercise 1
print(sys.maxsize > 2**32)

#Exercise 2
    #a)
print(2 * math.pi * 1 )
    #b)
def is_it_even(n):
    return n % 2 == 0
print(is_it_even(5), is_it_even(10))
    #c)
a = 5
b = 10
a, b = b, a
print(a, b)

#Exercise 3
    #a)
def dev_by_5_or_7():
    for i in range(1000, 2001):
        if i % 5 == 0 or i % 7 == 0:
            print(i)
    return
print(dev_by_5_or_7())

    #b)
    
def is_prime(n): #Checking if n is prime
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
        return True
    
def consecutive_primes(n):
    count = 0
    x = 3
    while count < n:
        if is_prime(x) and is_prime(x + 2):
            print((x, x + 2))
            count += 1
        x += 1

print(consecutive_primes(10))
    
#Exercise 4:
    #a)
multiply = lambda x: 2 * x
print(multiply(3), multiply(10))

    #b)
c = [1, 5, 9]
square = lambda x: x ** 2
print([square(x) for x in c])

#Exercise 5:
    #a)
arr1 = np.array([0, 0, 0, 0, 0])
arr2 = np.array([1, 1, 1, 1, 1])
    #b)
def nothing_is_zero(arr):
    for i in np.array(arr):
        if i == 0:
            return False
    return True
    
print(nothing_is_zero([1, 2, 3, 4]))
print(nothing_is_zero([0, 1, 2, 3, 4]))
    
    #c)
def not_everything_is_zero(arr):
    for i in np.array(arr):
        if i != 0:
            return True
    return False
    
print(not_everything_is_zero([1, 2, 3, 4]))

    #d)
def arr_of_range(n, m):
    new_arr = np.array([])
    for i in range(n, m + 1):
        new_arr = np.append(new_arr, i)
    return new_arr

print(arr_of_range(1, 10))

    #e)
def multiplication_of_arr(arr):
    mult = 1
    for i in np.array(arr):
        mult *= i
    return mult

print(multiplication_of_arr([1, 4, 5]), multiplication_of_arr([6, 9, 5]))

    #f)
def create_matrix():
    new_matrix = np.array([])
    for i in range(4):
        new_matrix = np.append(new_matrix, [])
        for j in range(4):
            if i % 2 == 0:
                if j % 2 == 0:
                    new_matrix = np.append(new_matrix, 0)
                else: 
                    new_matrix = np.append(new_matrix, 1)
            else:
                if j % 2 == 0:
                    new_matrix = np.append(new_matrix, 1)
                else: 
                    new_matrix = np.append(new_matrix, 0)
    new_matrix = np.reshape(new_matrix, (4, 4))
    return new_matrix

print(create_matrix())

    #g)

a = np.random.rand(5)
print(a)
print(a.round())
print(np.ceil(a))
print(np.floor(a))

    #h)
x = np.zeros(5)
y = x
z = np.copy(x)
print(x, y, z)
x = np.zeros(10)
print(x, y, z)
# y is still the same as x was when y was defined, z is a copy of the original x and is not affected by the change to x. So none of them change when x changes.