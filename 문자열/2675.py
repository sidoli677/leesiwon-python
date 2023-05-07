t = int(input())
2
​
3
for i in range(t):
4
    r, s = input().split()
5
    p = ''
6
​
7
    for char in s:
8
        p += char * int(r)
9
​
10
    print(p)
