for r in range (1,9):
	for c in range (1,6):
		if c==1 and r in (2,3,4,5):
			print('#', end='  ')
		elif c in(2,3) and r in (1,6):
			print('#', end='  ')
		elif c==4 and r in (2,5,6,7,8):
			print('#',end='  ')
		else:
			print('  ',end='  ')
	print()
