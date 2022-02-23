a=eval(input('lower'))
b=eval(input('upper'))
for num in range(a,b+1):
	sum=0
	for i in range(1,num):
		if num%i==0:
			sum+=i
	if sum==num:
		print(num)

	
		