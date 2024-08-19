import random
import os
from time import sleep

#give information about game to the user
def gameInfo():

    print("\n\n----------------INTRODUCTION----------------")
    print("welcome to the one of the most known and belowed games.")
    print("ROCK SCISSORS AND PAPERS!!!!")
    print("---------------RULES----------------")
    print("the game will be 3 rounds an whoever wins the 2 rounds will be a winner.")
    print("if it is tie, round is not counted")
    print("type exit to be out of the game\n")

def roundInfo(game_num,tour_num,answer,computers_choice,result,player_rounds,pc_rounds):
    print("\n----------------------------------------------")
    print(f"---GAME{game_num}---",f"---TOUR{tour_num}---")
    print("gamer: ",answer," pc: ",computers_choice)
    print(result)
    print("gamer: ",player_rounds," computer: ",pc_rounds)
    print("----------------------------------------------\n")


def rock_scissors_papers_HediyeSila_Ozyurt(): 

    gameInfo()

    #number of the games, played by computer and gamer
    game_num=0
        
    game_list=["rock","scissors","paper","exit"]
    accurate_combinations={"rock":"scissors",
                           "scissors":"paper",
                           "paper":"rock"}
    

    #winner of the each game will be recorded 
    winners=[]

    #loop for games
    while(True):

        #number of the games, played by computer and gamer
        game_num+=1
        
        #number of the round in a game
        tour_num=1

        player_rounds=0
        pc_rounds=0

        #loop for rounds
        while(True): 
           
            answer=input("Rock,Scissors,Paper or Exit?: ").lower()

            if answer=="exit":

                #print winners of each game
                if winners:
                    print("\nWinners List")
                    for i in winners:
                        print(i)
                else:
                    print("no game played")
                return

            if answer not in game_list:
                print("Invalid input. Please choose Rock, Scissors, Paper, or Exit.")
                continue


            #take an answer from the pc excluding exit
            computers_choice=random.choice(game_list[:-1])
            
            if answer==computers_choice:

                result="IT S A TIE"
                roundInfo(game_num,tour_num,answer,computers_choice,result,player_rounds,pc_rounds)
   
            elif computers_choice in accurate_combinations.get(answer,""):

                result="YOU WON THIS ROUND"
                player_rounds+=1
                roundInfo(game_num,tour_num,answer,computers_choice,result,player_rounds,pc_rounds)
                
            else:
                
                result="HAHAHAH I WON THIS TIME"
                pc_rounds+=1
                roundInfo(game_num,tour_num,answer,computers_choice,result,player_rounds,pc_rounds)
                

            #check if there is a winner
            if player_rounds==2 or pc_rounds==2:

                winner="gamer" if player_rounds==2 else "computer"

                print(winner,"won the game. Congratulations!!!!")
                winners.append(f"GAME{game_num},{tour_num} round is playyed, {winner} is the winner")

                #ask both of them if they like to play again
                choices=["yes","no"]
                users_answ=input("Would you like to play again?\nyes or no: ").lower()
                pc_answ=random.choice(choices)
                if users_answ=="no":
                    #print winners of each game
                    if winners:
                        print("\nWinners List")
                        for i in winners:
                            print(i)    
                    return
                elif pc_answ=="no":
                    print("computer doesn't like to play again :'(")

                    #print winners of each game
                    if winners:
                        print("\nWinners List")
                        for i in winners:
                            print(i)    
                    return
                
                else:
                    break
               

            tour_num+=1
            
        #for a new game clear the console
        print("\n\nnew game will start in seconds")
        sleep(7)
        os.system('cls' if os.name=='nt' else 'clear')
        
         
rock_scissors_papers_HediyeSila_Ozyurt()
