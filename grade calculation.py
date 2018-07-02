def grade(marks):
	if marks >= 90:
		return "A"
	elif (marks< 90) and (marks >= 80):
		return "B"

	elif (mark < 80) and (marks>= 70):
		return "C"

	elif (marks < 70) and (marks >= 60):
		return "D"
	else:
		return "F"


def main():
	marks = input("Enter your marks: ")
	try:
		marks = int (marks)
		if marks > 100:
			raise exception
	except:
		print("Enter valid marks.")

	else:
		print (grade(marks))

	finally:
		print ("Program End")

main()
