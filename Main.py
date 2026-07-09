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

def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0]*B[0][0]]]
    A11,A12,A21,A22 = split(A)
    B11,B12,B21,B22 = split(B)
    P1 = strassen(A11, sub(B12,B22))
    P2 = strassen(add(A11,A12), B22)
    P3 = strassen(add(A21,A22), B11)
    P4 = strassen(A22, sub(B21,B11))
    P5 = strassen(add(A11,A22), add(B11,B22))
    P6 = strassen(sub(A12,A22), add(B21,B22))
    P7 = strassen(sub(A11,A21), add(B11,B12))
    C11 = add(sub(add(P5,P4),P2),P6)
    C12 = add(P1,P2)
    C21 = add(P3,P4)
    C22 = sub(sub(add(P5,P1),P3),P7)
    return merge(C11,C12,C21,C22)

sizes = [2,4,8,16,32,64,128]
t1,t2,t3 = [],[],[]

for n in sizes:
    A = [[random.randint(1,5) for _ in range(n)] for _ in range(n)]
    B = [[random.randint(1,5) for _ in range(n)] for _ in range(n)]

    s = time.time()
    standard_multiply(A,B)
    t1.append(time.time()-s)

    s = time.time()
    dc_multiply(A,B)
    t2.append(time.time()-s)

    s = time.time()
    strassen(A,B)
    t3.append(time.time()-s)

plt.figure(figsize=(8, 5))
plt.plot(sizes, t1, label='Standard', marker='o')
plt.plot(sizes, t2, label='Divide & Conquer', marker='s')
plt.plot(sizes, t3, label='Strassen', marker='^')
plt.xlabel('Matrix Size (n)')
plt.ylabel('Time (seconds)')
plt.legend()
plt.grid(True)
plt.show()