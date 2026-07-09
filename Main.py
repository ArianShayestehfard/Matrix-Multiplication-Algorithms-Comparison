import time
import random
import matplotlib.pyplot as plt

def standard_multiply(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def add(A, B):
    n = len(A)
    return [[A[i][j]+B[i][j] for j in range(n)] for i in range(n)]

def sub(A, B):
    n = len(A)
    return [[A[i][j]-B[i][j] for j in range(n)] for i in range(n)]

def split(A):
    n = len(A)
    m = n//2
    A11 = [[A[i][j] for j in range(m)] for i in range(m)]
    A12 = [[A[i][j] for j in range(m,n)] for i in range(m)]
    A21 = [[A[i][j] for j in range(m)] for i in range(m,n)]
    A22 = [[A[i][j] for j in range(m,n)] for i in range(m,n)]
    return A11,A12,A21,A22

def merge(C11,C12,C21,C22):
    m = len(C11)
    C = [[0]*(m*2) for _ in range(m*2)]
    for i in range(m):
        for j in range(m):
            C[i][j] = C11[i][j]
            C[i][j+m] = C12[i][j]
            C[i+m][j] = C21[i][j]
            C[i+m][j+m] = C22[i][j]
    return C

def dc_multiply(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0]*B[0][0]]]
    A11,A12,A21,A22 = split(A)
    B11,B12,B21,B22 = split(B)
    C11 = add(dc_multiply(A11,B11), dc_multiply(A12,B21))
    C12 = add(dc_multiply(A11,B12), dc_multiply(A12,B22))
    C21 = add(dc_multiply(A21,B11), dc_multiply(A22,B21))
    C22 = add(dc_multiply(A21,B12), dc_multiply(A22,B22))
    return merge(C11,C12,C21,C22)

