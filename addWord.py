

##def addWord(dutch, english, typeOfWord, memTrick="", context=""):
##    ''' takes user give attributes for the new word:
##dutch word, english translation, type of word, memory trick and context sentence.
##Creates word object and appends to words.json file'''

'''
reading about software development, I've failed many principles with this
it should be more abstract, it should allow changes to other pieces and reusability
challnege:
function to create an instance of a class using user input on the most abstract level i can

as this is the first thing ive made. I just wanna make it work.

Leaarnt:
#this while loop doesnt work at the moment
while(typeWord != 1 or typeWord != 2 or typeWord !=3)):

when i give an input of 1 or 2 or 3, the loop still runs. this is because i should
have been using and. It runs because one of the other loops is still true.
I need to think more carefully about the logic of or and and. I've messed this up
before

'''

from wordsClasses import Verb, Noun, Connective
import json

def newWordUser():
    ''' using user inputs it returns a tuple containg an instance of the new word and
what type of word it is that was created
'''
    typeWord = 0
    #this while loop doesnt work at the moment
    while(typeWord != 1 and typeWord != 2 and typeWord !=3):
        typeWord = int(input('What sort of word is it? type 1 for verb, 2 for noun, 3 for connective \n'))
        
    dutch = ''
    while dutch == '':
        dutch = input('what is the new word in dutch? \n')

    english = ''
    while english == '':
        english = input('what is the new word in english? \n')

    memTrick = input('A memory trick really helps. Type one: \n')
    context = input('A context sentence is a good memory tool. Type one: \n')

    if typeWord == 1:
        tense = input('what tense is this version of the word \n')
        return(Verb(dutch, english, memTrick, context, tense), 'verbs')

    if typeWord == 2:
        print('These are the current categories: \n')
##        for cat in categories:
##            print(cat)
        category = input('Whats the category of this word? \n')
        return(Noun(dutch, english, memTrick, context, category), 'nouns')

    if typeWord == 3:
        print('The word order after the connective is important')
        print(' e.g. verb pronoun ... or pronoun ... verb?')
        wordOrder = input('Whats the word order after this connective? \n')
        return(Connective(dutch, english, memTrick, context, wordOrder), 'connectives')

def addNewWordToFile(newWord, typeWord):
    f = open('words.json')
    myWords = json.load(f)
    f.close()
    #need to add a way to check for duplicates here
    myWords['words'][0][typeWord].append(vars(newWord))
    f = open('words.json', 'w')
    json.dump(myWords, f, indent=2)
    f.close()

def addNewWord():
    newWord, typeOfWord = newWordUser()
    addNewWordToFile(newWord, typeOfWord)

#addNewWord()


#just checking it worked
f = open('words.json')

'''
its possible to only pull the correct values rather than the whole file but i think
taking the whole file in a dict form then searching is faster
'''
##for i in f:
##    print(i)
##    print('*'*20)
##
##for i in f:
##    print(i.split()[0])
myWords = json.load(f)
print(json.dumps(myWords, indent=2))
f.close()
    
