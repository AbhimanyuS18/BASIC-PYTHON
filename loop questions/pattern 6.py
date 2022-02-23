for i in range (1,4):
	for j in range(1,6):
		if j<=i+2 and j>=4-i:
			print('#',end=' ')
		else:
			print('  ', end=' ')
	print()