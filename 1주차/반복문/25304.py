X = int(input())
2
N = int(input()) 
3
i = 1
4
total = 0
5
​
6
while i <= N:
7
    a, b = map(int, input().split())
8
    result = (a * b)
9
    total += result
10
    i += 1
11
if total == X :
12
    print("Yes")
13
else:
14
    print("No")
