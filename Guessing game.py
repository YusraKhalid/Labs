import random

def main():
	#Assinging a random number to a variable
	rightGuess = random.randint(0,20)
	print("Guess the number between 0-20.")
	count = 0

	for var in range(9999999999999):
		count += 1
		guess = input("Enter your guess: ")
		try:
			guess = float(guess)
		except:
			print("Invalid input")
			guess = 0
		if guess == rightGuess:
			print(count,"Congratulations your guess is right.")
			break #If the guess is right than loop breaks
		else:
			print(count, "Ops! wrong guess.")
main()