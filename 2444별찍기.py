temp = int(input()) # 5
x = temp-1 # 4
for i in range(x): # i = 0 1 2 3 4  
    print(' ' * (x - (i+1)), '*' * (2*(i+1)- 1)) 

print('*' * (temp * 2 - 1)) # 가운데 

for j in range(x): # i = 0 1 2 3 4  
    print(' ' * j, '*' * (2*x - (2*j+1))) # 8 - 1, 8 - 3



