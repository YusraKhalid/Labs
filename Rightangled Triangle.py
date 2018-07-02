
#a,b,c are used as sides of triangle in this function
def isRightTriangle (a,b,c):
	if ((a+b) > c) or ((a+c) > b) or ((b+c) > a):
		print("The three integers are the sides of a right angle triangle.")

	else:
		print("No the three integers are not the sides of a right angle tri angle.")

	return



def main():
	#sides of triangle are sideA, sideB, sideC
	sideA,sideB,sideC = input("Enter the sides of the triangle with space in between: ").split()
	try:
		sideA = int (sideA)
		sideB = int (sideB)
		sideC = int (sideC)
	except:
		print ("Invalid sides are entered.")
		flag = False
	else:
		flag = True
	
	if flag == True:
		isRightTriangle(sideA,sideB,sideC)

	print("Program finish")

main()
