from WordLearningV2 import quitGame, pullWords

def learnWords():
    '''Pulls together multiple functions to create a learning words game
'''
    print('press q anytime to quit')
    userInput = None
    while userInput != 1 and userInput != 2 and userInput != 'q':
        userInput = input('press 1 to play and 2 to add a word (or q to quit, it works anytime!)')
        print(userInput)
        if userInput == '1' or userInput == '2':
            userInput = int(userInput)
    if userInput == 1:
        #play
        while userInput != 'verbs' and userInput !='nouns' and userInput !='connectives':
            #need to create an all or random option
            if quitGame(userInput):
                print('herhe')
                break
            userInput = input("""Which type of words would you like to practice? Type verbs
, nouns or connectives""")

        words = pullWords(userInput)

        for word in words:
            print(word)
    elif userInput == 2:
        #add word
        print('not ready')
    else:
        print('Bye then')
learnWords()
