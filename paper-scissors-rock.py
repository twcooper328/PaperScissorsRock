import random
import time
import os

#These are the funtions for the game.

clear = lambda: os.system('cls')


def stars(string):
    #prints a border of stars above and below text
    print("*********************************")
    print(string)
    print("*********************************\n")
    
def game_over(string):
    #a game over screen - for when you run out of money
    clear()
    name = string
    stars("        -THE GAME IS OVER-")  
    print("You have run out of money, " + str(name))
    print("\n")
    print("""Close this window to try again
    
    
    
    
    """) 
    time.sleep( 5 )
 
    
    #closed text files
    paper.close() 
    rock.close() 
    scissor.close()  

def tutorial(string):
    #tutorial screen
    name = string

    stars("          TUTORIAL")
    
    print("Rock beats Scissors\n")
        
    print("Scissors beats Paper\n")
        
    print("Paper beats Rock\n")

    print("When you run out of money, you lose!\n") 

    print("-entries are not case sensitive-")
    
    stars("ENTER 'p' TO ADVANCE MENUS QUICKLY")
    
    choice = input("Please type your choice here: ")
    
    real_choice = str(choice).lower()
    
    if str(real_choice) == "back" or str(real_choice) == "p":
        clear()
        return main_menu(name)
    else:
        clear()
        return tutorial(name)

def main_menu(string):
    #main menue screen
    
    name = string
    mnu = True 
    while mnu == True:
    
        stars("            MAIN MENU")
        print("Welcome " + name + "!\n")
        print("From here, you may either select:\n")
        print("play - Enter the arena!\n")
        print("tutorial - Learn the ropes!\n") 
        print("-entries are not case sensitive-")
        stars("PLEASE ENTER 'PLAY' OR 'TUTORIAL'")

        choice = input("Please type your choice here: ")
        real_choice = str(choice).lower()

        if str(real_choice) == "play" or str(real_choice) == "p":
            clear()
            return 

        elif str(real_choice) == "tutorial" or str(real_choice) == "tut":
            clear()
            return tutorial(name)
            
        else:
            clear()
            return main_menu(name)

def hand(int):
    #file based hand animation 
    y = int

    if i == 1:
        print("              PAPER!!!")
        print(paper)
        print("\n")
        y += 1
        return y

    elif i == 2:
        print("            SCISSORS!!!")
        print(scissor)
        print("\n")
        y += 1
        return y

    else:
        print("              ROCK!!!")
        print(rock)
        print("\n")
        return 1

def money_screen(string, int):
    #betting screen
    coins = int
    name = string

    if coins == 0:
        return game_over(name)
    # money screen intro animation
    stars("      HERE IS YOUR MONEY")
    print("You currently have: ")
    time.sleep( 1 )
    clear()

    stars("      HERE IS YOUR MONEY")
    print("You currently have: " + str(coins) + " coins")
    time.sleep( 1 )
    clear()

    x = 0
    coins = int
    bet = 10
    pool = coins - bet
    upper_limit = False
    lower_limit = False
    all_bet = False

    while x == 0:

        stars("      HERE IS YOUR MONEY")
        print("You currently have: " + str(coins) + " coins")
        print("\nAdjust your bet by entering:\n")
        print("more - Bet more!")
        print("less - Bet less?")
        print("all - Go ALL IN!!!")
        stars("    CHOOSE AN AMOUNT TO BET")

        #warning text for betting limits - if too low or too high
        
        if upper_limit == True:
            print(" --Insufficient funds to cover bet--")
            upper_limit = False
        elif all_bet == True:
            print(" --We are going ALL IN!!!--")
            all_bet = False
        elif lower_limit == True:
            print(" --The bet must be at least 10 coins--")
            lower_limit = False
        else:
            print(" --The minimum bet is 10 coins--")
      
        pool = coins - bet
        print(str(name) + "'s coins: " + str(pool))
        print(str(name) + "'s   bet: " + str(bet))
        
        stars("ENTER 'MORE' 'LESS' OR 'PLAY'")

        choice = input("Please type your choice here: ")
        coin_choice = str(choice).lower() 

        if str(coin_choice) == "play" or str(coin_choice) == "p":
            clear()
            return bet
        elif str(coin_choice) == "more":
            if pool >= 10:
                bet += 10
                clear()
                continue
            else:
                upper_limit = True
                clear()
                continue
        elif str(coin_choice) == "less":
            if bet == 10:
                lower_limit = True
                all_bet = False
                clear()
                continue
            else:
                bet -= 10
                clear()
                continue
        elif str(coin_choice) == "all":
            bet = coins
            all_bet = True
            clear()
            continue
        else:
            clear()
            continue

def selection_screen(string, int):
    name = string
    bet = int
    #hand = 3
    hand = random.randint(1, 3)

    
    z = 0
    while z == 0:
        stars("CURRENT BET: " + str(bet) + " - MAKE YOUR CHOICE")
        if hand == 1:
            print("       SELECTED: PAPER")
            print(paper)
            print("\n")
            
            
        elif hand == 2:
            print("       SELECTED: SCISSORS")
            print(scissor)
            print("\n")
            
        else:
            print("       SELECTED: ROCK!!!")
            print(rock)
            print("\n")


        print("Make your selection: \n")
        print("Rock: 'r' - Paper: 'a' - Scissors: 's'\n")
        stars("SELECT YOU HAND - 'PLAY' TO CONTINUE")

        choice = input("Please type your choice here: ")
        real_choice = str(choice).lower() 

        if str(real_choice) == "play" or str(real_choice) == "p":
            clear()
            if hand == 3:
                return 0
            elif hand == 1:
                return 4
            else:
                return 2
            return
        
        elif str(real_choice) == "rock" or str(real_choice) == "r":
            hand = 3
            clear()
            continue
        elif str(real_choice) == "paper" or str(real_choice) == "a":
            hand = 1
            clear()
            continue
        elif str(real_choice) == "scissors" or str(real_choice) == "s":
            hand = 2
            clear()
            continue
        else:
            clear()
            continue
     
def battle_screen (money, num, int, string):
    #battle screen: runs the showdowns

    coin = money
    name = string
    bet = num
    hand = int
    
    q = 0
    while q <= 1:
        #ready set go screen - wind up before results screen
        stars(str(name)+ "'s ZONE")
        print("\n")
        if q == 0:
            print("             READY")
        elif q == 1:
            print("              SET")
        print("\n\n")
        stars(" ")
        print("\n")
        if q == 0:
            print("             READY")
        elif q == 1:
            print("              SET")
            #q = 100
        print("\n\n")
        stars("OPPONENTS'S ZONE")
        time.sleep( 1 )
        q += 1
        
        clear()
    #enemy hand: 1 - rock| 2 - scissors| 3 - paper    
    enemy = random.randint(1, 3)
    if enemy == 1:
        enemy = 0
    elif enemy == 3:
        enemy = 4
    
    if hand == enemy:
        phrase_1 = "        THERE WAS A TIE!"
        phrase_2 = " YOUR " + str(bet) + " COINS WERE RETURNED"
        battle = "tie"
        
    elif (hand == 4 and enemy == 2) or (hand == 2 and enemy == 0) or (hand == 0 and enemy == 4):
        phrase_1 = "          YOU LOST"
        phrase_2 = "    BETTER LUCK NEXT TIME!"
        battle = "lost"
    else:
        phrase_1 = "          YOU WON!!!"
        phrase_2 ="      YOU WON " + str(bet) + " COINS!"
        battle = "won"

    q = 0
    clear()
    while q == 0:
        #results screen: Tells you if you won or lost
        stars(phrase_1)
        if hand == 4:
            print(paper)
        elif hand == 2:
            print(scissor)
        else:
            print(rock)

        stars(phrase_2)
        if enemy == 4:
            print(paper)
        elif enemy == 2:
            print(scissor)
        else:
            print(rock)
            
        stars("OPPONENTS'S ZONE")

        time.sleep( 1 )
        remaining = coin - bet

        if remaining <= 0 and battle == "lost":
            return game_over(name)

        choice = input("Please type 'play' to go again: ")
        real_choice = str(choice).lower() 
        if str(real_choice) == "play" or str(real_choice) == "p":
            clear()
            if battle == "won":
                return 1
            elif battle == "tie":
                return 0
            else:
                return -1
        else:
            clear()
            continue
        #time.sleep( 5 )
        clear()


#The rock paper scissors are text files. They are loaded here.
'''
folder = os.path.dirname(os.path.abspath(__file__))
paper_path = os.path.join(folder, 'paper.txt')

folder = os.path.dirname(os.path.abspath(__file__))
rock_path = os.path.join(folder, 'rock.txt')

folder = os.path.dirname(os.path.abspath(__file__))
scissor_path = os.path.join(folder, 'scissors.txt')
'''

with open('rock.txt', 'r') as f:
    rock = f.read()

with open('paper.txt', 'r') as f:
    paper = f.read()

with open('scissor.txt', 'r') as f:
    scissor = f.read()




#The game begins with a short message that shows my name
clear()

stars("Thomas Cooper    ICSTARS:C47")

time.sleep( 2 )

#hand animations for the opening
i = random.randint(1, 3)

clear()

x = 0
while x < 6:
    
    stars(" ")
    
    i = hand(i)
    stars(" ")
     
    time.sleep( .35 )
    x += 1
    clear()

stars("WELCOME TO PAPER, SCISSORS, ROCK!")   

if i < 3:
    i += 1
else:
    i = 1

hand(i)
 
stars("  PREPARE YOUR HAND FOR BATTLE!")

player_name = input("Please enter your name: ")
clear()

#The main menu is called here
main_menu(player_name)

clear()

coin = 100

#The main game loop. Betting screen > hand selection > battle screen
q = True
while q == True:

    round_bet = money_screen(player_name, coin)

    sel_hand = selection_screen(player_name, round_bet)

    outcome = battle_screen(coin, round_bet, sel_hand, player_name)

    if outcome == 1:
        coin += round_bet
    elif outcome == -1:
        coin -= round_bet
