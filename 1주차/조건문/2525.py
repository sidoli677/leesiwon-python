A, B = map(int, input().split())
C = int(input())

time = (A*60 + B + C) % (24*60)
hour = time // 60
minute = time % 60

print(hour, minute)