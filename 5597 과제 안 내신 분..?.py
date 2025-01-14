total = 30
total_set = set()
for i in range(1, 31):
    total_set.add(i)

submit = 28
submit_set = set()
for i in range(submit):
    submit_set.add(int(input()))

result = total_set - submit_set

a = result.pop()
b = result.pop()

if (a > b):
    print(b)
    print(a)
else:
    print(a)
    print(b)