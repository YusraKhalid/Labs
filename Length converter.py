def centimeter (inch):
	centi = 2.54 * inch
	return (centi)

def feet (inches):
	feets = inches/12.0
	return (feets)

def func ():
	height = float (input ("Enter height in inches :  "))
	print ( centimeter (height), "cm")
	print (feet (height), "ft")

func ()

