import sys

n,m = map(int, sys.stdin.readline().split())
site_password_dict={}

for i in range(n):
    site, password = map(str, sys.stdin.readline().split())
    site_password_dict[site] = password


need_password_site = []

for i in range(m):
    need_password_site.append(sys.stdin.readline().strip())


for i in need_password_site:
    print(site_password_dict[i])