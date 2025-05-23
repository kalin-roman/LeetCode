digits = [9,0,10,2]

def plusOne(digits):
    return list(map(int,str(int(''.join(str(x) for x in digits))+1)))

def plusOne2(digits):
    return map(int,str(int(''.join(map(str, digits)))+1))

print(plusOne2(digits))