def main():
	#taking two variables as 0 and 1 to start the series
	var01 = 0
	var02 = 1
	fibonacci = [var01,var02] #The starting values of the series are included in the list
	
	for var in range(1,10):
		var03 = var01 + var02
		var01 = var02
		var02 = var03
		fibonacci.append(var03) #appending each new value in the list
	print(fibonacci)

main()