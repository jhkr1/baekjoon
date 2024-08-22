def seq_search(n, S, x):
	location = 1
	while (location <= n and S[location] != x):
		location += 1
	if(location > n):
		location = 0
	return location

S = [0, 10, 7, 11, 5, 13, 8] # 0번째 인덱스는 사용X
x = 5
location = seq_search(len(S) - 1, S, x)
print('location =', location)