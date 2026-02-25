# Strassen Matrix Multiplication using user input

def strassen(A, B):

    p1 = (A[0][0] + A[1][1]) * (B[0][0] + B[1][1])
    p2 = (A[1][0] + A[1][1]) * B[0][0]
    p3 = A[0][0] * (B[0][1] - B[1][1])
    p4 = A[1][1] * (B[1][0] - B[0][0])
    p5 = (A[0][0] + A[0][1]) * B[1][1]
    p6 = (A[1][0] - A[0][0]) * (B[0][0] + B[0][1])
    p7 = (A[0][1] - A[1][1]) * (B[1][0] + B[1][1])

    C = [[0, 0], [0, 0]]

    C[0][0] = p1 + p4 - p5 + p7
    C[0][1] = p3 + p5
    C[1][0] = p2 + p4
    C[1][1] = p1 + p3 - p2 + p6

    return C


# ---- User Input ----

A = []
B = []

print("Enter elements of Matrix A (2x2):")
for i in range(2):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter elements of Matrix B (2x2):")
for i in range(2):
    row = list(map(int, input().split()))
    B.append(row)

result = strassen(A, B)

print("Result Matrix:")
for row in result:
    print(row)


# Time complexity = O(n^2.81)
