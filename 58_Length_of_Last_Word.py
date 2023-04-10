s = "luffy is still joyboy "
word = ''

for i,x in enumerate(s):
    if i == len(s)-1 and x == ' ':
        break
    elif x != ' ':
        word += x
    else:
        word = ''

print(len(word))