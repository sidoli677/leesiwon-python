words = [] 
max_len = 0  
for i in range(5):
    word = input().strip() 
    words.append(word)
    if len(word) > max_len:  
        max_len = len(word)

result = ""  
for j in range(max_len): 
    for i in range(5): 
        if j < len(words[i]): 
            result += words[i][j]  
print(result)
