"""
I dont understand what super does.
Useful? --> http://www.artima.com/weblogs/viewpost.jsp?thread=236275

        while dutch == '':
            dutch = raw_input("Type the word in Dutch? \n")
        else:


difference between word.english and word.call_english. I often see people make a function to call the name of a variable rather than going straight to that var
"""
import json

def LearnWords(Words):
    for word in Words:
        play = input("Would you like to play? y or n\n")
        if play == 'y':
            english = input('What is the english for ' + str(word.translation_dutch()) + ' ? \n')
            if english == word.english:
                print('correct! the english for ' + str(word.translation_dutch()) + ' is ' + str(word.translation_english()))
                continue
            else:
                print('not quite')
                if context(word):
                    #prints word context sentence
                    context(word)
                    print
                    attempt = input('try again, whats the english for ' + str(word.dutch) + '\n')
                elif memTrick(word):
                    memTrick(word)
                    print
                    attempt = input('try again, whats the english for ' + str(word.dutch) + '\n')
                else:
                    attempt = input('try again, whats the english for ' + str(word.dutch) + '\n')

                if attempt == word.english:
                    print('correct! the english for ' + str(word.translation_dutch()) + ' is ' + str(word.translation_english()))
                else:
                    print('unlucky, the english for ' + str(word.dutch) + ' is: ' + str(word.translation_english()))                        
        else:
            print('Bye then')
            break

def pullWords(typeOfWord):
    '''returns ditctionary of words of type = typeOfWord
'''
    f = open('words.json')
    myWords = json.load(f)
    f.close()
    words = myWords['words'][0][typeOfWord]
    return(words)

def quitGame(userInput):
    if userInput == 'q':
        return(True)
    
def memTrick(word):
    if word.memTrick != '':
        print("heres your memory trick:")
        print(word.call_memTrick())

def context(word):
    if word.context != '':
        print("heres a context sentence:")
        print(word.call_context())
'''
def contextCheck(word):
    if context(word):
        
'''                        

def contextCheck(word):
    '''
checks for context, returns an attempt or False
should i return true if its right, false if its wrong and take next action
based on that?
    '''
    attempt = ''
    if context(word):
        context(word)
        print
        attempt = input('try again, whats the english for ' + str(word.dutch) + '\n')
    else:
        print('unlucky, the english for ' + str(word.dutch) + ' is: ' + str(word.translation_english()))   
        print('Maybe, a context sentence can help?')
        #change context
    return(attempt)

'''
def changeContext(word):

def changeMemTrick(word):
   ''' 
        
  

