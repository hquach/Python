def add(a,b):
	print "adding %d + %d = %d" % (a,b, a + b)
	return a + b

def subtract(a,b):
	print "subtracting %d - %d = %d" % (a,b, a - b)
	return a - b

def multiply(a,b):
	print "multiply %d * %d = %d" % (a, b, a * b)
	return a * b

def divide(a,b):
	print "divide %d / %d = %d" % (a,b, a / b)
	return a / b

print "here we go:"

age = add(30, 5)
height = subtract(78, 5)
weight = multiply(33,5)
iq = divide(299,3)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Extra:"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "that becomes: ", what, "can you do it by hand"