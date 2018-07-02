def main():
	for i in range (1,10):
		str1 = ""
		for j in range (i):
			str1 += "*"
		print(str1)

	print("") #Just to give space between different structures
	print("") #Just to give space between different structures

	for a in range (10,1,-1):
		str2 = ""
		for b in range(a-1):
			str2 += "*"
		print(str2)

	print("") #Just to give space between different structures
	print("") #Just to give space between different structures

	for c in range (10):
		str3 = "" #one string for * and one for star
		str4 = ""
		for d in range (10-c): #one loop for * and one for the space
			str3 += "*"
		for e in range (c):
			str4 += " "
		print (str4 + str3)

	print("") #Just to give space between different structures
	print("") #Just to give space between different structures

	for g in range (10):
		str5 = ""
		str6 = ""
		for h in range(g):
			str5 += "*"
		for k in range(10-g):
			str6 += " "
		print(str6 + str5)


main()