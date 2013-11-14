import random

def readFile(filename):
    f = open(filename)
    text = f.read()
    f.close()
    return text.split()

class MarkovTable(object):
    def __init__(self, text):
        self.table = self.build(text)

    def build(self, text):
        table = {}

        def addWordsToTable(word1, word2):
            nonlocal table
            if word1 not in table:
                table[word1] = {}
            if word2 not in table[word1]:
                table[word1][word2] = 0
            table[word1][word2] += 1

        # Loop through text
        for i in range(len(text) - 1):
            currentWord, nextWord = text[i], text[i + 1]
            addWordsToTable(currentWord, nextWord)

        # Normalize table
        for row in table.values():
            total = sum(row.values())

            for nextWord in row.keys():
                row[nextWord] /= total

        return table

    @property
    def wordList(self):
        return list(self.table.keys())

    def getRandomWord(self):
        return random.choice(self.wordList)

    def getNextWord(self, currentWord):
        # Weird code, ask me to explain this!
        r = random.random()
        probSum = 0
        row = self.table[currentWord]
        for nextWord in list(row.keys()):
            prob = row[nextWord]
            probSum += prob
            if r < probSum:
                return nextWord

    def generateSentence(self):
        word = self.getRandomWord()
        sentence = [word]
        while word != ".":
            nextWord = self.getNextWord(word)
            sentence.append(nextWord)
            word = nextWord
        return ' '.join(sentence)
