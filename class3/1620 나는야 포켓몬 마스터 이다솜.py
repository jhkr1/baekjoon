import sys
n, m = map(int, sys.stdin.readline().split())
pokemon_dict = {}
problem_list = []


for i in range(n):
    pokemon = sys.stdin.readline().strip()
    pokemon_dict[i+1] = pokemon

reverse_pokemon_dict = {v:k for k, v in pokemon_dict.items()}

for i in range(m):
    problem_list.append(sys.stdin.readline().strip())

for i in problem_list:
    if i.isdigit():
        print(pokemon_dict[int(i)])
    else:
        print(reverse_pokemon_dict[i])






