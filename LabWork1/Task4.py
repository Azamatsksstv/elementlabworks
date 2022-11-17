import math

num = int(input())
result = num*45
san = num - 1
added1 = math.ceil(san/2)*5
added2 = math.floor(san/2)*15
ads = added1+added2+num*45

inHours = int(ads/60)
inMinutes = ads - 60*inHours
print(f'{inHours+9} {inMinutes}')