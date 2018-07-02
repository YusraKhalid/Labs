def main():
	name = ["Ali","Ahsan","Ahmed","Zubair"]
	print (name)

#getting input from user
	name1, name2, name3, name4 = input ("Enter 4 names: ").split()
	
	#conveting names to uppercase
	name1 = name1.upper()
	name2 = name2.upper()
	name3 = name3.upper()

#replacing list with user entered data
	name.pop(0)
	name.insert(0,name1)
	name.pop(1)
	name.insert(1,name2)
	name.pop(2)
	name.insert(2,name3)
	name.pop(3)
	name.insert(3,name4)

	print(name)
	
	#index "2" from negative side of 4 member list is "-2"
	nameAt2 = name[-2]

	print ("Name at index 2 is:", nameAt2)

main()