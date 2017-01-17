# program logic
def sr(s1,s2):
	l1 = len(s1)
	if l1 == len(s2) and l1 > 0:
		combine = s1 + s1
		return isSubstring(combine,s2)
	return false
