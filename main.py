import operator
from math import log

M = 1 
def importData(file):
	"""
	 This function imports the data into a list form a file name passed as an argument. 
	 The file should only the data seperated by a space.
	"""
	hamData = {}
	spamData = {}
	vocabulary = {}

	ham = 0
	spam = 0

	f = open(str(file), 'r')
	for line in f:
		current = line.split()
		if current[1] == 'ham':
			ham += 1
			for i in range(2, len(current), 2):
				vocabulary[current[i]] = 1
				if hamData.has_key(current[i]):
					hamData[current[i]] = int(hamData.get(current[i])) + int(current[i+1])
				else:
					hamData[current[i]] = int(current[i+1])

		elif current[1] == 'spam':
			spam += 1
			for i in range(2, len(current), 2):
				vocabulary[current[i]] = 1
				if spamData.has_key(current[i]):
					spamData[current[i]] = int(spamData.get(current[i])) + int(current[i+1])
				else:
					spamData[current[i]] = int(current[i+1])
	f.close()

	
	
	Pham = float(ham) / (ham + spam)
	Pspam = float(spam) / (ham + spam)
	
	print ham + spam
	print Pham
	print Pspam

	return hamData, spamData, vocabulary, ham, spam


def getConditionalProbablities(total, hamData, spamData):
	



	hamProbablity ={}
	spamProbablity ={}

	totalHam = 0
	totalSpam = 0

	for word in hamData:
		totalHam += hamData.get(word)

	for word in spamData:
		totalSpam += spamData.get(word)

	for word in hamData:
		hamProbablity[word] = float(hamData.get(word) + float(M/total)) / (totalHam + M)

	for word in spamData:
		spamProbablity[word] = float(spamData.get(word) + float(M/total)) / (totalSpam + M)

	maxHam = dict(sorted(hamProbablity.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
	maxSpam = dict(sorted(spamProbablity.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
	print maxHam
	print maxSpam

	return hamProbablity, spamProbablity, totalHam, totalSpam


def test(TESTNAME, hamProbablity, spamProbablity, totalHam, totalSpam, total):
	correct = 0
	testtotal = 0
	f = open(str(TESTNAME), 'r')
	for line in f:
		spam = float(0)
		ham = float(0)
		current = line.split()
		for i in range(2, len(current),2):
			# print hamProbablity.get(current[i], float(1) / (totalHam + total)),
			# print log1p(hamProbablity.get(current[i], float(1) / (totalHam + total)))
			# print spamProbablity.get(current[i], float(1) / (totalSpam + total)),
			# print log1p(spamProbablity.get(current[i], float(1) / (totalSpam + total)))

			ham += log(hamProbablity.get(current[i], (1 + float(M/total)) / (totalHam + M))) * int(current[i+1])
			spam += log(spamProbablity.get(current[i], (1 + float(M/total)) / (totalSpam + M))) * int(current[i+1])
			
		print ham, spam, current[1]
		
		if ham > spam:
			if current[1] == 'ham':
				correct += 1
		else:
			if current[1] == 'spam':
				correct += 1
		testtotal += 1
	f.close()

	accuracy = float(correct) / testtotal * 100
	print M
	return accuracy



def main(FILENAME, TESTNAME):
	hamData, spamData, vocabulary, ham, spam = importData(FILENAME)
	total =  len(vocabulary.keys())
	hamProbablity, spamProbablity, totalHam, totalSpam = getConditionalProbablities(total, hamData, spamData)

	print test(TESTNAME, hamProbablity, spamProbablity, totalHam, totalSpam, total)



	

if __name__ == '__main__':
	"""
	Main driver function for the experiment.
	"""
	FILENAME = 'nbctrain'
	TESTNAME = 'nbctest'

	M = 996

	main(FILENAME, TESTNAME)
