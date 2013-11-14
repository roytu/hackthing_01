import random

def readFile(filename):
    """Reads a file from directory <filename> and returns the full text as a string
    >>> readFile("../sample_tests/smalltest")
    'Hi mom . Hi dad .'
    """
    """ YOUR CODE HERE """
    pass

class MarkovTable(object):
    def __init__(self, text):
        self.table = self.build(text)

    def build(self, text):
        """Build the Markov table.
        """
        # TODO: Doctests
        """ YOUR CODE HERE """
        pass

    @property
    def wordList(self):
        return list(self.table.keys())

    def getRandomWord(self):
        return random.choice(self.wordList)

    def getNextWord(self, currentWord):
        """Return a random word based on the current word and the Markov table"""
        # TODO: Doctests
        pass

    def generateSentence(self):
        """Generate a random sentence"""
        # TODO: Doctests
        pass
