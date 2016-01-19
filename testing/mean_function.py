# Program: numeric_functions.py

def mean(vals=[]):
	"""
	Calculates the mean values of a list of numbers
	
	RETURNS
	mean value of list
	"""
	mean_val = sum(vals)/len(vals)
	return mean_val
	