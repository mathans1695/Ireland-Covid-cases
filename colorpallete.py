# colorPallete accept a function and returns colorPallete
def colorpallete(color=None, num=None):
	if color == 'brown' or num == 1:
		return ['#e6b0aa', '#d98880', '#cd6155', '#c0392b', '#a93226', '#922b21']
	elif color == 'red' or num == 2:
		return ['#f5b7b1', '#f1948a', '#ec7063', '#e74c3c', '#cb4335', '#b03a2e']
	elif color == 'purple' or num == 3:
		return ['#d2b4de', '#bb8fce', '#a569bd', '#8e44ad', '#7d3c98', '#6c3483']
	elif color == 'blue' or num == 4:
		return ['#aed6f1', '#85c1e9', '#5dade2', '#3498db', '#2e86c1', '#2874a6']
	else:
		return ['#a2d9ce', '#73c6b6', '#45b39d', '#16a085', '#138d75', '#117a65']