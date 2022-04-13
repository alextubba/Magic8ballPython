import random

def Ask():
    question = input('Whats your question?')

    ran = random.randint(1,9)
    text = "Nice"

    if (ran == 1):
        text = "Yes - definitely"
    elif (ran == 2):
        text = "It is decidedly so"
    elif (ran == 3):
        text = "Without a doubt"
    elif (ran == 4):
        text = "Reply hazy, try again"
    elif (ran == 5):
        text = "Ask again later"
    elif (ran == 6):
        text = "Better not tell you now"
    elif (ran == 7):
        text = "My sources say no"
    elif (ran == 8):
        text = "Outlook not so good"
    elif (ran == 9):
        text = "Very doubtful"

    print(text)

    again = input("Would you like to ask again?")

    if (again.lower() == "yes" or again.lower() == "ya" or again.lower() == "sure" or again == "y"):
        Ask()
        

Ask()