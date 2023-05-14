word = input()
alphabet_list = [-1]*26 
for i in range(len(word)):
    if alphabet_list[ord(word[i])-97] == -1:
        alphabet_list[ord(word[i])-97] = i 
for i in range(len(alphabet_list)):
    print(alphabet_list[i], end=' ')