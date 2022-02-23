a=int(input("Enter a number:-"))
j= 1
i=1
while i <= a:
    
    if j <= 10:
        mul = i*j
        print(f"{i} * {j} = {mul}")
        j+=1
    else:
        print("")
        i+=1
        j=1