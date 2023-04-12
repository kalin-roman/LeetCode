s = "  luffy is stilljoyboy"


def f1(s):
    word = ''
    for i,x in enumerate(s):
        if i == len(s)-1 and x == ' ' :
            break
        elif x != ' ':
            word += x
        elif s[i+1] != ' ':
            word = ''

def f2(s):
    return len(set(s.split()).pop())

# def f3(s):
#     return 
# print(f3(s))

a = f1
x = lambda s : len(s.split()[-1])
print(x(s))

