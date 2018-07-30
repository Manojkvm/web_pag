import random

def user_guess():
    return list(input("enter a 3 digits number to guess: "))

def generate_code():
    x = [str(i) for i in range(10)]
    random.shuffle(x)
    return x[:3]

def check_guess(code,user_code):

    if code == user_code:
        return "CODE CRACKED!"

    clues = []

    for ind,num in enumerate(user_code):
        if num == code[ind]:
            clues.append('match')
        elif num in code:
            clues.append('close')

    if clues==[]:
        return list('nope')
    else:
        return clues

print("hi! welcome lets play game")
code = generate_code()
clue_report = []

while clue_report != "CODE CRACKED!":
    user_code = user_guess()
    clue_report = check_guess(code,user_code)
    print(" here is the result of your clue: ")
    for clue in clue_report:
        print(clue)
