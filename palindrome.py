def palindrome(digit):
	fifth = digit % 10
	digit = digit // 10
	fourth = digit%10
	digit = digit// 10
	third = digit % 10
	digit = digit// 10
	second = digit % 10
	first = digit // 10
	if (first == fifth) and (second == fourth):
		return "It is a palindrome."

	else:
		return "It is not a palindrome."

def main():
	number = input("Enter a 5 digit number:")
	try:
		number = int(number)

	except:
			print("Invalid number.")

	else:
		print(palindrome(number))

main()