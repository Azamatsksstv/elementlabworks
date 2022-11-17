a = int(input())
b = int(input())
c = int(input())

if a > b:
    temp = a
    a = b
    b = temp
if a > c:
    temp = a
    a = c
    c = temp
if b > c:
    temp = b
    b = c
    c = temp

print(f'{a} {b} {c}')
