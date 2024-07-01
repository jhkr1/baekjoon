rows=5
words = []

for i in range(rows):
    words.append(list(map(str, input())))


cols_len = []
for col in words:
    cols_len.append(len(col))

cols = max(cols_len)


result = []
for i in range(cols):
    for j in range(rows):
        try:
            result.append(words[j][i]) # 
        except:
            continue

for i in result:
    print(i, end='')
