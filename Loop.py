def main():
	number = input("Enter a number: ")
	try:
		number = int(number)
	except:
		print("Invalid input.")
		number = 0
#Taking asterisk as an empty string and than entering it to this string for everytime the loop works
	asterisk = ""
	for var in range(1,number+1):
		asterisk += "*"

	print(asterisk)
main()