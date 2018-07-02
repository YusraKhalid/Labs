def summation(num):
	if num == 0:
		return 0
	else:
		return ((num) + summation(num-1)) #calling the summation function till it reaches zero then returning this value in the line and calculating sum


def main():
	var = input("Enter the number you want to take summation of from zero: ")
	try:
		var = int(var)
	except:
		print("Invald input.")
		var = 0 #if input is not integer then return 0
	if (var < 0):
		print("Ther is no factorial of negative number.")
	else:
		print("Sum of the given number from zero is: ",summation(var))

main()