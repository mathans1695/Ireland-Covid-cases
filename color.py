def generate_pallete():
	pallete = {
		'red': [],
		'green': [],
		'blue': []
	}
	
	for i in range(20):
		value = i*8
		pallete['red'].append('#%02x%02x%02x' %(255, value, value))
		pallete['green'].append('#%02x%02x%02x' %(value, 255, value))
		pallete['blue'].append('#%02x%02x%02x' %(value, value, 255))
		
	return pallete

def color_pallete(color):
	'''accepts color
		returns color pallete'''
	
	return generate_pallete()[color]
		
def get_color(proportion, color):
	'''accpets a porportion
		returns a color based on the proportion'''
	c_pallete = color_pallete(color)
	if proportion >= 0 and proportion < 5:
		return c_pallete[19]
	elif proportion >= 5 and proportion < 10:
		return c_pallete[18]
	elif proportion >= 10 and proportion < 15:
		return c_pallete[17]
	elif proportion >= 15 and proportion < 20:
		return c_pallete[16]
	elif proportion >= 20 and proportion < 25:
		return c_pallete[15]
	elif proportion >= 25 and proportion < 30:
		return c_pallete[14]
	elif proportion >= 30 and proportion < 35:
		return c_pallete[13]
	elif proportion >= 35 and proportion < 40:
		return c_pallete[12]
	elif proportion >= 40 and proportion < 45:
		return c_pallete[11]
	elif proportion >= 45 and proportion < 50:
		return c_pallete[10]
	elif proportion >= 50 and proportion < 55:
		return c_pallete[9]
	elif proportion >= 55 and proportion < 60:
		return c_pallete[8]
	elif proportion >= 60 and proportion < 65:
		return c_pallete[7]
	elif proportion >= 65 and proportion < 70:
		return c_pallete[6]
	elif proportion >= 70 and proportion < 75:
		return c_pallete[5]
	elif proportion >= 75 and proportion < 80:
		return c_pallete[4]
	elif proportion >= 80 and proportion < 85:
		return c_pallete[3]
	elif proportion >= 85 and proportion < 90:
		return c_pallete[2]
	elif proportion >= 90 and proportion < 95:
		return c_pallete[1]
	else:
		return c_pallete[0]

def manual_pallete(color):
	'''accepts color and returns color pallete'''
	
	if color == 'brown':
		return ['#f9ebea', '#e6b0aa', '#cd6155', '#c0392b', '#a93226']
	elif color == 'purple':
		return ['#f5eef8', '#d7bde2', '#af7ac5', '#884ea0', '#633974']
	elif color == 'blue':
		return ['#ebf5fb', '#aed6f1', '#5dade2', '#2e86c1', '#21618c']
	elif color == 'yellow':
		return ['#fef9e7', '#f9e79f', '#f4d03f', '#d4ac0d', '#9a7d0a']
	elif color == 'green':
		return ['#e9f7ef', '#a9dfbf', '#52be80', '#229954', '#196f3d']
	else:
		return ['#eaecee', '#abb2b9', '#566573', '#273746', '#1c2833']
		
def get_manual_color(proportion, color):
	c_pallete = manual_pallete(color)
	if proportion >= 0 and proportion < 20:
		return c_pallete[0]
	elif proportion >= 20 and proportion < 40:
		return c_pallete[1]
	elif proportion >= 40 and proportion < 60:
		return c_pallete[2]
	elif proportion >= 60 and proportion < 80:
		return c_pallete[3]
	else:
		return c_pallete[4]