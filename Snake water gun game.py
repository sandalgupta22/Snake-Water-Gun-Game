import random
import time
from termcolor import colored, cprint
from pygame import mixer

def snake():
    mixer.init()
    mixer.music.load('D:\\snake.mp3')
    mixer.music.set_volume(0.5)
    mixer.music.play()

def win():
    mixer.music.load('D:\\win.mp3')
    mixer.music.set_volume(0.2)
    mixer.music.play()

def lose():
    mixer.music.load('D:\\lose.mp3')
    mixer.music.set_volume(0.2)
    mixer.music.play()

snake()

cprint(' \t \t \t \t \t \t \t \t \t \t \t SNAKE, WATER, GUN GAME\t \t \t \t \t \t \t \t \t \t \t','cyan', 'on_grey', attrs=['bold','dark','concealed'])

k=10
print("\t\t\t\nWelcome to the game.....\n ")
print(" PRESS\n s for snake\n w for water \n g for gun\n")
print("You have",k," chances \n")


i=1
j=1
userscore=0
compscore=0
tie=0


while(i<=10):
    snake()
    u = str(input("Choose your choice :  "))
    lst = ["snake", "water", "gun"]
    comp = random.choice(lst)



    if (u=='s') and (comp=="snake"):
        print("\nYou and Computer choose the same option\n")
        cprint('\t\t \t \t \t \t \t \t \t \t \t \tRESULT : The Match is Tied\t\t\t \t \t \t \t \t \t \t \t\n','yellow', 'on_cyan',attrs=['bold','dark','concealed'])
        tie=tie+1
        i=i+1

    elif (u=='w') and (comp=="snake"):
        print("\nOOPS....Snake drank the water...\n")
        cprint('\t\t \t \t \t \t \t \t \t \t \t \tRESULT : You Lost Computer Win\t\t\t \t \t \t \t \t \t \t \t\n', 'yellow',
               'on_cyan', attrs=['bold', 'dark', 'concealed'])
        compscore=compscore+1
        i=i+1
        lose()
        time.sleep(2)

    elif (u == 'g') and (comp == "snake"):
        print("\nSnake was killed by gun...\n")
        cprint('\t\t \t \t \t \t \t \t \t \t \t \tRESULT : You Won Computer lost\t\t\t \t \t \t \t \t \t \t \t\n', 'yellow',
               'on_cyan', attrs=['bold', 'dark', 'concealed'])
        userscore=userscore+1
        i=i+1
        win()
        time.sleep(2)

    elif (u == 's') and (comp == "water"):
        print("\nSnake drank the water...\n")
        cprint('\t\t \t \t \t \t \t \t \t \t \t \tRESULT : You Won Computer Lost\t\t\t \t \t \t \t \t \t \t \t\n', 'yellow',
               'on_cyan', attrs=['bold', 'dark', 'concealed'])
        userscore=userscore+1
        i=i+1
        win()
        time.sleep(2)

    elif (u == 'w') and (comp == "water"):
        print("\nYou and Computer choose the same option \n")
        cprint('\t\t \t \t \t \t \t \t \t \t \t \tRESULT : The Match is Tied\t\t\t \t \t \t \t \t \t \t \t\n', 'yellow',
               'on_cyan', attrs=['bold', 'dark', 'concealed'])
        tie=tie+1
        i=i+1


    elif (u == 'g') and (comp == "water"):
        print("\nOOPS....Gun drowned in water....\n")
        cprint('\t\t \t \t \t \t \t \t \t \t \t \tRESULT : You Lost Computer Won\t\t\t \t \t \t \t \t \t \t \t\n', 'yellow',
               'on_cyan', attrs=['bold', 'dark', 'concealed'])
        compscore=compscore+1
        i=i+1
        lose()
        time.sleep(2)

    elif (u == 's') and (comp == "gun"):
        print("\nOOPS...Snake was killed by gun...\n")
        cprint('\t\t \t \t \t \t \t \t \t \t \t \tRESULT : You Lost Computer Won\t\t\t \t \t \t \t \t \t \t \t\n', 'yellow',
               'on_cyan', attrs=['bold', 'dark', 'concealed'])
        compscore=compscore+1
        i=i+1
        lose()
        time.sleep(2)

    elif (u == 'w') and (comp == "gun"):
        print("\nGun drowned in water...\n")
        cprint('\t\t \t \t \t \t \t \t \t \t \t \tRESULT : You Won Computer Lost\t\t\t \t \t \t \t \t \t \t \t\n', 'yellow',
               'on_cyan', attrs=['bold', 'dark', 'concealed'])
        userscore=userscore+1
        i=i+1
        win()
        time.sleep(2)

    elif (u == 'g') and (comp == "gun"):
        print("\nYou and Computer choose the same option \n")
        cprint('\t\t \t \t \t \t \t \t \t \t \t \tRESULT : The Match is Tied\t\t\t \t \t \t \t \t \t \t \t\n', 'yellow',
               'on_cyan', attrs=['bold', 'dark', 'concealed'])
        tie=tie+1
        i=i+1

    elif (u!='s') and (u!='g') and (u!='w'):

        cprint('\t\t \t \t \t \t \t \t \t \t \t \t Wrong Input\t\t\t \t \t \t \t \t \t \t \t\n', 'yellow',
               'on_cyan', attrs=['bold', 'dark', 'concealed'])
        i=i+1

    k=k-1
    print("you have", k, " chances left\n")



while(j==1):
    print("\nNo. of times user won : ",userscore)
    print("No. of times computer won : ",compscore )
    print("No. of times tied : ",tie )

    if(userscore>compscore):
        print("\n")
        cprint("\t \t \t \t \t \t \t \t \t \t \t******** USER WONNNNN THE GAME ********\t \t \t \t \t \t \t \t \t \t \t",'cyan', 'on_grey',attrs=['bold','dark','concealed'])
    elif(userscore<compscore):
        print("\n")
        cprint("\t \t \t \t \t \t \t \t \t \t \t******** COMPUTER WONNNNN THE GAME ********\t \t \t \t \t \t \t \t \t \t \t",'cyan', 'on_grey',attrs=['bold','dark','concealed'])
    elif(userscore==compscore) and (userscore<=tie) and (compscore<=tie):
        print("\n")
        cprint("\t \t \t \t \t \t \t \t \t \t \t******** THE GAME IS TIED ********\t \t \t \t \t \t \t \t \t \t \t",'cyan', 'on_grey',attrs=['bold','dark','concealed'])
    break






