#I'm not certain what super() is doing in the subclasses


class Word(object):
    ''' This is the main word object. Contains key attributes and methods
of all types of words (verbs, nouns, adjectives,...)'''
    def __init__(self, dutch, english, memTrick="", context=""):
        self.dutch = dutch
        self.english = english
        self.memTrick = memTrick
        self.context = context
    #i dont know best practice for printing. Should I have return here
        #or make it a function which prints by itself? currently i type
        #print(word.print_dutch()) which seems weird.
    def translation_dutch(self):
        return(self.dutch)

    def translation_english(self):
        return(self.english)

    def call_memTrick(self):
        return(self.memTrick)

    def call_context(self):
        return(self.context)

    def change_dutch(self, newDutch=''):
        while newDutch == '':
            newDutch = input("what should the dutch become? \n")
        self.dutch = newDutch

    def change_english(self, newEnglish=''):
        while newEnglish == '':
            newEnglish = input("what should the english translation become? \n").format(dutch=self.dutch)
        self.english = newEnglish

    def change_memTrick(self, newMemTrick=''):
        while newMemTrick == '':
            newMemTrick = input("whats your new memory trick? \n")
        self.memTrick = newMemTrick

    def change_context(self, newContext=''):
        while newContext == '':
            newContext = input("whats your new context sentence? \n")
        self.context = newContext
        
class Verb(Word):
    def __init__(self, dutch, english, memTrick="", context="", tense=''):
        super(Word, self).__init__()
        self.dutch = dutch
        self.english = english
        self.memTrick = memTrick
        self.context = context
        self.tense = tense

class Noun(Word):
    def __init__(self, dutch, english, memTrick="", context="", category=''):
        super(Word, self).__init__()
        self.dutch = dutch
        self.english = english
        self.memTrick = memTrick
        self.context = context
        self.category = category

    def __str__(self):
        read = "{dutch} in english is: {english}".format(
            dutch = self.dutch,
            english = self.english)
        return(read)

class Connective(Word):
    def __init__(self, dutch, english, memTrick="", context="", wordOrder=''):
        super(Word, self).__init__()
        self.dutch = dutch
        self.english = english
        self.memTrick = memTrick
        self.context = context
        self.wordOrder = wordOrder

    def print_wordOrder(self):
        print(self.wordOrder)
