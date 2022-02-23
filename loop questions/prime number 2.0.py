b=int(input('lower'))
a=int(input('upper'))
for i in range(b,a):
	sum=0
	for j in range(b,a):
		if i%j==0:
			sum+=1
	if sum==2:
		print(i)