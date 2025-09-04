def solution(sizes):
    w_sizes = []
    h_sizes = []

    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        for j in range(len(sizes[0])):
            if j == 0:
                w_sizes.append(sizes[i][j])
            else:
                h_sizes.append(sizes[i][j])
    return max(w_sizes) * max(h_sizes)