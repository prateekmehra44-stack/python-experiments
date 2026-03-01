import numpy as np

n = int(input("Enter size of matrix: "))

print("Enter first matrix:")
A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter second matrix:")
B = []
for i in range(n):
    row = list(map(int, input().split()))
    B.append(row)

A = np.array(A)
B = np.array(B)

C = np.dot(A, B)

print("Result of multiplication:\n", C)