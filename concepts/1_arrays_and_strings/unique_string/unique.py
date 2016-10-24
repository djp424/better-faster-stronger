def is_unique( str ):
	strlen = len( str );

	if strlen > 128:
		return;

	checker = []

	for letter in str:
		checker.append( letter );

	if len(checker) > len(set(checker)):
		return 'false'

	return 'true'

print is_unique("abcdefghijklmnopqrstuvwxyz"); # true
print is_unique("abcdefghijklmnopqrstuvwxyzz"); # false
print is_unique("aa"); # false
print is_unique("aba"); # false
print is_unique("aaaaaaaaaaaaaaaaaaaaaaaaaaa"); # false
print is_unique("  "); # false
print is_unique(" "); # true
