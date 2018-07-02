def odd(digit):
	number = (digit*3) + 1
	return number

def even(digit):
	number = digit/2
	return number

def main():
	currentNumber = input ("Enter a number: ")
	flag = False
	try:
		currentNumber = int(currentNumber)
	except:
		print("Enter a valid number.")
	else:
		flag = True

	
	if flag == True:
		if (currentNumber%2 != 0):
			print (odd(currentNumber))

		else:
			print (even(currentNumber))

	print ("Program End")

main()