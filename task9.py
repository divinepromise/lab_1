def is_triangle(a,b,c):
	if a>b+c or b>a+c or c>a+b:
		print("You cannot form a triangle")
	elif a+b==c or b+c==a or a+c==b:
		print("You form degenerate triangle")
	else:
		print("You can")


is_triangle(3,4,5)

