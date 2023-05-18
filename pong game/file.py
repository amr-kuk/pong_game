print("**************************")
print("*****NUMBER GUESSING******")
print("********** GAME *********")
print("**************************")
from random import randint
ans=randint(0,25)
print("enter the number below 25\n")
def easy_mode():
    while True:
        try:
            usr=int(input(">:"))
            if ans==usr:
                print("\nyou won the game")
                break
            elif ans<usr:
                print("you enter bigger value")
            elif ans>usr:
                print("you enter smaller value")
        except ValueError:
            print("!!!!!enter number!!!!!")
def hard_mode():
    print("you have only five chances")
    tries=0
    while tries<5:
        try:
            usr=int(input(">:"))
            if ans==usr:
                print("you won")
                break
            elif ans<usr:
                print("you enter bigger value")
                tries+=1
                if tries==5:
                    print("chance over")
                else :
                    print("try again")
            elif ans>usr:
                print("you enter smaller value")
                tries+=1
                if tries==5:
                    print("chance over")
                else :
                    print("try again")
        except ValueError:
            print("!!!!enter num!!!")
def pre_game():
    num=int(input("enter 1 for easy mode,enter 2 for hard mode\n"))
    if num==1:
        easy_mode()
    elif num==2:
        hard_mode()
    else:
        print("plz choose 1 or 2 num")
        pre_game()
        
pre_game()

        

    
