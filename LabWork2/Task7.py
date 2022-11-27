x, y, z = map(int, input().split())
countOfTrue = 0
countOfFalse = 0
if x == 1:
    countOfTrue += 1
else:
    countOfFalse += 1
if y == 1:
    countOfTrue += 1
else:
    countOfFalse += 1
if z == 1:
    countOfTrue += 1
else:
    countOfFalse += 1
if countOfTrue>countOfFalse:
    print(1)
else:
    print(0)