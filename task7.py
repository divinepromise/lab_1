def do_n(f,n):
	i=1
	while i <= n:
		f()
		i+=1


def print_spam():
	print("spam")


do_n(print_spam,10)
