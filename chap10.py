# Chapter 10 Exercises 10.7 and 10.13
# Patrick Kennedy

#10.7
def is_anagram (testword, comparedword):
	holder = []
	holder2 = []
	flag = False



	if testword == comparedword: #this works
		return True
	elif len(testword) != len(comparedword): #this works
		return False
	else:
		for i in testword:
			holder.append(i)
			print holder

		for j in comparedword:
			holder2.append(j)
			print holder2

		if holder.sort() == holder2.sort(): #I didn't think this would actually work! Who knew?
			return True
		else:
			return False	


Word1 = 'rickPat'
Word2 = 'Patrick'
#print "This is Exercise 10.7"
#print is_anagram(Word1, Word2)




#10.13 - Interlocking words

thesaurus = open('words.txt')

def is_interlocking(peanutbutter, jelly, thesaurus):
	testlock = peanutbutter
	testlock += jelly
	testlist = []
	counter = 0
	line = thesaurus.readline()

	for i in testlock:
		testlist.append(i) 

	for line in thesaurus:
		word = line.strip()
		compareword = []
		for x in word:
			compareword.append(x)
		if compareword.sort() == testlist.sort():
			Print word
			counter += 1

	if counter == 0:
		print "there were no interlocking words from the two given"		



