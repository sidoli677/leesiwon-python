N, X = map(int, input().split())
A = list(map(int, input().split()))

result = []
for i in range(N):
    if A[i] < X:
        result.append(str(A[i]))

print(" ".join(result))