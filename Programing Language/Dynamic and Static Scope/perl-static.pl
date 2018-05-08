 #!/usr/bin/env perl

  use v5.10.0;
  use warnings;
  use strict;

say "Static Scope for perl";

my $x;
sub A{
	print "1th decleration for \$x: $x \n";
}
sub B{
	my $x = 10;
	A();
	print "2nd decleration for \$x after calling A: $x \n";
}
sub C{
	$x = 5;
	B();
	print "3th decleration for \$x after calling A: $x \n";
}
$x = 21;
print "Decleration without using 'my' before calling functions: $x \n";
C();
print "Decleration without using 'my' after calling functions: $x \n";
