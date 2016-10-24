<?php

echo is_unique( 'abcdefghijklmnopqrstuvwxyz' ) . "\n"; // true
echo is_unique( 'abcdefghijklmnopqrstuvwxyzz' ) . "\n"; // false
echo is_unique( 'aa' ) . "\n"; // false
echo is_unique( 'aba' ) . "\n"; // false
echo is_unique( 'aaaaaaaaaaaaaaaaaaaaaaaaaaa' ) . "\n"; // false
echo is_unique( '  ' ) . "\n"; // false
echo is_unique( ' ' ) . "\n"; // true

function is_unique( $string ) {
	$strlen = strlen( $string ); // calculate once instead of twice

	if ( 128 < $strlen ) { // TODO understand the difference between ascii and unicode
		return 'false';
	}

	$alf = array();
	for ( $i = 0; $i <= $strlen; $i++ ) { // not foreach
		$char = substr( $string, $i, 1 );

		if ( ! $alf[ $char ] ) { // true (already set)
			$alf[ $char ] = 'true';
		} else { // false
			return 'false';
		}
	}

	return 'true';
}
