croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']  
word = input() 
for c in croatian:
    word = word.replace(c, 'a')  
print(len(word))  