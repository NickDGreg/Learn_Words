from wordsClasses import Verb, Noun, Connective

##
##class words(object):
##    ''' to establish json dictionary
##'''
##    def __init__(self, words=[]):
##        self.words = words
##
##    def get_JSON_dict(self):
##        #creates a dict of own attributes
##        d = vars(self)
##        words_list = []
##        return(d)
##
##wordList = words()
##
##print(wordList.get_JSON_dict())
##

wordList = {'words': [{'verbs': [], 'nouns': [], 'connectives':[]}]}
'''
to access the correct place in the dictionary

wordList['words'][0]['verbs'/'noun'/'connective']


this would print the dutch nouns, i is a dict of vars of one word
for i in myWords['words'][0]['nouns']:
    print(i['dutch'])

'''

tonen = Verb('tonen', 'to show', 'the sharp tones show the whale is distressed'
             , tense = 'present')
nederigheid = Noun('nederigheid', 'humility')
opmerking = Noun('opmerking', 'remark')

wordList['words'][0]['verbs'].append(vars(tonen))
wordList['words'][0]['nouns'].append(vars(nederigheid))
wordList['words'][0]['nouns'].append(vars(opmerking))

hoewel = Connective('hoewel', 'although', 'although, how well it went depends on your view',
                    'Hoewel ik ging naar de winkel, ik heb geen eten', 'normal')

##
##
import json
f = open('words.json', 'w')
json.dump(wordList, f, indent=2)
f.close()

'''

'''
f = open('words.json')
myWords = json.load(f)
#print(json.dumps(myWords, indent=2))
f.close()

#adds new word to the dictionary pulled from the json file
myWords['words'][0]['connectives'].append(vars(hoewel))

f = open('words.json', 'w')
#replaces old dict with new dict
json.dump(myWords, f, indent=2)
f.close()

#just checking it worked
f = open('words.json')
myWords = json.load(f)
print(json.dumps(myWords, indent=2))
f.close()


