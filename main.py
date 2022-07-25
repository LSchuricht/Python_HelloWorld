import random


def dice():
    com = random.choice(["Sissor","Paper","Rock"])
    user_input = input("Please Write Sissor:\n")

    if user_input == "Sissor" and com == "Sissor": printmessage("draw")
    elif user_input == "Sissor" and com == "Paper": printmessage("win")
    elif user_input == "Sissor" and com == "Rock": printmessage("lost")
    else: printmessage("you wrote sth wrong")

def printmessage(msg):
    if msg == "draw":
        print("its a draw")
    elif msg == "win":
        print("its a win")
    elif msg == "lost": 
        print("it a lost")
    else: print(msg)    



dice()