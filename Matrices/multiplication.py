def matrix_product(A, B):
    # Get the dimensions of matrices A and B
    row_A = len(A)
    cols_A = len(A[0])
    row_B = len(B)
    cols_B = len(B[0])

    # Check if the matrices can be multiplied
    if cols_A != row_B:
        print("The matrices cannot be multiplied")
        return None

    # Initialize the product matrix
    product = []

    # Calculate the product of matrices A and B
    for i in range(row_A):
        row = []
        for j in range(cols_B):
            sum_ele = 0
            for k in range(cols_A):
                sum_ele += A[i][k] * B[k][j]
            row.append(sum_ele)
        product.append(row)

    # Return the product matrix
    return product
