def url( str, len ):
	return str.replace( ' ', '%20' )

print url( 'David Parsons', 13 ) # David%20Parsons
print url( 'The Great and Super Awesome', 27 ) # The%20Great%20and%20Super%20Awesome
print url( 'WhyNotTestThis', 14 ) # WhyNotTestThis
