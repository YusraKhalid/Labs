def encryption(digit):
	if digit >= 7:
		digit = digit - 7
	else:
		digit = (digit + 10) - 7

	return digit



def seperatingDigits(digit):
	fourth = digit%10
	digit = digit// 10
	third = digit % 10
	digit = digit// 10
	second = digit % 10
	first = digit // 10


	first = encryption(first)
	second = encryption (second)
	third = encryption (third)
	fourth = encryption (fourth)

	temporaryFirst = first
	first = third
	third = temporaryFirst

	temporarySecond = second
	second = fourth
	fourth = temporarySecond

	required = str(first) + str(second) + str(third) + str(fourth)
	return required


def main():
	number = input ("Enter 4 digit encrypted number:")
	try:
		number = int (number)

	except:
		print("Invalid number.")

	else:
		print (seperatingDigits(number))

	finally:
		print("Encrypted number convertion Complete.")

main()


