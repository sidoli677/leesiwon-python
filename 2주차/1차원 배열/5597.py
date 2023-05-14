submitted = set()
for i in range(28):
    submitted.add(int(input()))

for i in range(1, 31):
    if i not in submitted:
        print(i)