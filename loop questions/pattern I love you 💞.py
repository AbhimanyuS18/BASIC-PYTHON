for r in range(1,6):
	for c in range(1,6):
		if c in (1,2,4,5,) and r in (1,5):
			print('@',end='   ')
		elif c==3 and r in (1,2,3,4,5):
			print('@',end='   ')
		else:
			print('   ' ,  end='   ')
	print()
print()
print()
print()
print()
print()
	
	

for r in range(1,8):
	for c in range(1,9):
		if c in (1,8) and r in (2,3,4):
			print('@',end='   ')
		elif c in (2,7) and r in (1,5):
			print('@',end='   ')
		elif c in (3,6) and r in (2,6):
			print('@',end='   ')
		elif c in (4,5) and r in (3,7):
			print('@',end='   ')
		else:
			print('   ',end='   ')
	print()
print()
print()
print()
print()
print()

for r in range(1,8):
	for c in range(1,6):
		if c in (1,5) and r in (1,2,3,4,5,6):
			print('@',end='   ')
		elif c in (2,3,4) and r ==7:
			print('@',end='   ')
		else:
			print('   ', end='   ')
	print()