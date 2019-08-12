import collections
import string
#8.1
def my_read_file(filename):
	file_stream = open(filename, 'r')
	for i in file_stream:
		print(i)

# my_read_file('file.txt')



class Wordcount:
	SPACE = " "
	def __init__(self, filename):
		self.words_counter = collections.Counter()
		self.process_file(filename)



	def process_file(self, filename):	
		file_stream = open(filename, 'r')
		for i in file_stream:
			for j in i.split(self.SPACE):
				# trantab = j.maketrans(string.punctuation,"")
				self.words_counter[j.strip(string.punctuation + "\n").lower()] += 1
		return

	def top_words(self, numwords):
		for word, count in self.words_counter.most_common(20):
			print("%s   %s "  % (word, count))
		return

	def unique_words(self):
		print(len(list(self.words_counter.values())))
		return

	def used_atlease(self, number):
		result = 0
		for _ , count in self.words_counter.items():
			if count >= number:
				result += 1

		print(result)

		return

	def write_most_used(self, filename, amount):
		file_out = open(filename, 'w')
		for word, count in self.words_counter.most_common(amount):
			file_out.write("%s   %s \n" % (word, count))

		return


# TEST CODE
wc = Wordcount("shakespeare.txt")
print("TOP 20  WORDS")
wc.top_words(20)
print("NUMBER OF UNIQUE WORDS")
wc.unique_words()
print("WORDS USED AT LEAST 5 TIMES")
wc.used_atlease(5)
print("200 most used words")
wc.write_most_used("output.txt", 200)



#7.3
#see Markov


import random as rn
#7.4
#a
def random_integers_to_file(n, a, b, filename):
	filestream = open(filename, 'w')
	for _ in range(n):
		filestream.write(str(rn.randrange(a,b)) + "\n")
	filestream.close()
#b
def read_and_return(filename):
	filestream = open(filename, 'r')
	return list(map(int,filestream.readlines()))
	# result = []
	# for i in filestream:
	# 	result.append(int(i))
	# return result
#c
def sum_lists(file1, file2, k):
	result = []
	filestream1 = open(file1, 'r')
	filestream2 = open(file2, 'r')
	a = filestream1.readlines()
	b = filestream2.readlines()

	indexA = [0] * (k + 1)

	for i in a:
		if int(i) <= k:
			indexA[int(i)] += 1
	for j in b:
		if indexA[k - int(j)] and (k - int(j)) >= 0:
			result.append((int(j), k-int(j)))
	return result

'''
random_integers_to_file(2000, 1, 10000, 'test1.txt')
random_integers_to_file(2000, 1, 10000,'test2.txt')
print(read_and_return('testfile.txt'))
print(sum_lists('test1.txt','test2.txt',5000))
'''