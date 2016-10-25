<?php

echo permutation( 'abcdefgzzdddd', 'gfedcbazzdddd' ) . "\n"; // true
echo permutation( 'abcdefg', 'gfedcbaa' ) . "\n"; // false
echo permutation( 'a', 'gafaefoaiwehraoiehjfrpawhefrlfedcbaa' ) . "\n"; // false

function permutation( $string1, $string2 ) {
	$strlen1 = strlen( $string1 );
	if ( $strlen1 !== strlen( $string2 ) ) {
		return 'false';
	}

	$array1 = create_array( $string1, $strlen1 );
	$array2 = create_array( $string2, $strlen1 );

	if ( ! array_compare( $array1, $array2 ) ) {
		return 'false';
	}

	return 'true';
}

function create_array( $string, $strlen ) {
	$chars = array();
	for ( $i = 0; $i <= $strlen - 1; $i++ ) {
		$char = substr( $string, $i, 1 );
		if ( ! isset( $chars[ $char ] ) ) {
			$chars[ $char ] = 1;
		} else {
			$chars[ $char ]++;
		}
	}
	return $chars;
}

function array_compare( $array1, $array2 ) {
	foreach ( $array1 as $key => $value ) {
		if ( $value !== $array2[ $key ] ) {
			return false;
		}
	}
	return true;
}
