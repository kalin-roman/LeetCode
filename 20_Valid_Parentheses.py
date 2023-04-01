s = '[()][{}]'



def correct(s):

    if len(s) % 2 > 0:
        return False
    
    op_cl = { ')':'(', ']':'[', '}':'{' }
    sta = []

    for x in s:
        if  x in op_cl.values():
            sta.append(x)
        elif len(sta) > 0 and sta[-1] == op_cl[x]:
            sta.pop()
        else:
            return False
    return len(sta) == 0
   

def incorrect(s):
    close = { '[': 0,
            '(':0,
            '{':0
            }

    if len(s) % 2 != 0 or s[0] == ')' or s[0] == ']' or s[0] == '}':
        print('False')
    else:
        for x in s:
            if x == '[' :
                close[x] += 1
            elif x == '{' :
                close[x] += 1
            elif x == '(':
                close[x] += 1
            elif x == ']' :
                close['['] -= 1
            elif x == ')' :
                close['('] -= 1
            elif x == '}' :
                close['{'] -= 1

    return print( 'True' if close['('] ==  close['{'] ==  close['[']  else 'False')

print(correct(s))