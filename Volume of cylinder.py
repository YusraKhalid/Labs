def volume (radius, height):
	vol= 3.14 * (pow (radius, 2) * height)
	return (vol)

def main():
	diameter = float (input ("Enter diameter of cylinder :  "))
	radius = diameter / 2
	height = float ( input ("Enter height of cylinder : "))
	print (volume (radius, height), "Sq units")

main()