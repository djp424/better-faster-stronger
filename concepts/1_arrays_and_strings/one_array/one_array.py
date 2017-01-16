import time
import os.path

# timer for speed testing of program logic
def run_timer():
	tests = 30
	start_time = time.time() # start
	for i in xrange(tests):
		run_tests()
	end_time = time.time()
	total_time = (end_time - start_time) / tests # end
	print("Runtime: %.10f seconds" % total_time)
	# save results
	file_name = "speed.csv"
	if os.path.isfile(file_name) is False:
		with open(file_name, "a") as results:
			results.write("time,tests\n")
	with open(file_name, "a") as results:
		results.write("%.10f" % total_time)
		results.write(",%s\n" % tests)

# program logic
def base(old,new):
	if old == new:
		return 'true'

	found = 'false'
	len1 = len(old)
	len2 = len(new)
	diff = len1 - len2
	first = 'false'
	second = 'false'

	# check lengths
	if abs( diff ) > 1: # break out early if leg diff is 2 or more
		return 'false'
	elif len1 > len2: # first string is longer
		first = 'true'
	elif len1 < len2: # second string is longer
		second = 'true'

	i1 = 0
	i2 = 0
	while i1 < len1 and i2 < len2:
		if old[i1] != new[i2]: # could be spacing or char difference
			if found == 'true':
				return 'false'
			found = 'true'

			# move longer string up by 1
			if first == 'true': # first is longer
				i1 += 1
				pass
			elif second == 'true': # second is longer
				i2 += 1
				pass

		i1 += 1
		i2 += 1

	return 'true'

# test cases
def run_tests():
	print base('pale','pale') # true - 0 edits away
	print base('pale','pal') # true - add one
	print base('pales','pale') # true - remove one
	print base('pale','bale') # true - change one
	print base('pale','bake') # false - two steps away
	print base('bbake','bake') # true - remove one

# run_tests()
run_timer()
