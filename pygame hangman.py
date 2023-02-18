#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 23:37:30 2020

@author: Hannah
"""

# Import a library of functions called 'pygame'
import pygame

#called 'random'
import random
 
# Initialize the game engine
pygame.init()

question=""
wrong=False
buttons=None

WHITE=  (255, 255, 255)
BLACK=  (  0,   0,   0)
RED=    (255,   0,   0)
ORANGE= (255,  94,   0)
YELLOW= (255, 228,   0)
GREEN=  (171, 242,   0)
SKYBLUE=(  0, 216, 255)
BLUE=   (  1,   0, 255)
PURPLE= ( 95,   0, 255)
PINK=   (255,   0, 221)

# Set the height and width of the screen
size  = [500,300]
screen= pygame.display.set_mode(size)
font= pygame.font.SysFont("consolas",20)
 
pygame.display.set_caption("Game Title")
  
#Loop until the user clicks the close button.
done = False
flag = None
clock= pygame.time.Clock()
score=0

is_print=False 
# print text function
def printText(msg, color='BLACK', pos=(50,50)):
    textSurface     = font.render(msg,True, pygame.Color(color),None)
    textRect        = textSurface.get_rect()
    textRect.topleft= pos
 
    screen.blit(textSurface, textRect)

question_txt=""

list_question_topic=[]    
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

list_question_topic.append(animal)
list_question_topic.append(food) 
list_question_topic.append(color) 
list_question_topic.append(fruit) 


question_correct=[]
question_correct_support=[]

while not done:
    # Main Event Loop
    for event in pygame.event.get():# User did something
        if event.type == pygame.KEYDOWN:# If user release what he pressed.
            pressed= pygame.key.get_pressed()
            buttons= [pygame.key.name(k) for k,v in enumerate(pressed) if v]
            flag= True
        elif event.type == pygame.KEYUP:# If user press any key.
             flag= False
        elif event.type == pygame.QUIT: # If user clicked close.
            done= True 
    if done:
        break                

    list_question=[]
    is_duplicate=True
    count=0

    answer=question

    #varifing whether the question that randomly chose are repeated
    while is_duplicate:
        count_is_duplicate=0
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

        question=random.choice(topic_question)
        for i in range (len(list_question)):
            if list_question[i]==question:
                is_duplicate=True
                count_is_duplicate=1
        if count_is_duplicate==0:
            is_duplicate=False
    
    for i in range (len(question)):        
        if question[i]!= " ":
            question_correct.append("")
            question_correct_support.append("")
        else:
            question_correct.append(" ")
            question_correct_support.append(" ")
    
    
    list_alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
                   'k','l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                   'u', 'v','w', 'x', 'y', 'z']
    list_alphabet_color=['BLACK','BLACK','BLACK','BLACK','BLACK','BLACK','BLACK','BLACK',
                         'BLACK','BLACK','BLACK','BLACK','BLACK','BLACK','BLACK','BLACK',
                         'BLACK','BLACK','BLACK','BLACK','BLACK','BLACK','BLACK','BLACK',
                         'BLACK','BLACK']
    

    question_txt=""
    guess=""
    
    #list for checking the input alphabet is whether duplicated or not
    list_guess=['return']
        
    #loop per question
    while count!=7:
        if question==question_correct:
            score=score+2
            print("question_correct=",question_correct)
            break
                
        #if the input alphabet is duplicated: True
        #if the input alphabet is not duplicated: False
        #change in line 226
        is_duplicate_alphabet=False
        
        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(10)
        
        # Main Event Loop
        for event in pygame.event.get():# User did something
            if event.type == pygame.KEYDOWN:# If user release what he pressed.
                pressed= pygame.key.get_pressed()
                buttons= [pygame.key.name(k) for k,v in enumerate(pressed) if v]
                flag= True
            elif event.type == pygame.KEYUP:# If user press any key.
                 flag= False
            elif event.type == pygame.QUIT: # If user clicked close.
                done= True 
        if done:
            break                

        # All drawing code happens after the for loop and but
        # inside the main while done==False loop.
          
        # Clear the screen and set the screen background
        screen.fill(WHITE)
         
        #print topic of the word(question)
        topic_txt="topic: "
        for i in range (len(list(topic))):
            topic_txt=topic_txt + "" + topic[i]
        printText(topic_txt, 'BLACK', (165, 100))
        
        #print answer after guess the question
        #it will the blank at the firt question
        answer_txt='answer(for question before): '
        for i in range (len(answer)):
            answer_txt=answer_txt+' '+answer[i]
        printText(answer_txt, 'BLACK', (165, 70))
        
        #print introduction
        printText("please press the enter if you lose or finish the game",
                  'BLACK', (165, 50))
        
        printText("score: ", 'BLACK', (25, 50))
        printText(str(score), 'BLACK', (80, 50))
        #draw gallows for hangman 
        pygame.draw.line(screen, BLACK, [25, 250], [75, 250], 3)
        pygame.draw.line(screen, BLACK, [45, 80], [45, 250], 3)
        pygame.draw.line(screen, BLACK, [45, 80], [75, 80], 3)
        pygame.draw.line(screen, BLACK, [75, 80], [75, 100], 3)
        
        #print how many alphabet does question has
        position_question_correct=170
        for i in range (len(question)):
            if question[i]!=" ":
                printText("_", 'BLACK', (position_question_correct, 135))
            position_question_correct=position_question_correct+20
       
        #check if the loop work more than one times
        press_execute=True
        
        
        #type(buttons[0])=str
        #when player press the keyboard
        if flag== True:
            press_execute=False
            if len(buttons)>0:
                guess=buttons[0]
                
            #checking the input alphabet is whether duplicated or not                
            for i in range (len(list_guess)):
                if list_guess[i]==guess:
                    is_duplicate_alphabet=True
            if is_duplicate_alphabet:
                continue
            
            list_guess.append(guess)
                        
            for i in range (len(question)):
                if guess==question[i]:
                    question_correct[i]=guess
                    count_support=0
            
            if question_correct==question_correct_support:
                count=count+1
            for i in range (len(question_correct)):
                question_correct_support[i]=question_correct[i]
        
        #after player press the keyboard(not pressing)
        elif flag== False:
            if guess=="":
                continue

            #print the guessed alphabet if it is right
            question_correct_position=170
            for i in range (len(question_correct)):
                printText(question_correct[i], 'BLACK', (question_correct_position, 130))
                question_correct_position=question_correct_position+20
        
            position_list_alphabet=75
            for i in range (len(list_alphabet)):            
                position_list_alphabet=position_list_alphabet+15
                if list_alphabet[i]==guess:
                    #put the right color for the alphabet
                    #not pressed:       black
                    #pressed but wrong: red
                    #pressed and right: blue
                    for j in range (len(question)):
                        if guess==question[j]:
                            list_alphabet_color[i]='BLUE'
                            
                        elif guess!=question[j]:
                            if list_alphabet_color[i]=='BLACK':
                                list_alphabet_color[i]='RED'                            

                printText(list_alphabet[i], list_alphabet_color[i], 
                          (position_list_alphabet, 240))
                                
            #print hangman for right timing(how many times that player got wrong)
            if count==1:
                #head
                pygame.draw.circle(screen, BLACK, [75, 120], 20, 3)
            if count==2:
                pygame.draw.circle(screen, BLACK, [75, 120], 20, 3)
                #body
                pygame.draw.line(screen, BLACK, [75, 140], [75, 190], 3)
            if count==3:
                pygame.draw.circle(screen, BLACK, [75, 120], 20, 3)
                pygame.draw.line(screen, BLACK, [75, 140], [75, 190], 3)
                #left arm
                pygame.draw.line(screen, BLACK, [55, 170], [75, 140], 3)
            if count==4:
                pygame.draw.circle(screen, BLACK, [75, 120], 20, 3)
                pygame.draw.line(screen, BLACK, [75, 140], [75, 190], 3)
                pygame.draw.line(screen, BLACK, [55, 170], [75, 140], 3)
                #right arm
                pygame.draw.line(screen, BLACK, [95, 170], [75, 140], 3)
            if count==5:
                pygame.draw.circle(screen, BLACK, [75, 120], 20, 3)
                pygame.draw.line(screen, BLACK, [75, 140], [75, 190], 3)
                pygame.draw.line(screen, BLACK, [55, 170], [75, 140], 3)
                pygame.draw.line(screen, BLACK, [95, 170], [75, 140], 3)
                #left leg
                pygame.draw.line(screen, BLACK, [55, 210], [75, 190], 3)
            if count==6:
                pygame.draw.circle(screen, BLACK, [75, 120], 20, 3)
                pygame.draw.line(screen, BLACK, [75, 140], [75, 190], 3)
                pygame.draw.line(screen, BLACK, [55, 170], [75, 140], 3)
                pygame.draw.line(screen, BLACK, [95, 170], [75, 140], 3)
                pygame.draw.line(screen, BLACK, [55, 210], [75, 190], 3)
                #right leg
                pygame.draw.line(screen, BLACK, [75, 190], [95, 210], 3)
                score=score-1
                break           
                
        if not press_execute:
            press_execute = True
        
        # if question==question_correct:
        #     score=score+2
        #     print("score=",score)
        #     print("question_correct=",question_correct)
        #     printText(answer_txt, 'BLACK', (165, 70))

        #     break

        pygame.display.flip()

    #guess=""
        
       
    
# Be IDLE friendly
pygame.quit()
