<?php

echo permutation( 'abcdefgzzdddd', 'gfedcbazzdddd' ) . "\n"; // true
echo permutation( 'abcdefg', 'gfedcbaa' ) . "\n"; // false
echo permutation( 'a', 'gafaefoaiwehraoiehjfrpawhefrlfedcbaa' ) . "\n"; // false

function permutation( $string1, $string2 ) {
	if ( strlen( $string1 ) !== strlen( $string2 ) ) {
		return 'false';
	}

	$array1 = str_split( $string1 );
	$array2 = str_split( $string2 );
	$chars  = array(); // TODO ASCII (128)

	foreach ( $array1 as $c ) { // count
		$chars[ $c ]++;
	}

	foreach ( $array2 as $c ) { // reverse
		$chars[ $c ]--;
		if ( $chars[ $c ] < 0 ) {
			return 'false';
		}
	}

	return 'true';
}
