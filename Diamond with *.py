def main():
	for i in range(6):
		str1 = ""
		str2 = ""
		str3 = ""
#making three patterns two of * and one of sp-aces. then combining them to get the required upper part of the shape

		for j in range(i):
			str1 += "*"
		for k in range(6-i):
			str2 += " "
		for l in range (i-1):
			str3 += "*"

		print(str2 + str1 + str3) #first printing the spaces than * of one pattern and then of other

	for a in range(5):
		str4 = ""
		str5 = " "
		str6 = ""
#making three patterns two of * and one of sp-aces. then combining them to get the required lower part of the shape. Both combined will give the required shape
		for b in range (3-a):
			str4 += "*"
		for c in range (a+1):
			str5 +=" "
		for d in range (4-a):
			str6 += "*"
		print (str5 + str4 + str6)

main()