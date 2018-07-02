def prime(number):
	isPrime = True
	#if a number is divisible by any number other than itself and 1 than we say it is not a prime number
	for var in range(2,number):
		if number % var == 0:
			isPrime = False
		else:
			isPrime = isPrime and True
	return (isPrime)
#This function is returning if the number is prime or not

def main():
	#User enters the number till where it wants to check the prime numbers.
	checkTill = input("Enter a number till where you want to check prime numbers: ")
	try:
		checkTill = int(checkTill)
	except:
		print("Invalid number.")
		checkTill = 0
	
	for var in range(1, checkTill+1):
		isPrime = prime(var)
		if isPrime == True:
			print(var)

main()

