<?php
echo "PHP Code to Show Subprogram Parameters \n";

function positional($x, $y, $z)
{
	return $x * $y + $z;
} 

echo "Positional usage: ";
echo positional(1, 2, 3);
echo "\n";

function keywordBased($x, $y, $z = 5)
{
	return $x + $y * $z;
} 

echo "Keyword-Based usage with 2 variables: ";
echo keywordBased($y = 1, $x = 2);
echo "\n";

echo "Keyword-Based usage with 3 variables: ";
echo keywordBased($y = 1, $z = 3, $x = 2);
echo "\n";

function comb($x, $y, $z = 5)
{
	return $x + $y + $z;
} 

echo "Combination of default, positional and keyword-based usage: ";
echo comb(8, $y = 2);
echo "\n";
?>
