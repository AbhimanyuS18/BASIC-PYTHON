u=int(input('Enter First Argument: '))
uu=int(input('Enter Second Argument: '))
a=0
b=1
dc=0
l=0
while True:
    c=a+b
    a=b
    b=c
    l+=1
    print(c)
    if c%u==0:
        dc+=1
        if dc==uu:
            x=c
            l+=1
            break
print(u,'table of',uu,'Index',c,'Present')
print('Indexing',l)


