
def check_fermat(a,b,c,n):
	if n>2 and a**n+b**n==c**n:
		print("Holy smokes, Fermat was wrong!")
	else:
		print("No, that doesnt work.")


check_fermat(3,5,4,5)
