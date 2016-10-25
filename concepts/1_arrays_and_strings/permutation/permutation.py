def permutation( str1, str2 ):
	if len( str1 ) != len( str2 ):
		return 'false'

	if word_array_sort(str1) != word_array_sort(str2):
		return 'false'

	return 'true'

def word_array_sort( str ):
	return list(str).sort()

print permutation( "abcdefg", "gfedcba" ); # true
print permutation( "abcdefg", "gfedcbaa" ); # false
print permutation( "a", "gafaefoaiwehraoiehjfrpawhefrlfedcbaa" ); # false
