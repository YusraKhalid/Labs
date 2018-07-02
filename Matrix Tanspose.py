def main():
	firstRow = input("Enter the firt row of 3x3 matrix: ").split()
	secondRow = input("Enter the second row of 3x3 matrix: ").split()
	thirdRow = input("Enter the third row of 3x3 matrix: ").split()

	matrix = [firstRow,secondRow,thirdRow]
	transposeRow1 = []
	transposeRow2 = []
	transposeRow3 = []
	
#taking each row in one loop then each element in nested loop
	for rows in matrix:
		eachRow = ""
		for element in rows:
			entery = element + "	"
			eachRow += entery
		print (eachRow) #printing each row
#taking transpose of the matrix and making new list for each row of transpose
		transposeRow1.append(rows[0])
		transposeRow2.append(rows[1])
		transposeRow3.append(rows[2])

	transposeMatrix = [transposeRow1,transposeRow2,transposeRow3]

	print("") #Just to give space between matrices
	print("") #Just to give space between matrices

	for transposeRows in transposeMatrix:
		newRow = ""
		for newElement in transposeRows:
			newEntery = newElement + "	"
			newRow += newEntery
		print (newRow)

main()
