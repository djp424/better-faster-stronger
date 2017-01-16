# program logic (not complete)
for i = 0 to n:
	temp = top[i]
	top[i] = left[i]
	left[i] = bottom[i]
	bottom[i] = right[i]
	right[i] = temp
