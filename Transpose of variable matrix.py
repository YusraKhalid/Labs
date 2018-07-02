def main():
	rows = input("Enter the number of rows:")
	coloums = input("Enter the number of coloums:")

	try:
		rows = int(rows)
		coloums = int(coloums)
	except:
		print("Invalid input.")
		rows = 0
		coloums = 0
	matrix = [] #taking an empty list for the matrix
	newRow = [] #taking an empty list for the rows of the matrix

	for i in range(rows):
		eachRow = []
		rowOutput = "" #The elelment of each row is stored in it one by one
		for j in range(coloums):
			element = input("Enter the element " + str(i+1) + str(j+1) +" of the matrix: ")
			eachRow.append(element)
			rowOutput += (element + "	") #putting element into the the row
		matrix.append(eachRow) #appending each row into the matrix so it is in the form of nested list.
		newRow.append(rowOutput)
#each new list in the list matrix is a new coloum of the matrix

	for var in newRow:
		print(var)

	print("") #Just to give space between matrices
	print("") #Just to give space between matrices
#Taking rows as coloums and coloums as rows in the loop usung index. First calling the coloum and then the row in reverse manner
	for x in range(coloums):
		trasposeRow = ""
		for y in range(rows):
			transposeColoum = matrix[y]
			entery = transposeColoum[x]
			trasposeRow = trasposeRow + str(entery) + "	"

		print(trasposeRow)


main()
