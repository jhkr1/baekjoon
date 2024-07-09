music = input().split()
music_list_A = ['1', '2', '3', '4', '5', '6', '7', '8']
music_list_D = ['8', '7', '6', '5', '4', '3', '2', '1']

if (music == music_list_A):
    print('ascending')
elif (music == music_list_D):
    print('descending')
else:
    print('mixed')

