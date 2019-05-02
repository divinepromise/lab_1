def check_fermat(a,b,c,n):
	if n>2 and a**n+b**n==c**n:
		print("Holy smokes, Fermat was wrong!")
	else:
		print("No, that doesnt work.")


def input_values_fermat():
	a=int(input("Enter the value of a: "))
	b=int(input("Enter the value of b: "))
	c=int(input("Enter the value of c: "))
	n=int(input("Enter the value of c: "))
	check_fermat(a,b,c,n)



input_values_fermat()
