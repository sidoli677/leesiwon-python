given = [int(x) for x in input().split()]
correct = [1, 1, 2, 2, 2, 8]
diff = [correct[i] - given[i] for i in range(6)]
print(*diff)