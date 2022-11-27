def power(a: float, n: float):
    return a**n


a, n = map(float, input().split())
print(power(a, n))
