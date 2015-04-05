from playFunctions import playWord, pullWords, answerCheck, quitGame
import addWord

def learnWords():
    '''Pulls together multiple functions to create a learning words game
'''
    print('press q anytime to quit')
    userInput = None
    while userInput != 1 and userInput != 2 and userInput != 'q':
        userInput = input("""press 1 to play and 2 to add a word (or q to quit, it works anytime!) \n""")
        if userInput == '1' or userInput == '2':
            userInput = int(userInput)
            
    if userInput == 1:

        #ask language to play in
        while userInput != 'dutch' and userInput != 'english':
            userInput = input("""Would you like to be given dutch or english words?\n""")
            language = userInput

       #ask type of word to play with     
        while userInput != 'verbs' and userInput !='nouns' and userInput !='connectives':
            #need to create an all or random option
            userInput = input("""Which type of words would you like to practice? Type verbs, nouns or connectives \n""")
            userQuit = quitGame(userInput)
            if userQuit == True:
                break

        if userQuit == False:
            words = pullWords(userInput)

            for word in words:
                print('*'*30)
                print(playWord(word, language))
                
    elif userInput == 2:
        addWord.addNewWord()
        
    else:
        print('Bye then')
        
learnWords()
