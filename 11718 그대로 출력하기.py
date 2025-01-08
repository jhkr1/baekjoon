# while True:
#     try:
#         a = input()
#         print(a)
#     except:
#         break
#
#

import sys
s = sys.stdin.readlines()
for i in s:
    print(i.rstrip())