import logging


class Instance(object):
	"""This is the instance class used to collect the data."""
	def __init__(self, inputString):
		super(Instance, self).__init__()
		self.email = inputString[0]
		self.classLable = inputString[1]

		

def importData(file):
	"""
	 This function imports the data into a list form a file name passed as an argument. 
	 The file should only the data seperated by a space.
	"""
	data = []
	f = open(str(file), 'r')
	for line in f:
		current = line.split()	#enter your own delimiter like ","
		data.append(Instance(current))
	return data


def getPriorProbablities(data):
	"""
	Function to get the prior probablities of the dataset.
	"""
	ham = 0
	spam = 0
	for instances in data:
		if instances.classLable == 'ham':
			ham += 1
		elif instances.classLable == 'spam':
			spam +=1
		else:
			print "err"
	ham =  float(ham)/len(data)
	spam = float(spam)/len(data)
	return ham, spam



def main(FILENAME):
	data = importData(FILENAME)
	Pham, Pspam = getPriorProbablities(data)

	


if __name__ == '__main__':
	"""
	Main driver function for the experiment.
	"""
	FILENAME = 'nbctest'
	main(FILENAME)
