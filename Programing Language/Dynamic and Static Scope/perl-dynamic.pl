print "Dynamic Scope for perl \n";

local $x;
sub A{
	print "1th decleration for \$x: $x \n";
}
sub B{
	$x = 10;
	A();
	print "2nd decleration for \$x after calling A: $x \n";
}
sub C{
	local $x = 5;
	B();
	print "3th decleration for \$x after calling A: $x \n";
}
$x = 21;
print "Decleration without using 'local' before calling functions: $x \n";
C();
print "Decleration without using 'local' after calling functions: $x \n";
