def make_trans(A):
    # no_of_rows
    rows = len(A)
    for i in range(rows):
        for j in range(i):
            temp = A[i][j]
            A[i][j] = A[j][i]
            A[j][i] = temp

    return A


B = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(make_trans(B))

