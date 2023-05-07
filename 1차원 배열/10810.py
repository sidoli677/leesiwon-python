n, m = map(int, input().split())

baskets = [0] * n

for i in range(m):
    start, end, number = map(int, input().split())
    for j in range(start-1, end):
        baskets[j] = number

for basket in baskets:
    print(basket, end=' ')