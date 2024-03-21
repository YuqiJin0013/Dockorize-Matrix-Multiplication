import numpy as np

# Goal is to implement matrix multiplcation A*B = C 
def matrix_multiply(A, B):
    # matrix A size m*n
    # matrix B size n*p
    m = len(A)
    n = len(A[0])
    p = len(B[0])

    # Check if matrices can be multiplied
    if len(B) != len(A[0]):
        print("Matrices dimensions are not compatible for multiplication")

    # Initialize the result matrix C with all zeros
    C = [[0] * p for _ in range(m)]

    # Implement matrix multiplication
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


# step 2
'''
Test cases
1. the empty matrix -> error
2. mismatch, the matrix size is not corrected for matrix multiply rules -> error
3. input is not a number (characters vs numbers) -> error
4. float * integer will give a float result
5. if super huge number multply each other, it will lose the precision. Put values such as xFFFFFFFF
6. line of matrixs miss some input values -> error
'''
