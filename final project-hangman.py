#import the random fuction for hangman
import random

#list for all the question that player did before
#It is used for varifing whether random words are duplicated or not
list_question=[] #only used in single mode

#function of drawing hangman
#count=how many times player did wrong guess
def hangman_image(count):
    if count==0:
        print("   ____\n"
              "  |    | \n"
              "  |    | \n"
              "  |     \n"
              "  |    \n"
              "  |    \n"
              "__|____", end=("\t\t"))        
    elif count==1:
        print("   ____\n"
              "  |    | \n"
              "  |    | \n"
              "  |    O \n"
              "  |    \n"
              "  |   \n"
              "__|____", end=("\t\t"))        
    elif count==2:
        print("   ____\n"
              "  |    | \n"
              "  |    | \n"
              "  |    O \n"
              "  |    | \n"
              "  |    \n"
              "__|____", end=("\t\t"))        
    elif count==3:
        print("   ____\n"
              "  |    | \n"
              "  |    | \n"
              "  |    O \n"
              "  |   /| \n"
              "  |    \n"
              "__|____", end=("\t\t"))        
    elif count==4:
        print("   ____\n"
              "  |    | \n"
              "  |    | \n"
              "  |    O \n"
              "  |   /|\\ \n"
              "  |    \n"
              "__|____", end=("\t\t"))       
    elif count==5:
        print("   ____\n"
              "  |    | \n"
              "  |    | \n"
              "  |    O \n"
              "  |   /|\\ \n"
              "  |   /  \n"
              "__|____", end=("\t\t"))       
 
#validation for input value except for the guessing spelling part
def input_validation (input_value, comparision):
    while input_value!=comparision:
        for i in range (len(comparision)):
            if input_value==comparision[i]:
                return input_value        
        print("\nInvalid input! You have to input",comparision)
        input_value=input("Please try again: ")
    return input_value

#fuction for guessing spelling part(both double and single mode)
def hangman(question, question_correct, topic):
    score_correct=0
    score_wrong=0
    count=0
    #'count_for_support': position to put guess in question_correct_support
    count_for_support=[]
    guess="_"
    
    list_alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                   'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    list_guess=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    
    #loop for completing each question
    while count!=6 and question!=question_correct:
    #To indicate how many times player play
    #varify correct input or not to put in the list, question_correct_support
        if question_correct_support!=question_correct:
            for i in range (len(count_for_support)):
                question_correct_support[count_for_support[i]]=guess
        
        #print right hangman shape
        print("\ntopic:", topic)
        
        #called fuction
        hangman_image(count)
        #shows how many alphabet for the question question
        #print what player input and either right or not
        for i in range (len(question_correct)):
            print(question_correct[i], end=(' '))        
        print("\n\n")
        
        #printing the alphabet that player didn't input
        for i in range (len(list_alphabet)):
            print(list_alphabet[i], end=(" "))
        print()
        
        #printing the alphabet that player already guess
        #below the alphabet that player didn't guess yet
        for i in range (len(list_guess)):
            print(list_guess[i], end=(" "))
            
        #ask player to input the alphbet
        guess=input("\n\nGuess the alphabet for the word\n"
                    "(Please write only in lower case): ")
        
        #validation for right input(guessing the spelling of the word)
        is_duplicated = True
        while is_duplicated:
            count_is_duplicated=0
            
            #varify that player input one alphabet per time
            if len(guess)>1:
                guess=input("\nYou have to input one alphabet per try."
                            "\nTry again: ")
                continue
            
            #make sure player didn't input anything
            elif guess=="" or guess==" ":
                guess=input("\nYou have to input alphabet. Try again: ")
                count_is_duplicated=count_is_duplicated+1
                continue
            
            #make sure player input the same alphabet more than once
            for i in range (len(list_guess)):
                if list_guess[i]==guess:
                    guess=input("\nYou already input that alphabet. Try again: ")
                    count_is_duplicated=count_is_duplicated+1
            
            #if input value is not applied to those three condition, leave the while loop
            if count_is_duplicated==0:
                is_duplicated=False
                
        #add the alphabet that player already input
        list_question.append(guess)
        
        #remove the input alphabet from the list of alphabet 
        #that player didn't input yet
        for i in range (len(list_alphabet)):
            if list_alphabet[i]==guess:
                list_alphabet[i]=" "
                list_guess[i]=guess
                
        #initialize count_for_support                
        count_for_support=[]
        #varify correct input or not to put in the list, question_correct
        for i in range (len(question)):        
            if question[i]==guess:
                question_correct[i]=guess
                count_for_support.append(i)
                score_correct=score_correct+1
        #announce incorrect input
        if question_correct_support==question_correct:
            print ("\nYour guess is incorrect!")
            score_wrong=score_wrong+1
            count=count+1
    
    #if player lose the game(wrong guess for 6 times)
    if count==6:
        print("   ____\n"
              "  |    | \n"
              "  |    | \n"
              "  |    O \n"
              "  |   /|\\ \n"
              "  |   / \\ \n"
              "__|____\n"
              "Game Over")
    
    else:
        #called 'hangman_image' fuction to print right hangman shape
        hangman_image(count)
    
    #list for the variable that is needed from outside of fuction
    count_score_list=[]
    count_score_list.append(count)
    count_score_list.append(score_correct)
    count_score_list.append(score_wrong)
    #count_score_list=[count, score_correct, score_wrong]
    return count_score_list

#comparision for right input(validation)
comparision_another_game=["quit", "q", "another mode", "a", "new game", "ng"]
comparision_y_n=["yes", "y", "no", "n"]
another_game="a"

#loop if player wants to change the mode
while another_game=="another mode" or another_game=="a":
    game_mode=input("Choose the mode that you want to play"
                    "\n(single(s)/double(d)): ")

    #comparision for right input(validation)
    comparision_game_mode=['single', 's', 'double', 'd']
    
    #called validation function
    game_mode=input_validation(game_mode, comparision_game_mode)
    
    another_game="ng"
    
    #varify the mode that player wants to play
    if game_mode=="double" or game_mode=="d":
        #loop for the new game if player wants(initialize the score)
        while another_game=="ng" or another_game=="n":
            
            #print the rule for players
            print("\nRule: two player will choose the question for each other's hangman word.\n"
                  "1 score for 1 question.\n"
                  "It doesn't matter how many you got wrong unless you don't make hangman\n"
                  "The one that has higher score will win!")
            
            another_game="yes"
            #scores for double mode
            score_player1=0
            score_player2=0
            
            #varify whether player don't want to play another game
            while another_game!="no" and another_game!="n":
                
                #choose the role for player 1
                #it will effect the score
                player1=input("\nFor player 1, choose the roll that you want to do"
                              "\n(questioner(q)/guesser(g)): ")

                #comparision for validation
                comparision_player1=['questioner', 'q', 'guesser', 'g']
                #called validation function
                player1=input_validation(player1, comparision_player1)
                
                #automatically choose the role for player 2 depends on player1's role
                if player1=="questioner" or player1=='q':
                    player2="guesser"
                    print("Then player 2 is", player2)
                    topic=input("\nInput the topic of your word: ")
                    question=list(input("Enter the word for the question: "))
                    #"\n": to make sure another player doesn't see
                    #the answer that one player input
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          "Now, player 2, guess the word!")
                    
                else:
                    player2="questioner"
                    print("Then player 2 is", player2)
                    topic=input("\nInput the topic of your word: ")
                    question=list(input("\nEnter the word for the question: "))
                    #"\n": to make sure another player doesn't see
                    #the answer that one player input
                    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          "Now, player 1, guess the word!")

                #compare and store the alphabet that player guess and right
                question_correct=[]
                #to varify that player input wrong guess(alphabet)
                question_correct_support=[]
                
                #append amount of '_' same with the question
                for i in range (len(question)):
                    if question[i]!=" ":
                        question_correct.append("_")
                        question_correct_support.append("_")
                    #append blank if the question if formed with two word
                    else:
                        question_correct.append(" ")
                        question_correct_support.append(" ")

                #call hangman function
                count_score_list=hangman(question, question_correct, topic)

                #add the score to right player
                if player1=="questioner" or player1=="q":
                    if count_score_list[0]==6:
                        score_player1=score_player1+1
                    else:
                        score_player2=score_player2+1
                else:
                    if count_score_list[0]==6:
                        score_player2=score_player2+1
                    else:
                        score_player1=score_player1+1
                        
                #for printing the answer
                answer=""
                print("\nThe answer is '"+ answer.join(question)+"'.\n",
                      score_player1, "vs", score_player2)
                another_game=input("\nDo you want continue this game? (y/n): ")
                #called validation fuction
                another_game=input_validation(another_game, comparision_y_n)
            
            #print the final score of player don't want to continue the game
            print("\nFinal score is", score_player1, "for player 1 "
                  "\nand", score_player2, "for player 2")
            if score_player1<score_player2:
                print("So the winner is Player 2")
            elif score_player1==score_player2:
                print("So you draw the game")
            else:
                print("So the winner is Player 1")

            #ask player want a new game, another mode or leave(quit)
            another_game=input("\nnew game(ng)/another mode(a)/quit(q): ")
            #called validation fuction
            another_game=input_validation(another_game, comparision_another_game)

    #varify if player wants to play single mode
    if game_mode=="single" or game_mode=='s': 
        another_game="ng"
        
        #varify if the player wants to player new game with initialized score
        while another_game=="new game" or another_game=="ng":
            #count how many time that player play
            count_while=1
            #list of all the question word with different topic
            #list_question_topic=[animal, food, color, fruit]
            list_question_topic=[]
            #score in single mode
            score_single=0
            #list for all the question that player did before
            #It is used for varifing whether random words are duplicated or not
            list_question=[] 
            
            #list of question that is stored in the game(categorized with the topic)
            animal=[list('bear'), list('rabbit'), list('tiger'), list('elephant'),
                    list('canada goose'), list('kangaroo'), list('giraff'),
                    list('puppy'), list('squirrel'), list('hummingbird')]
            food=[list('bread'), list('cake'), list('spagetti'), list('pizza'),
                  list('french fries'), list('poutin'), list('ice cream'),
                  list('sandwich'), list('soup'), list('hot dog')]
            color=[list('red'), list('skyblue'), list('green'), list('brown'),
                   list('white'), list('black'), list('grey'),
                   list('purple'), list('pink'), list('yellow')]
            fruit=[list('orange'), list('apple'), list('banana'), list('grape'),
                   list('pineapple'), list('mango'), list('peach'),
                   list('blueberry'), list('strawberry'), list('lemon')]

            #append the question that is categorized with each topic)
            list_question_topic.append(animal)
            list_question_topic.append(food) 
            list_question_topic.append(color) 
            list_question_topic.append(fruit) 

            #printing the rule for player
            print("\nRule: You cannot play more than 40 questions\n"
                  "+2 point for right guess and -1 for wrong guess\n")

            #varify that player want to continue the game
            while another_game!="no" and another_game!="n":
                is_duplicate=True

                #varifing whether the question that randomly chose are repeated
                while is_duplicate:
                    count_is_duplicate=0
                    #varify the topic of question(that is randomly chose)
                    topic_question=random.choice(list_question_topic)
                    if topic_question==animal:
                        topic="animal"
                    elif topic_question==food:
                        topic="food"
                    elif topic_question==color:
                        topic="color"
                    else:
                        topic="fruit"

                    question_correct=[]
                    question_correct_support=[]

                    #choose the question randomly in the topic list that is randomly chose
                    question=random.choice(topic_question)
                    for i in range (len(list_question)):
                        if list_question[i]==question:
                            is_duplicate=True
                            count_is_duplicate=1
                    if count_is_duplicate==0:
                        is_duplicate=False

                for i in range (len(question)):        
                #append amount of '_' same with the question
                    if question[i]!= " ":
                        question_correct.append("_")
                        question_correct_support.append("_")
                    #append blank if the question if formed with two word
                    else:
                        question_correct.append(" ")
                        question_correct_support.append(" ")

                #list to varify the question is whehter duplicated or not
                list_question.append(question)
                #call hangman function
                count_score_list=hangman(question, question_correct, topic)
                score_single=score_single+count_score_list[1]*2-count_score_list[2]

                #if player fail to guess the question, the score become zero
                if count_score_list[0]==6:
                    score_single=0
                
                #to print the answer after the game for each question is over
                answer=""
                print("\nThe answer is '"+ answer.join(question)+
                      "'.\n\nYour total score is", score_single)
                
                #varify whether the question that is store in the game is all played or not
                if count_while==40:
                    print("\nYou finish all the words")
                    break
               
                #ask player whether wants to continue the game or not
                another_game=input("\nDo you want continue this game? (y/n): ")
                count_while=count_while+1
                #called validation function
                another_game=input_validation(another_game, comparision_y_n)

            #ask what player wants(new game, another mode, or leave)
            if count_while==40 or another_game=="n" or another_game=="no":
                another_game=input("\nnew game(ng))/another mode(a)/quit(q): ")
                #called validation function
                another_game=input_validation(another_game, comparision_another_game)

print ("\nbye bye")
