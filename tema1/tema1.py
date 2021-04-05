from Cryptodome.Util.number import inverse
from itertools import combinations
import string
import random
from functions import horner, pol, int2base, DecimalToBinary, inm_cu_x, inm_cu_scalar, op_gr_1

input=123456789123456789
p=base=130043 #17 bits

#input=1234556789
#p=base=31

#input=29
#p=base=11

mess=int2base(input, base)
print(mess)
message=[]

for i in mess:

    if i >= '0' and i<='9':
        message.append(int(i))
    elif i>='a' and i<='z':
        message.append(ord(i)-87)
    elif i>='A' and i<='Z':
        message.append(ord(i)-29)


print("m: ", message)

s=1
k=len(message)+1
n=k+2*s

y=[]
y_prim=[]

message_prim=message.copy()
message_prim.append(0)

for i in range(1, n+1):
    #y.append(pol(i, message)%base)
    y_prim.append(horner(i, message_prim)%base)

y=y_prim
print("y: ", y)
#print("y_prim: ", y_prim)
pozitie=random.randrange(len(y))
z=y.copy()

valoare=random.randrange(0, 100)%base
while valoare==y[pozitie]:
    valoare = random.randrange(0, 100) % base

z[pozitie]=valoare

print("z: ", z)
print("k: ", k)
print("n: ", n)

poz=[]
for i in range(0, len(z)):
    if z[i]==y[i]:
        poz.append(i+1)
print("pozitii fara eroare: ", poz)

comb = combinations(poz, k)

sum=0
B=[]
ok=0
for A in list(comb):
    #print("A: ", A)
    for i in A:
        prod = 1
        for j in A:
            if j!=i:
                prod*=(j*inverse(j-i, base))%base
                #print("prod: ", prod)
        prod=prod%base
        numm=z[i-1]*prod
        sum+=numm%base
    sum=sum%base
    if sum==0 and ok==0:
        B=list(A).copy()
        ok=1
    print("fc:", A, " - ", sum)
    sum=0

coef=[1]
coef1=[1]
res_final=[]

comb = combinations(poz, k)

A=B
#print("A----------------------", A)
res_final_suma=[0]*200
for i in A:
    prod = 1
    coef = [1]
    coef1 = [1]
    res_final = []
    for j in A:
        if j!=i:
            inv=inverse(i-j, base)
            inm_cu_x(coef)
            coef1=inm_cu_scalar(j, coef1)
            res_final = op_gr_1(coef, coef1)
            res_final= [element * inv for element in res_final]

            coef = res_final.copy()
            coef1 = res_final.copy()

    res_final = [(element * z[i-1])%base for element in res_final]
    res_final_suma=[(element1+element2)%base for element1, element2 in zip(res_final_suma, res_final)]
    print("res_final---", res_final)

res_final_suma.reverse()
print(res_final_suma)
mesaj=[]
for i in range(len(res_final_suma)-1):
    mesaj.append(res_final_suma[i])
print("m_decoded:", mesaj)

if mesaj==message:
    print("same as the input")