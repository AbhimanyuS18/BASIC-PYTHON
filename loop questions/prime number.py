i=1
a=int(input('num'))
sum=0
while i<=10:
	if a%i==0:
		sum+=1
	i+=1
if sum==2:
	print('prime')
else:
	print('not prime')
	