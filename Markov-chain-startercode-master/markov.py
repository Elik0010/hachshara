import random
import sys

def process_line(line, key):
    '''
    Process a line of text to extract (state, new_word) pairs.
    Note that we remove uppercase letters in this example, though
    you don't have to.

    Example:
    process_line("In winter I get up at night") =
    [('BEGIN', 'in'),
     ('in', 'winter'),
     ('winter', 'i'),
     ('i', 'get'),
     ('get', 'up'),
     ('up', 'at'),
     ('at', 'night'),
     ('night', 'END')]

    We add the BEGIN and END keywords so that we can initialize the
    sentence and know when the line ends.
    '''

    # YOUR CODE HERE #
    line_list = line.lower().split(" ")
    # print(line_list)
    # for t in line_list:
    #     t = t + " "
    key -= 1
    result = []
    # print(" ".join(line_list))
    # try:
    # result.append(('BEGIN ' + " ".join(line_list[:key]), line_list[key + 1]))
    result.append(('BEGIN'," ".join(line_list[: key + 1])))
    for i in range(len(line_list) - 1 - key):
        result.append((" ".join(line_list[i : i + key + 1]), line_list[i + key + 1]))
    result.append((" ".join(line_list[-key:]), "END"))
    return result
    # except:
    #     pass
def process_textfile(filename, key):
    '''
    Creates a dictionary with transition pairs
    based on a file provided

    For the first part of the assignment, we use a
    placeholder text that you will have to replace
    at some point.

    Based on the placeholder text, the dictionary
    should contain the following key-value pairs:

    'blue,': ['END']
    'by': ['yellow', 'day.', 'day?']
    'still': ['hopping', 'going']
    '''
    d = {}
    f = open(filename, 'r')
    # YOUR CODE HERE #
    for i in f: #each line
        if len(i) == 0:
            continue
        sub_list = process_line(i, key)
        if not sub_list:
            continue
        for j, k in sub_list:
            if j == " " or k == " ":
                continue
            if j.strip(" ") in list(d.keys()):
                d[j.strip(" ")].append(k.strip(" "))
            else:
                d[j.strip(" ")] = [k.strip(" ")]
    return d

def generate_line(d, length):

    # TODO find out what causes a key error, it should not be happening

    result = ""
    next_word = "BEGIN"
    # key = random.choice(list(filter(check_key('BEGIN'),list(d.keys()))))
    next_word = random.choice(d['BEGIN'])
    while next_word != 'END':
        result += next_word + " "
        if '\n' in result or result[-2:] == "  ":
            return result
        # if len(result.split(" ")) >= length:
        try:
            next_word = random.choice(d[" ".join(result.strip(" ").split(" ")[-length:])])
        except:
            next_word = random.choice(random.choice(list(d.values())))
    return result



def check_key(keys, key):
    '''
    checks that this key has a 'BEGIN' in it
    '''
    return True if key in keys else False


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('ERROR: Run as python markov.py <filename> <word accuracy>')
        exit()
    d = process_textfile(sys.argv[1], int(sys.argv[2]))
    for i in range(5000):
        print(generate_line(d, int(sys.argv[2])))
