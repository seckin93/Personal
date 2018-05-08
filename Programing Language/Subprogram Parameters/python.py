print("Python Code to Show Subprogram Parameters");

def positional(x, y, z): #this will show the positional usage
	return x * y + z

def keywordBased(x, y, z = 5): #this will show the keyword usage 
	 return x + y * z

def comb(x, y, z = 5): #this will show the combination of them
	return x + y + z

p = positional(1, 2, 3);
print("First call for positional: %d" % p);

p = keywordBased(y = 1, x = 2);
print("Second call for Keyword-based with 2 variables: %d" % p);

p = keywordBased(y = 1, z= 3, x = 2);
print("Third call for Keyword-based with 3 variables: %d" % p);

p = comb(8, y = 6);
print("Fourth call for combination of default, positional and keyword-based: %d" % p);

#Here is the example of passıng parameters and https://stackoverflow.com/questions/1419046/python-normal-arguments-vs-keyword-arguments/1419159#1419159 is used to study and write testing program [1] (reference in report)

def exampleForPandK(*positional, **keyword): #Positional and Keyword-Based example
	print ("Positionals: " , positional)
	print ("Keywords: ", keyword)

exampleForPandK();
exampleForPandK(1,2,3,4)
exampleForPandK(1, 2, z = 3, t = 4)
exampleForPandK(x = 1, y = 2, z = 3, t = 4)

