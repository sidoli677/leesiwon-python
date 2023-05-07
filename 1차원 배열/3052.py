nums = []
for i in range(10):
    nums.append(int(input()))

remainders = [n % 42 for n in nums]
unique_remainders = set(remainders)
print(len(unique_remainders))