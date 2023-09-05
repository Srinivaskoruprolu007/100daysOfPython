def make_trans(A):
    # no_of_rows
    rows = len(A)
    cols = len(A[0])
    trans = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            trans[j][i] = A[i][j]
    return trans


B = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(make_trans(B))

