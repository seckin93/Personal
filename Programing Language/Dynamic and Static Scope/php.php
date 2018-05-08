 <?php
echo "Scope by Using PHP";
$x = 45;
$y = 50;

function A(){
	echo "First declaration for x is $GLOBALS[$x] \n";
	echo "First declaration for y is $GLOBALS[$y] \n";
	$x = 10;
	$y = 5;
	echo "Second declaration for x is $x \n";
	echo "Second declaration for y is $y \n";
}

A();
?>
