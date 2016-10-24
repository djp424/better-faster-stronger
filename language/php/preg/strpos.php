<?php

$input = '[wibbitz id="b40d336b69af74f6ca51416b177a23858" autoplay="false"]';

if ( 0 === strpos( $input, '[' ) && strlen( $input ) - 1 === strpos( $input, ']' ) ) {
	echo 'pass';
} else {
	echo 'fail';
}
