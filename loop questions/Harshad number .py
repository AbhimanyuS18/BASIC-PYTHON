b=int(input('lower'))
a=int(input('upper'))
for i in range(b,a):
	sum=0
	for j in range(b,a):
		c=i%10
		d=i//10
		sum=c+d
	if i%sum==0:
		print(i)