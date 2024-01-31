#This code genrates L and U and then substitutes to get roots
n = int(input("Enter n"))

mat=[]
for i in range(n):
    mat.append([0.0] * (n))

B = list(map(float,input("Enter B").split()))



for j in range(n):
    row = input(f"Enter the {j + 1} th row of coefficient Matrix")
    row_arr = row.split(" ")
    for l in range(n):
        mat[j][l] = float(row_arr[l])
# 
L = []
for i in range(n):
    L.append([0.0] * (n))
for i in range(n):
    L[i][i] = 1

U = []
for i in range(n):
    U.append([0.0] * (n))

def forwardElimination(mat,L,U):
    for j in range(n):
        for k in range(j+1,n) :
            f_kj = mat[k][j]/mat[j][j]
            L[k][j] = f_kj
            for l in range(n):
                mat[k][l]=mat[k][l] - (f_kj)*mat[j][l]
    for q in range(n):
        for p in range(n):
            U[q][p] = mat[q][p]

forwardElimination(mat,L,U)
print('\n')
print("L is : ")
for m in range(n):
    print(L[m])

def forwardSubstituation(L,B):
    D = [0]*n
    p=n-2
    D[n-1] = B[n-1]/L[n-1][n-1]
    p = 0
    while p<n:
        D[p] = (B[p] - sum((mul(L[p],D))))/(L[p][p])
        p+=1
    return D

def mul(A,B):
    P = []
    for i in range(len(A)):
        P.append(A[i]*B[i])
    return P

def backSubstitution(A,B) : 
    roots = [0]*n
    roots[n-1]=B[n-1]/A[n-1][n-1]
    p=n-2
    while p>-1:
        roots[p] = (B[p] - sum((mul(A[p],roots))))/(A[p][p])
        p-=1
    return roots

print('\n')
print("U is : ")
for m in range(n):
    print(U[m])

D = forwardSubstituation(L,B)
print("\n")
roots = backSubstitution(U,D)
print("Roots are : ")
print(roots)