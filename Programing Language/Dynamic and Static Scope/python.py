print("Python code to show scoping rule");

x = 15;
def f1():
	x = 3;
	print("First print in f1 %d" % x);
	x = 10;
	print("Second print in f1 %d" % x);
	def f2():
		global x;
		print("First print in f2 %d" % x);
		x = 1;		
		print("Second print in f2 %d" % x);
		def f3():
			x = 0;
			print("First print in f3 %d" % x);
			def f4():
				global x;
				print("First print in f4 %d" % x);
				x = 315;
				print("First print in f4 %d" % x);
			
			print("Before calling f4 %d" % x);
			f4();
			print("After calling f4 %d" % x);
	
		print("Before calling f3 %d" % x);
		f3();
		print("After calling f3 %d" % x);

	print("Before calling f2 %d" % x);	
	f2();
	print("After calling f2 %d" % x);		

print("Before everything %d" % x);
f1();	
print("After everything %d" % x);	
