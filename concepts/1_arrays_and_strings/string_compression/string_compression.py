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
def base(original):
	if original == '': # empty case
		return ''

	# take care of first char before hand
	new = original[0]
	old_letter = original[0]

	# calculate
	repeat = 'false'
	repeat_count = 0
	for current_letter in original:
		if old_letter != current_letter: # same
			new += str(repeat_count) # add number after switch
			new += current_letter # add first char of new after switch
			repeat_count = 0 # restart count

		repeat_count += 1
		old_letter = current_letter # setup for next loop

	new += str(repeat_count) # last number

	if len(new) < len(original):
		return new

	return original

# test cases
def run_tests():
	print base('aabcccccaaa') # a2b1c5a3 - 11 vs 8
	print base('abcdefg') # abcdefg - 7 vs 14
	print base('abbbbbbbbbbbbbbbbbbcdefg') # a1b18c1d1e1f1g1

# run_tests()
run_timer()
