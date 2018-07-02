def main():
    numberOfRows = input("Enter the number of rows: ")
    numberOfColoums = input("Enter the number of coloums: ")
    try:
        numberOfColoums = int(numberOfColoums)
        numberOfRows = int(numberOfRows)

    except:
        print("Invalid input.")
        numberOfRows= 0

    matrix = []
    i = 0

    while i < numberOfRows :
        j = 0
        row1 = []
        while j < numberOfColoums:
            element1 = input("Enter the element of matrix: ")
            row1.append(element1)
            j +=1
        matrix.append(row1)
        i +=1

    i = 0
    while i < numberOfRows:
        j = 0
        string = ''
        while j < numberOfColoums:
            string += ((matrix[i][j]) +"    ")
            j +=1
        print(string)
        i+=1

    print("\n")
    i = 0
    while i < numberOfRows:
        j = 0
        string = ''
        while j < numberOfColoums:
            string += ((matrix[j][i]) +"    ")
            j +=1
        print(string)
        i+=1

main()

