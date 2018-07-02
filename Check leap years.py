def leapYear(year):
	if (year/4):
		required = "Leap Year"

	else:
		required = "Not a leap year"
	
	return required

def main():
	year = input("Enter the year: ")
	try:
		year = int(year)
	except:
		print("Enter a valid year.")
	else:
		print(leapYear(year))

	finally:
		print ("Program complete.")

main()