import time #import shizzle for the program to work
import random


def question(MedTypeQ,AskQuestion): #Checks whether to display a medical question or reaction question
    if (MedTypeQ==True): #Chooses to display a medical question
        MedQuestion()
    elif (MedTypeQ==False): #Chooses to display a reaction question
        ReactionQuestion("Please tap when the tile turns from blue to white")
        

def MedQuestion(): #Displays a medical question
    MedQBool=True
    ReactionQBool=False
    
    specifyKey=random.sample(list(MedicalQ),1) #Selects a random question from the dictionary
    print(specifyKey[0]) #Prints out the selected question
    
def ReactionQuestion(Reactquestion):     #Displays a reaction question
    ReactQBool=True
    MedQBool=False #Tells the program that the question being asked is reaction
    
    print (Reactquestion)                #In this function, tells the user the instruction
    time.sleep((randint(2,5))) #Makes the white tile appear randomly, sometimes its 2 seconds...
    #sometimes it can be 5 seconds instead, or any seconds between 2 and 5
    
    print("Tap now!") #Tells the user to tap!
    isTileWhite=True #Set to true to signify to the program that the tile is now white
    
    
def clickP1(userAnswer): #When Player 1 clicks on button, it comes to this function
    if (ReactQBool==True and isTileWhite==True): #If Reaction Q=T, then the only way..
        #the question condition can be fulfilled is if the tile was true when the player..
        #clicked
        player1_score +=1
    elif (ReactQBool==True and isTileWhite==False): #Player clicked too early
        player1_score -=1
    elif (MedQBool==True and  userAnswer==(MedicalQ.get(specifyKey[0]))):
        player1_score +=1 #Checks the user answer against the actual correct answer
    elif (MedQBool==True and  userAnswer!=(MedicalQ.get(specifyKey[0]))):
        player1_score -=1 #If the answer is incorrect, score is deducted by 1
        
def clickP2(userAnswer): #When Player 2 clicks on button, it comes to this function
    if (ReactQBool==True and isTileWhite==True):
        player2_score +=1
    elif (ReactQBool==True and isTileWhite==False):
        player2_score -=1
    elif (MedQBool==True and  userAnswer==(MedicalQ.get(specifyKey[0]))):
        player2_score +=1
    elif (MedQBool==True and  userAnswer!=(MedicalQ.get(specifyKey[0]))):
        player2_score -=1
        

#Program is set to flow in the following order:
        #1) Question function is called, for it to decide whether to run...
        #a reaction-type question or a medical-type question
        
        #2) Depending on the choice, one of the respective functions is run
        
        #3) In the respective function, it sets some booleans to true and some to false...
        #This is to signify to the program that the question has been displayed
        #This helps the program to differentiate between if player clicked early or not
        #i.e. (if player clicks on time, that means question boolean was true as it executed)
        #however, program detects the player as clicking early if boolean was set to false..
        #while they were clicking
        
        #4) IF the Question has been executed AND the conditions for the question is fulfilled...
        #then the player gets a point! If they selected a wrong answer, score - 1
        
        #5) Then you just loop as many times as you want for your questions
    
    
player1_score=0 #Stores score of player 1
player2_score=0;    #Stores score of player 2
AskQuestion=""     #Declares question variable
MedQBool=False      #Set to false because a medical question has not been asked yet
ReactQBool=False    #Set to false because a reaction question has not been asked yet

MedTypeQ=False  #Declares MedType as false
#This boolean variable is used to understand if  the question to be asked is a...
#Reaction question or a medical question

MedicalQ={"What is love":"Baby don't hurt me","But Wait there's more":"hey!","third time!":"go go"}
#A dictionary holding question and answer pairs, so its Question1:Answer1, Question2:Answer2
specifyKey="" #Variable used to hold the answer for validation later

isTileWhite=False #Checks whether the tile in Reaction questions has been set to white yet
#This is to verify if the player have clicked before its turned true/tile turned white
#Hence, allowing the program to deduct a score of 1 from the offending player



question(True,MedicalQ)



