import collections
import string

class ErrorK(Exception):
    pass
class LengthError(Exception):
    pass


def process_file(filename):
    try:
        file_stream = open(filename, 'r')
        words_counter = collections.Counter()
        for i in file_stream:
            for j in i.split(" "):
                words_counter[j.strip(string.punctuation + "\n").lower()] += 1
        return words_counter
    except(FileNotFoundError) as e:
        print("%s File not found, perhaps a spelling error?" % e)


def top_words(filename, k):
    try:
        if k <= 0:
            raise ErrorK

        words_counter = process_file(filename)
        if k > len(words_counter):
            raise LengthError
        for word, count in words_counter.most_common(k):
            print("%s   %s "  % (word, count))
        return
    except(ErrorK) as e:
        print("%s K Number cannot be less than 1" % e)
    except(IndexError) as oob:
        print("%s Not enough unique words in file" % oob)




    

top_words('shakespeare.txt', 20)

