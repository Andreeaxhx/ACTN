import string

digs = string.digits + string.ascii_letters

def DecimalToBinary(n):
    return bin(n).replace("0b", "")

def pol(x, message):
    result=0
    for i in range(0, len(message)):
        result=result+(message[i]*(x**(len(message)-i)))
    return result

#-------------------------------------------------------------
def horner(x, coef_list):
    result = 0
    for i in range(0, len(coef_list)):
        result = coef_list[i] + (x * result)
    return result
#-------------------------------------------------------------

def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[(int(x % base))%62])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()
    return digits

def inm_cu_x(coef):
    coef.insert(0,0)

def inm_cu_scalar(c, coef):
    for i in range(len(coef)):
        coef[i]=coef[i]*c
    return coef

def op_gr_1(list1, list2):
    while len(list1)<len(list2):
        list1.insert(len(list1),0)

    while len(list2)<len(list1):
        list2.insert(len(list2),0)

    i=0; final_list=[]
    while i<len(list1):
        final_list.append(list1[i]-list2[i])
        i+=1

    return final_list