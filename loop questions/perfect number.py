i=1
sum=0
a=int(input('num  '))
while i<a:
	if a%i==0:
		sum+=i
	i+=1
if sum==a:
		print('perfect')
else:
	print('not perfect')
	