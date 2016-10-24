<?php

$input = '[wibbitz id="b40d336b69af74f6ca51416b177a23858" autoplay="false"]';

if ( '[' === substr( $input, 0, 1 ) && ']' === substr( $input, -1 ) ) {
	echo 'pass';
} else {
	echo 'fail';
}
