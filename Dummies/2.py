try:
	Value = int(input("Number between 1 and 10: "))
except ValueError:
	print "You must type a number between 1 and 10"
else:
	if (Value > 0) and (Value < 10):
		print "you typed: ", Value
	else:
		print "Incorrect!"