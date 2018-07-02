def main(): #M1, M2 are matrix one and two
    print("Matric Mutiplication")
	print("Enter space after every entery/element")
	firstRowM1 = input("Enter the firt row of 1st 3x3 matrix: ").split()
	secondRowM1 = input("Enter the second row of 1st 3x3 matrix: ").split()
	thirdRowM1 = input("Enter the third row of 1st 3x3 matrix: ").split()

	firstRowM2 = input("Enter the firt row of 2nd 3x3 matrix: ").split()
	secondRowM2 = input("Enter the second row of 2nd 3x3 matrix: ").split()
	thirdRowM2 = input("Enter the third row of 2nd 3x3 matrix: ").split()

	try:
		firstRowM1 = list(map(int, firstRowM1))
		firstRowM2 = list(map(int, firstRowM2))
		secondRowM1 = list(map(int, secondRowM1))
		secondRowM2 = list(map(int, secondRowM2))
		thirdRowM1 = list(map(int, thirdRowM1))
		thirdRowM2 = list(map(int, thirdRowM2))
	except:
		print("Invalid input.") #if input is not valid it will make all the enteries zero
		firstRowM1,firstRowM2,secondRowM1,secondRowM2,thirdRowM1,thirdRowM2 = 0,0,0,0,0,0

	matrix1 = [firstRowM1,secondRowM1,thirdRowM1]
	matrix2 = [firstRowM2,secondRowM2,thirdRowM2]

#taking each row of matrix 1 in one loop then each element in nested loop
	for rowsM1 in matrix1:
		eachRowM1 = ""
		for elementM1 in rowsM1:
			enteryM1 = str(elementM1) + "	"
			eachRowM1 += enteryM1
		print (eachRowM1) #printing each row

	print("") #Just to give space between matrices
	print("") #Just to give space between matrices

	#taking each row of matrix 2 in one loop then each element in nested loop
	for rowsM2 in matrix2:
		eachRowM2 = ""
		for elementM2 in rowsM2:
			enteryM2 = str(elementM2) + "	"
			eachRowM2 += enteryM2
		print (eachRowM2) #printing each row

	print("") #Just to give space between matrices
	print("") #Just to give space between matrices

	for i in range(3):
		productRow = ""
		for j in range(3):
			element = matrix1[i][j] * matrix2[j][i]
			productRow = productRow + str(element) +"	"
		print(productRow)



main()
