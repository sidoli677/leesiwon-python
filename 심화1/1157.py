word = input().upper()  
word_dict = {} 

for w in word:
    if w in word_dict:
        word_dict[w] += 1
    else:
        word_dict[w] = 1

max_count = max(word_dict.values())  
max_alpha = [] 

for key, value in word_dict.items():
    if value == max_count:
        max_alpha.append(key)

if len(max_alpha) == 1:
    print(max_alpha[0])
else:
    print('?')