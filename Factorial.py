def factorial(num):
	if num == 0:
		return 1
	elif num == 1:
		return 1
	else:
		num -= 1 #reducing the value of number 
		return ((num+1) * factorial(num)) #num +1 is used as we minused 1 from it in one step before

def main():
	var = input("Enter the number you want to take factorial of: ")
	try:
		var = int(var)
	except:
		print("Invald input.")
		var = 0  #if input is not integer then return 0
	if (var < 0):
		print("Ther is no factorial of negative number.")
	else:
		print("Factorial of the given number is: ",factorial(var))

main()