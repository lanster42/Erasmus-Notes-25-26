def recursion(n):
    if n <= 1:
        print("Recursion ends here")
        return 1
    else:
        return n * recursion(n - 1)

print(recursion(8))