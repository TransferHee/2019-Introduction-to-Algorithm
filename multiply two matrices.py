import random
o=int(input('Order of Matrix:'))
lst1=[]
lst2=[]
lst3=[]
lst=[]
print('Generate lst Matrix.')
for a in range(o):
    for b in range(o):
        lst.append(random.randint(1,10))
    lst1.append(lst)
    lst=[]
for a in lst1:
    print(a)
print('Generate 2nd Matrix.')
for a in range(o):
    for b in range(o):
        lst.append(random.randint(1,10))
    lst2.append(lst)
    lst=[]
for a in lst2:
    print(a)
print('Result of Matrix Multiplication.')
r=0
for a in range(o):
    for b in range(o):
        for c in range(o):
            r+=lst1[a][c]*lst2[c][b]
        lst.append(r)
        r=0
    lst3.append(lst)
    lst=[]
for a in lst3:
    print(a)
    
