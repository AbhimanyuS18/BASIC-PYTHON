print("Fibnacci series..")
a=int(input("enter a digits"))
if a==1:
	print(1)
elif a==2:
	print(1,1)
elif a<=0:
	print("please enter natural number")
else:
	b=1
	c=1
	print(b)
	print(c)
	i=2
	while a>i:
		d=b+c
		b=c
		c=d
		print(d)
		i+=1
