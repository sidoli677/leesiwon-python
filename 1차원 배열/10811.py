n, m = map(int, input().split())

baskets = [i for i in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    baskets[i:j+1] = reversed(baskets[i:j+1])

for i in range(1, n+1):
    print(baskets[i], end=' ')