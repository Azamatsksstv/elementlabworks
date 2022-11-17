ladyaX = int(input())
ladyaY = int(input())
anotherFigureX = int(input())
anotherFigureY = int(input())

if ladyaX == anotherFigureX and ladyaY != anotherFigureY:
    print("YES")
elif ladyaX != anotherFigureX and ladyaY == anotherFigureY:
    print("YES")
else:
    print("NO")