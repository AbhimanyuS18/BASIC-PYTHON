i=1
a=int(input('num'))
while i<=5:
	b=a%10
	c=a//10
	k=c**2+b**2
	if k==1 :
		print('happy')
	else:
		if i==5 :
			print("unhappy")
	i+=1
	a=k


	