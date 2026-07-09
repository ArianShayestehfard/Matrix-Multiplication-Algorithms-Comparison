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
