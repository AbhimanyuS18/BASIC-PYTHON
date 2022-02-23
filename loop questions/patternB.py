for r in range (1,10):
	for c in range (1,4):
		if c==1 and r in (2,3,4,5,6,7,8,):
			print('#', end='  ')
		elif c==2 and r in (1,5,9):
			print('#', end='  ')
		elif c==3 and r in (2,3,4,6,7,8):
			print('#', end='   ')
		else:
			print(' ',end='   ')
	print( )