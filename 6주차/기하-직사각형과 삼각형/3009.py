
x_nums = []
2
y_nums = []
3
for _ in range(3):
4
    x, y = map(int, input().split())
5
    x_nums.append(x)
6
    y_nums.append(y)
7
​
8
for i in range(3):
9
    if x_nums.count(x_nums[i]) == 1:
10
        x4 = x_nums[i]
11
    if y_nums.count(y_nums[i]) == 1:
12
        y4 = y_nums[i]
13
print(x4, y4)
