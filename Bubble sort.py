def main():
	count = 0
	mylist = []
	while count < 10:
		element = input("Enter the element of list: ")
		try:
			element = int(element)
		except:
			print("Invalid input. Enter again.")
		else:
			count +=1
			mylist.append(element)

	for i in range(len(mylist)-1): #this loop is used for the number of times a list is sorted
		for j in range (len(mylist)-1): #this loop is used for moving the higest number towards the end.
			if mylist[j] > mylist[j+1]:
				temporary = mylist[j]
				mylist[j] = mylist[j+1]
				mylist[j+1] = temporary
				print(mylist)
	print("The sorted list is:",mylist)
main()


