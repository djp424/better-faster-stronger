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
def sr(original):
	return original

# test cases
def run_tests():
	print sr('aabcccccaaa') # a2b1c5a3 - 11 vs 8
	print sr('abcdefg') # abcdefg - 7 vs 14
	print sr('abbbbbbbbbbbbbbbbbbcdefg') # a1b18c1d1e1f1g1

run_tests()
# run_timer()
