import sys
li = []
for i in range(int(sys.stdin.readline())):
    text = sys.stdin.readline().strip() 
    li.append(text[0]+text[-1])  
for i in range(len(li)):
    print(li[i])