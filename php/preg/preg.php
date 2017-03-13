<?php

$input = '[wibbitz id="b40d336b69af74f6ca51416b177a23858" autoplay="false"]';

if ( preg_match( '\[[a-z]+.*\]', $input ) ) {
	echo 'pass';
} else {
	echo 'fail';
}
