import json

def playWord(word, language):
    """word is a dictionary from json file containing the components of the word
english, dutch, memtrick, context
language is dutch or english. dutch means user is given the dutch word as prompt.
"""
    if language == 'dutch':
        translation = 'english'
    else:
        #language is english
        translation = 'dutch'
        
    print("The word is:")
    print(word[language])
    #ask user for english answer. I repeat this: how can i avoid that?
    if answerCheck(word, translation) == True:
        return("good job!")
    else:
        print('Unlucky, perhaps some context will help:')
        print(word['context'])
        if answerCheck(word, translation) == True:
            return('good job!')
        else:
            print('Unlucky, perhaps your memory trick will help:')
            print(word['memTrick'])
            if answerCheck(word, translation) == True:
                return('good job')
            else:
                print('Hopefully you can remember it next time. The translation is:')
                return(word[translation])

def pullWords(typeOfWord):
    '''returns ditctionary of words of type = typeOfWord
'''
    f = open('words.json')
    myWords = json.load(f)
    f.close()
    words = myWords['words'][0][typeOfWord]
    return(words)


def answerCheck(word, translation):
    print("")
    answer = input('Do you know the translation? \n')
    print('*'*10)
    if answer == word[translation]:
        return(True)

def quitGame(userInput):
    if userInput == 'q':
        return(True)
    else:
        return(False)
    
