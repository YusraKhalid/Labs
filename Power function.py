def power (a,b,c):	
	variable = (a ** b) % c
	return variable

def func ():
	varOne = float (input( " a = "))
	varTwo = float (input( " b = "))
	varThree = float (input( " c = "))
	print ( power (varOne,varTwo,varThree))

func ()
