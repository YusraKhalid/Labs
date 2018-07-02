def grocery(shoppingList):
	newItems = input("Enter five grocery items").split()
	shoppingList.extend(newItems)

	return (shoppingList)

def main():
	shoppingList = []
	shoppingList1 = grocery(shoppingList)
	shoppingList2 = (grocery(shoppingList1))
	shoppingList3 = (grocery(shoppingList2))
	shoppingList4 = (grocery(shoppingList3))
	shoppingList5 = (grocery(shoppingList4))

	print(shoppingList)

main()
