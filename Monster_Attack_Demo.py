#!/usr/bin/env python
# coding: utf-8

# In[1]:

import random
import time


# In[2]:


# import starting values

player_look = ["\033[1m₍₍ ◝(・ω・)◟ ⁾⁾\033[0m"]
monster_look = ["\033[1m( •̀ω•́ )σ\033[0m", "\033[1m(ง •̀_•́)ง\033[0m", "\033[1mヽ༼ ಠ益ಠ ༽ﾉ\033[0m", "\033[1m（ ´థ౪థ）\033[0m", "\033[1m(=ↀωↀ=)\033[0m"]

player_lives = ["♡","♡","♡"]
player_attack_point = 10
run_number = 5
monster_attack_point = 0


# In[3]:


def start_the_game():
    print(f"""                                                                      ■    
 ■      ■                   ■                 ■■   ■   ■              ■    
 ■■    ■■                   ■                 ■■   ■   ■              ■    
 ■■    ■■  ■■■■  ■■■■  ■■■ ■■■■ ■■■   ■■■    ■ ■  ■■■■■■■■ ■■■   ■■■■ ■  ■ 
 ■ ■  ■ ■  ■  ■  ■  ■ ■■    ■   ■  ■  ■      ■  ■  ■   ■      ■  ■    ■ ■  
 ■ ■■ ■ ■ ■■   ■ ■  ■  ■■   ■  ■■■■■  ■     ■■  ■  ■   ■      ■ ■■    ■■   
 ■  ■■  ■ ■■   ■ ■  ■■   ■  ■  ■■     ■     ■■■■■■ ■   ■   ■■■■ ■■    ■ ■  
 ■   ■  ■  ■  ■  ■  ■■   ■  ■   ■     ■     ■    ■ ■   ■   ■  ■  ■    ■ ■■ 
 ■      ■  ■■■■  ■  ■■ ■■■  ■■■  ■■■  ■    ■     ■ ■■■ ■■■ ■■■■  ■■■  ■  ■ 
                         
                         Welcome to Monster Attack! 
    You will have ♡ ♡ ♡ lives to try and kill the monster.
    The monster’s attack will be a random value in a specific range.
    Your attack will be fixed and start at { player_attack_point }. 
    Each round your attack is higher than the monster’s, you’ll increase 
    your next round’s attack by the same amount of points that the previous 
    monster had. 
    The winning can be determined by probability and the attack points.
    When you lose, you’ll lose the round and lose one of your ♡ ♡ ♡  lives.""")
    
    print("\n")
    print(f"               This is you =  {player_look[0]}")  
    print(f"               This is a monster = {monster_look[0]}")

    player_will_play = ""
    while not (player_will_play.lower() == "yes" or player_will_play.lower() == "no"):
        player_will_play = input("               Do you want to play? Yes/No ")
    if player_will_play.lower().startswith("y"):
        return True    # want to play
    else:
        return False   # dont want to play


# In[4]:


def monster_power(player_attack_point):
    if player_attack_point <= 10:
        i  = random.randint(1, 31)
    elif player_attack_point <= 50:
        i = random.randint(20, 81)
    else:
        i = random.randint(30, 101)
    monster_attack_point = i
    
    # Commented out because monster seems too strong now
    #if monster_attack_point > 0.7*player_attack_point:
        #monster_attack_point += 0.01*player_attack_point
    return round(monster_attack_point)


# In[5]:


def winning_chance(player_attack_point, monster_attack_point):
    # This function controlls the Game Balance
    # Dertermine how high the possibility for you to win 
    # together with get_number function
    
    if monster_attack_point > player_attack_point:
        winning_percentage = round(((monster_attack_point - player_attack_point)*0.01+0.5),2)
        if get_number(winning_percentage) == (True):
            return "player_lose",  (1 - winning_percentage)
        # 1 minus because monster is more likely to win in this case
        else:
            return "player_win",  ( 1 - winning_percentage)
        
    elif monster_attack_point < player_attack_point:
        winning_percentage = round(((player_attack_point - monster_attack_point)*0.01),2)
        if get_number(winning_percentage) == (True):
            return "player_win",  winning_percentage
       
        else:
            return "player_lose",  winning_percentage
        
    else:  #tie
        winning_percentage = 0.5
        if get_number(winning_percentage) == (True):
                return "player_win", winning_percentage
        else:
            return "player_lose", winning_percentage


# In[6]:


def get_number (winning_percentage):        
    # work together with winning_chance function
    
    if random.random() <= winning_percentage:
        return True, 
    else:
        return False


# In[7]:


def make_monster(monster_attack_point):
    # change the moster face depends on its power
    
    if monster_attack_point < 20:
        this_round_monster = monster_look[0]
    elif monster_attack_point < 40:
        this_round_monster = monster_look[1]
    elif monster_attack_point < 60:
        this_round_monster = monster_look[2]
    elif monster_attack_point < 80:
        this_round_monster = monster_look[3]
    else:
        this_round_monster = monster_look[4]
    return this_round_monster


# In[8]:


def visual_make(player_lives, player_attack_point, player_look, monster_attack_point, this_round_monster, winning_percentage, endgame = False):
    
    just_heart=""   # Taking out only the hearts from the list
    for i in player_lives:
        for j in i:
            just_heart += " " + j + "  "
            
    print(just_heart)
    print("            ", player_attack_point, "                                  ", monster_attack_point)
    print ("    ", player_look[0], "                           ", this_round_monster) 
    
    if endgame == True:
        # if the game ends no need to see the winning possibility again
        pass
    else:
        print (f"             You have {round(winning_percentage*100)}% chance of killing the monster!")


# In[9]:


def check_running(run_number):
    # Check how many times you can run
    
    if run_number == 0:
        print("               You can't run anymore!!!!! Time to FIGHT!")
        time.sleep(2)
        return True  # no more run
    else:
        return False  # you can still run


# In[10]:


def player_choice(run_number):
    # asking player if he wants to run. 
    # should be only called when he still has the running point left.
    
    player_chose = ""
    while not (player_chose == "run" or player_chose == "fight"):
        player_chose = input("            Do you run or fight? ").lower()
    if player_chose == "run":
        print("               Escaping......")
        time.sleep(2)
        print ("              You have managed to run!")
        time.sleep(2)
        run_number -= 1
        return True, run_number  # True means he wants to run
    else: 
        print ("               You decided to fight!")
        time.sleep(2)
        return False, run_number #False means he wants to fight


# In[11]:


def fight(player_attack_point, monster_attack_point, player_lives, win_result):
    # player lose one live when he lost 
    # and he gets more atatck point if he won
    
    if win_result == "player_lose":
        player_lives.remove("♡")
        print("               You got injured......")
        time.sleep(2)
        
    elif win_result == "player_win":
        player_attack_point += monster_attack_point
        print("               You killed the monster!!")
        time.sleep(2)
        
    return player_lives, player_attack_point


# In[12]:


def check_end_game(player_lives, player_attack_point):
    # Checking the winning or losing condition.
    # Should be called after the each round.
    
    if player_lives == []:
        return "dead"
    elif player_attack_point >= 100:
        return "win"
    else: 
        return "continue game"


# In[13]:


def end_message(x):
    # will be called when winning or losing condition has fullfilled.
    
    if x == True:    # Player lost
        print("               Game over.....")
        time.sleep(3)
        
    else:            # Player won
        print("               Congratulations!")
        time.sleep(3)
    
    #Asking player if he wants replay
    player_will_play = ""  
    while not (player_will_play.lower() == "yes" or player_will_play.lower() == "no"):
        player_will_play = input("               Do you want to play again? Yes/No ")
    if player_will_play.lower().startswith("y"):
        return True    # want to play
    else:
        return False   # dont want to play


# In[14]:


def replay(answer):
    # Reset all the status to the original when game will replay
    
    if answer == True:  # Player wants replay
        player_lives = ["♡","♡","♡"]
        player_attack_point = 10
        run_number = 5
        monster_attack_point = 0
        return player_lives, player_attack_point, run_number, monster_attack_point 
    
    elif answer == False:# Player does not want replay
        pass 
        # print(" Ok! See you again someday soon. " )
        # time.sleep(2)


# In[15]:


def main(player_lives, player_attack_point, run_number, answer):
    
    # Below decides if this is a first game or replay.
    # we recieve answer from end_message function
    if answer == True:      
        # this is replay so no need to show the welcome message
        player_will_play = True
    else:
        # this is the first time he plays so need to welcome,
        # and ask him if he wants to play the game
        player_will_play = start_the_game()
        
    if player_will_play == True:   # he wants to play the game
        # checking if any ending game condition has fullfilled.
        while check_end_game(player_lives, player_attack_point) == "continue game":
        # ending condition has not been fullfilled.
        # Therefore starting the 1st round
            
            # Deciding the power of the moster
            monster_attack_point = monster_power(player_attack_point)
            
            # the outcome (win/lose) of the round will be determined here.
            # player_lose or player_win will be the win_result
            # Also recieving winning_percentage in order to pass it 
            # to the next visual_make function to show to the user.
            win_result, winning_percentage = winning_chance(player_attack_point, monster_attack_point)
            
            # Making the monster face according to the moster power
            this_round_monster = make_monster(monster_attack_point)
           
            # Visualizing on the screen
            visual_make(player_lives, player_attack_point, player_look, monster_attack_point, this_round_monster, winning_percentage, endgame = False)
            
            # Checking if he can still run
            no_more_run = check_running(run_number)
            if no_more_run == True:   #No more running
                print("               Fighting......")
                time.sleep(2)
                # change player_lives and player_attack_point
                player_lives, player_attack_point = fight(player_attack_point, monster_attack_point, player_lives, win_result)
            
            else:   # player can still run
                # get the answer whether he wants to run or not
                choice, run_number = player_choice(run_number)
                if choice == True: # Wants to run
                    # starting the second round
                    continue
                    
                else:  # Wants to fight!
                    print("               Fighting......")
                    time.sleep(2)
                    
                    # change player_lives and player_attack_point
                    player_lives, player_attack_point = fight(player_attack_point, monster_attack_point, player_lives, win_result)
                
                continue  # going back to the while loop for the next round.
                
        else: # end game condition has been fullfilled. no more round.
            # visualizing the last result of the game
            visual_make(player_lives, player_attack_point, player_look, monster_attack_point, this_round_monster, winning_percentage, endgame = True)            
            
            # checking why game ended
            if check_end_game(player_lives, player_attack_point) == "dead":
                answer = end_message(True) # will show Game Over
                
            else: # player won
                answer = end_message(False) # will show Congratulations
            
            # Asking if he wants replay
            if answer == True: # wants replay 
                 # resetting the number to the original number preparing 
                 # for replay
                player_lives, player_attack_point, run_number, monster_attack_point = replay(answer)
                
            # going back to the top of the main function 
            # but the answer is True so will not show welcome message
                main(player_lives, player_attack_point, run_number, answer)
                
            else: # player does not want replay
                print("               Ok! See you again someday soon. " )
                time.sleep(3)
                
    else: #Player does not want to play
        print("               Maybe next time!")


# In[ ]:


main(player_lives, player_attack_point, run_number, False)

