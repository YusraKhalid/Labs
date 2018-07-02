def grossPay(hour):

	payPerHour = 20000/40
	payAbove40Hour= ((hour-40)*(1.5*payPerHour)+20000)
	payFor45Hours = (5*(1.5*payPerHour)+20000)
	payAbove45Hour = ((hour-45)*(2*payPerHour)+payFor45Hours)
	if hour == 40:
		return("His gross pay will be Rs20000.")

	elif (hour <= 45 ) and (hour > 40):
		return(payAbove40Hour)

	else:
		return (payAbove45Hour)


def tax(hour):
	taxes = grossPay(hour)*0.28
	return (taxes)

def netPay(hour):
	net = grossPay(hour)-tax(hour)
	return(net)




def main():
	hours = int(input("Enter the hours worked in a week: "))
	if hours >=40:
		print("His gross pay is: ", grossPay(hours))
		print("His taxes are: ", tax(hours))
		print("His net pay is: ", netPay(hours))

	else:
		print("He has not worked enough hours.")

main()
