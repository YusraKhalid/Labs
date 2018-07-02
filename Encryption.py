
def encryption(digit):
	digit = (digit+7) % 10
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
	number = input ("Enter 4 digit number:")
	try:
		number = int (number)

	except:
		print("Invalid number.")

	else:
		print (seperatingDigits(number))

	finally:
		print("Encryption Complete.")

main()
