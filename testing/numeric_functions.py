##################
# Functions to do things with numbers
# Modified from Software Carpentry: http://katyhuff.github.io/python-testing/
##################

def mean(vals=[]):
	"""
	Calculates the mean values of a list of numbers
	If you enter a list of ints, you'll get a list of ints!!
	
	RETURNS
	mean value of list
	"""
	#mean_val = sum(vals)/float(len(vals))
	mean_val = sum(vals)/len(vals)
	return mean_val
	