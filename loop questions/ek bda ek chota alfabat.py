a=input('name')
c=len(a)
h=1
b=' '
for i in a:
	if h%2==0:
		b+=i.upper()
	else:
		b+=i
	h+=1
print(b)
	