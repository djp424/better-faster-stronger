<?php

echo url( 'David Parsons', 13 ) . "\n"; // David%20Parsons
echo url( 'The Great and Super Awesome', 27 ) . "\n"; // The%20Great%20and%20Super%20Awesome
echo url( 'WhyNotTestThis', 14 ) . "\n"; // WhyNotTestThis

function url( $str, $len ) {
	return str_replace( ' ', '%20', $str );
}
