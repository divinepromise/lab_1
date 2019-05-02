def grid_line():
	i=1
	while i<=3:
		print('+','---',sep='',end="")
		i+=1
	print("+")


def draw_bar():
	j=1
	while j<=3:
		print('|   ',sep='',end="")
		j+=1
	print("|")


def draw_bar_loop():
	i=1
	while i<=4:
		draw_bar()
		i+=1




grid_line()
draw_bar_loop()
grid_line()
draw_bar_loop()
grid_line()
