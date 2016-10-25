<?php

echo permutation( 'abcdefg', 'gfedcba' ) . "\n"; // true
echo permutation( 'abcdefg', 'gfedcbaa' ) . "\n"; // false
echo permutation( 'a', 'gafaefoaiwehraoiehjfrpawhefrlfedcbaa' ) . "\n"; // false

function permutation( $string1, $string2 ) {
	if ( strlen( $string1 ) !== strlen( $string2 ) ) {
		return 'false';
	}

	if ( string_to_sorted_array( $string1 ) !== string_to_sorted_array( $string2 ) ) {
		return 'false';
	}

	return 'true';
}

function string_to_sorted_array( $string ) {
	$chars = array();
	for ( $i = 0; $i <= $strlen - 1; $i++ ) {
		$chars[ $i ] = substr( $string, $i, 1 );
	}
	return arsort( $chars );
}
