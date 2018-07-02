def main():
    matrix1and2 = []
    count = 0

    countMatrix1 = 0
    while count <2:
        matrix = []

        while countMatrix1 < 3:
            countColoum1 = -1
            row1 = []
            while countColoum1 < 2:
                element1 = input("Enter the element of matrix: ")
                try:
                    element1 = float(element1)
                    countColoum1 +=1
                except:
                    print("Invalid input.")
                    continue
                row1.append(element1)
            matrix.append(row1)
            countMatrix1 +=1
        countMatrix1 = 0
        matrix1and2.append(matrix)
        count +=1

    h = 0

    while h < 2:
        matrix = matrix1and2[h]
        i = 0
        while i < 3:
            j = 0
            string = ''
            while j <3:
                string += (str(matrix[i][j]) +"    ")
                j +=1
            print(string)
            i+=1
        h+=1
        print("\n")

    matrix1 = matrix1and2[0]
    matrix2 = matrix1and2[1]
    h = 0
    productMatrix = []
    while h < 3:
        i=0
        productRow = []
        while i < 3:
            j =0
            newEntery = 0
            while j < 3:
                enteryProduct = matrix1[h][j]*matrix2[j][h]
                newEntery += enteryProduct
                j +=1
            productRow.append(newEntery)
            i +=1
        productMatrix.append(productRow)
        h +=1
    i = 0
    while i < 3:
        j = 0
        string = ''
        while j <3:
            string += (str(productMatrix[i][j]) +"    ")
            j +=1
        print(string)
        i+=1


main()






