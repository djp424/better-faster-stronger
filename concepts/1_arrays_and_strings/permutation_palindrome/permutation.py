def permutation_palindrome( string ):
	string = string.lower()
	length = len( string );

	if length == 1: # only one item
		return 'true'
	elif length == 2: # only 2 items (must be same char)
		wordArray = list( string )
		if wordArray[0] == wordArray[1]:
			return 'true'
		else:
			return 'false'
	elif length % 2 == 0: # even
		oneOdd = 'true'
	else: # odd
		oneOdd = 'false'

	wordArray = list( string )
	chars = []
	oddCount = 0

	for value in wordArray:
		if value != ' ':
			if string.count(value) % 2 == 1: # odd
				oddCount = oddCount + 1

	if oddCount == 1 and oneOdd == 'true': # if count is odd and we want odd
		return 'true'
	else:
		return 'false'

print permutation_palindrome( "a" ); # true
print permutation_palindrome( "aa" ); # true
print permutation_palindrome( "ab" ); # false
print permutation_palindrome( "ba" ); # false
print permutation_palindrome( "Tact Coa" ); # true: "taco cat", "atco cta"...
print permutation_palindrome( "Tact Coab" ); # false
