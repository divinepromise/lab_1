def do_twice(f,value):
	f(value)
	f(value)


def print_spam(value):
	print(value)


def do_four(f, value):
	do_twice(f,value)
	do_twice(f,value)


do_four(print_spam,"spam")
