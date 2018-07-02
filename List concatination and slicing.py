#converting str to int
def trying(oneList, twoList):
	flag = True
	try:
		oneList = list(map(int, oneList))
		twoList = list(map(int, twoList))

	except:
		print("Invalid input.")
		flag = False

	return (flag,oneList,twoList)


def main():
	markList1 = input("Enter the marks of four subjects: "). split()
	markList2 = input("Enter the marks of next four subjects: "). split()

	
	#converting the input to integer form.
	flag, markList1, markList2 = trying(markList1, markList2)

#if there is no exception than combining the list and seperating it.

	if flag == True:

		markList1.extend(markList2)

		print (markList1)

		markList2 = markList1[4:8]
		markList1 = markList1[0:4]

		print(markList1)
		print(markList2)

main()


