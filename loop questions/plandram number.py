i=int(input("enter any numbrr"))
s=0
x=i
while i>0:
    s=(s*10)+i%10
    i=i//10
if x==s:
    print("yes it is Palindrome")
else:
    print("No, it is not ")

