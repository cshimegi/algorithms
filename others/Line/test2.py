def fibonacci(a1, a2, n):
    for _ in range(n-2):
        a1, a2 = a2, a1+a2

    return a2

print(fibonacci(1,2,3))
print(fibonacci(3,2,10)) # 1 2 3 5 8