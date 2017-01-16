# Description
Output a compressed version of the string by replacing repeating characters with numbers. Return the original string if the compressed version is not shorter than the original. Assume that there are only uppercase and lowercase letters.

# Test Cases
aabcccccaaa (a2b1c5a3) - 11 vs 8
abcdefg (abcdefg) - 7 vs 14

# Thought Process
1. uppercase and lowercase are different
2. build string
3. return shorter version

# Thought Process (after seeing output)
1. Check for the last case in loop (number not showing)

# To Do (after seeing output)
1. Use StringBuilder (do you need that in python)
2. Check in advance to make sure we don't build string that is not needed. Run a function at the beginning to count the repeats.
