import string
import random


class Agent:
    '''
    Agent picks a random word from the wordlist as chooser.
    Agent picks a random remaining character as guess.

    This simple agent shows the setup of the methods of an Agent.
    '''

    def __init__(self, wordlist):
        self.available = [x for x in string.ascii_lowercase]
        self.wordlist = list(wordlist)  # create a copy\
        self.guesses = 0

    def getWord(self):
        '''
        Returns a word from the wordlist as word to be guessed.

        In this case, we pick a random word from the wordlist
        '''
        return random.choice(self.wordlist)

    def getGuess(self, hiddenWord):
        '''
        Returns a character as guess

        In this case, picks randomly from the remaining characters
        '''
        if self.guesses == 0:
            ch = 'e'
        elif self.guesses == 1:
            ch = 'a'
        else:
            ch = random.sample(self.available, 1)[0]
        self.available.remove(ch)
        self.guesses += 1
        return ch




class MyAgent(Agent):
    """Better version of a computer agent for playing hangman"""
    def __init__(self, wordlist):
        super().__init__(wordlist)
        self.letter_list = ""

        

    def getGuess(self, hiddenWord):
        if self.letter_list == "":
            self.letter_list = self.get_letter_list(hiddenWord)

        ch = self.letter_list[0]
        del self.letter_list[0]
        return ch


    def get_letter_list(self, hiddenWord):
        length = len(hiddenWord.split(" "))
        letters = {1:"ai",
                    2:"aoeimhnustyblpxdfrwgjk",
                    3:"aeoitsuprndbgmylhwfckxvjzq",
                    4:"aesoirltnudpmhcbkgywfvjzxq",
                    5:"searoiltnudcypmhgbkfwvzxjq",
                    6:"esariolntducmpghbykfwvzxjq",
                    7:"esiarntolducgpmhbyfkwvzxjq",
                    8:"esiarntoldcugmphbyfkwvzxqj",
                    9:"esirantolcdugmphbyfvkwzxqj",
                    10:"eisrantolcdugmphbyfvkwzxqj",
                    11:"eisnartolcudpmghbyfvkwzxqj",
                    12:"eisntarolcpumdghybvfzkwxqj",
                    13:"ientsaorlcpumgdhybvfzxkwqj",
                    14:"eitsnaorlcpumdhgybvfzxkwqj",
                    15:"ietnsoarlcpumdhgybvfzxwkqj",
                    16:"eitsnaorlcpumhdygbvfzxwqkj",
                    17:"ietnsoarlcpumhdgybvfzxqwjk",
                    18:"isetonralcpmuhdgybvzfxqwk",
                    19:"ietonasrlcpmuhdgybvfzxkjqw",
                    20:"ioetrsanclphumydgbzvfwkxjq"}
        general = "esiarntolcdupmghbyfvkwzxqj"
        if length >= 21:
            return general
        return letters[length]

        
class HumanAgent(Agent):
    '''
    HumanAgent asks user for input using the command line interface
    '''

    def getWord(self):
        '''
        Query the user for a word, making sure it is in the word list
        '''
        while True:
            word = raw_input('Pick a word: ')
            word = word.lower()
            if word in self.wordlist:
                return word
            else:
                print('Word not recognized, please try again')

    def getGuess(self, hiddenWord):
        '''
        Query the user for a character as guess
        '''
        while True:
            ch = raw_input('Next guess: ')
            if ch in self.available:
                self.available.remove(ch)
                return ch
            else:
                print('Not a valid guess, please pick from:')
                print(' '.join(self.available))
