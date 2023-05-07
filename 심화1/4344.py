C = int(input())

for i in range(C):

    scores = list(map(int, input().split()))
    N = scores[0]
    scores = scores[1:]

    
    avg = sum(scores) / N

   
    cnt = 0
    for score in scores:
        if score > avg:
            cnt += 1

    
    ratio = cnt / N * 100

   
    print("{:.3f}%".format(ratio))