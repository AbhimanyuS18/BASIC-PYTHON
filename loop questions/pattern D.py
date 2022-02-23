for r in range (1,7):
	for c in range (1,5):
		if c==1 and r in (2,3,4,5):
			print('#', end='  ')
		elif c==2 and r in (1,6):
			print('#', end='  ')
		elif c==3 and r in (1,2,3,4,5,6,):
			print('#',end='  ')
		else:
			print(' ',end='   ')
	print( )