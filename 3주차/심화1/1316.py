n = int(input()) 
result = 0 

for _ in range(n):
    word = input() 
    is_group_word = True  
    
    for i in range(len(word)):
      
        if i > 0 and word[i] != word[i-1]:
           
            if word[i] in word[:i-1]:
                is_group_word = False
                break
    
    
    if is_group_word:
        result += 1

print(result)