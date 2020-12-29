import matplotlib.pyplot as plt
from color import manual_pallete

x1 = [0, 1, 1, 0]
y1 = [0, 0, 20, 20]
x2 = [0, 1, 1, 0]
y2 = [20, 20, 40, 40]
x3 = [0, 1, 1, 0]
y3 = [40, 40, 60, 60]
x4 = [0, 1, 1, 0]
y4 = [60, 60, 80, 80]
x5 = [0, 1, 1, 0]
y5 = [80, 80, 100, 100]

def pallete_legend(axes, pallete_color):
	color = manual_pallete(pallete_color)
	
	axes.get_xaxis().set_visible(False)

	right = axes.spines['right']
	right.set_visible(False)

	left = axes.spines['left']
	left.set_visible(False)

	top = axes.spines['top']
	top.set_visible(False)

	bottom = axes.spines['bottom']
	bottom.set_visible(False)

	axes.fill(x1, y1, color=color[0])
	axes.fill(x2, y2, color=color[1])
	axes.fill(x3, y3, color=color[2])
	axes.fill(x4, y4, color=color[3])
	axes.fill(x5, y5, color=color[4])
	axes.set_xlim([0, 1])
	axes.set_ylim([0, 100])