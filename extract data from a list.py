def main():
	numbers = input("Enter ten digits").split()

	try:
		numbers = list(map(int,numbers))

	except:
		print("Invalid numbers.")
		numbers = []

	print("Length of list is: ", len(numbers))
	print("Maximum number is: ", max(numbers))
	print("Minimum number is: ", min(numbers))
	print("Difference btw maximum and minimum is: ", (max(numbers)-min(numbers)))
	print("Sum of the list is: ", sum(numbers))
	print("Average of the list is", (sum(numbers)/len(numbers)))
	print("Sorted list is:", numbers.sort())
	numbers.remove(max(numbers))
	print(numbers)


main()

