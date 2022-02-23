a = 1
b= int(input('Enter any No.: '))
for i in range(1,b+1):
    if i%2 != 0:
        for j in range(b):
            if a<10:
                print(a,end="  ")
            else:
                print(a,end=" ")
            a+=1
    if i%2==0:
        for j in range(a+b-1,a-1,-1):
            if a<10:
                print(j,end="  ")
            else:
                print(j,end=" ")
            a+=1

    print()