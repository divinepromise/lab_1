def is_triangle(a,b,c):
	if a>b+c or b>a+c or c>a+b:
		print("You cannot form a triangle")
	elif a+b==c or b+c==a or a+c==b:
		print("You form degenerate triangle")
	else:
		print("You can")


def user_input_for_triangle_check():
	a=int(input("Enter the value of a: "))
	b=int(input("Enter the value of b: "))
	c=int(input("Enter the value of c: "))

	is_triangle(a,b,c)


user_input_for_triangle_check()

