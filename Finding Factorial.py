
def main():
	#Taking input from user till where it wants the factorial
	variable = input("Enter a number: ")
	try:
		variable = int(variable)
	except:
		print("Invalid input.")
		variable = 0
	print("X	factorial of X")
	for number in range(1,variable+1):
		factorial = 1
		for var in range(1,number+1): #Calling loop in a loop so that every number is multiplied by all the number before it.
			factorial *= var
		print(number,"	", factorial)

main()