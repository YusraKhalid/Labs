def main():
	number = input("Enter a list of numbers: ").split() #Getting input in list from user
	remaining = len(number) #Remaing list to be checked is the total list
	try:
		smallest = float(number[0]) #putting first number as the smallest number if second, third or any other number is smaller than this it will be changed by it.
	except:
		print("Invalid input.")
		smallest = 0

	for var in number:
		try:
			var = float(var)
		except:
			print("Invali input.")
			break
		if var < smallest:
			smallest = var
		remaining -= 1
		print("Smallest number till yet is:",smallest)
		print("Remaining numbers are: ", remaining)
	print("The overall smallest number is: ", smallest)
main()

