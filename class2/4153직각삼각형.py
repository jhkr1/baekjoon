result = []
while True:
    a, b, c = map(int, input().split())
    if(a == 0 and b == 0 and c == 0):
        break
    sides = [a, b, c]
    sides.sort()
    a, b, c = sides[0], sides[1], sides[2]

    if(a**2 + b**2 == c**2):
        result.append('right')
    else:
        result.append('wrong')

for i in result:
    print(i)
    
