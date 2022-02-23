i=1
a=v=int(input('num3: '))
s=0
while i<=3:
	c=a%10
	s+=(c**3)
	a=a//10
	i+=1
	print()
if s==v:
		print('armstrong')
else:
		print('not armstrong')
	


	