isbn = input()
num_list = []
weight = 0
for i in range(len(isbn)):
    if isbn[i].isdigit():
        if i % 2 == 1:
            num_list.append(int(isbn[i]) * 3)
        else:
            num_list.append(int(isbn[i]))

total = sum(num_list)

star_idx = isbn.index('*')
star_weight = 3 if star_idx % 2 == 1 else 1

for x in range(10):
    if (total + x * star_weight) % 10 == 0:
        print(x)
        break







