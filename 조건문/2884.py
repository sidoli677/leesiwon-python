a, b = map(int, input().split())

x = a*60+b
x1 = x-45
b1 = int(x1%60)

if a == 0 and b<45:
    print('23',b1)
elif a==0 and b>=45:
    print('0', b1)
else:
    a1 = int(x1/60)
    print(a1,b1)