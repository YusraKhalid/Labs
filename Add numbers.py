def main():
	numberOfSum = input ("Enter the number of values you want to add: ")
	integers = input("Enter the numbers you want to add: ").split() #sequence is taken as input
	try:
		numberOfSum = int(numberOfSum)
	except:
		print ("Invalid input.")
		numberOfSum = 0
	addition = 0
	count = 1


	for var in integers:
		if count <= numberOfSum:
			try:
				var = float (var)
			except:
				print("Invalid input.")
				break
			else:	

				addition += var #adding the current number in the previouslly added numbers
		count += 1
	print (addition)
main()
