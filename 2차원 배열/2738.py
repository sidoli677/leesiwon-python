N, M = map(int, input().split())

A = []
for i in range(N):
    A.append(list(map(int, input().split())))
    
B = []
for i in range(N):
    B.append(list(map(int, input().split())))
    
result = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(A[i][j] + B[i][j])
    result.append(row)
    
for row in result:
    print(' '.join(map(str, row)))