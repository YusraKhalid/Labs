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
	count = len(mylist)-1 #this variable will not search the list from end, which is already sorted.

	for i in range(count):#this loop is used for the number of times a list is sorted
		for j in range (count):#this loop is used for moving the higest number towards the end.
			if mylist[j] > mylist[j+1]:
				temporary = mylist[j]
				mylist[j] = mylist[j+1]
				mylist[j+1] = temporary
				print(mylist)
		count -=1
		print("The sorted list is:",mylist)
main()


