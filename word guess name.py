import random
words = ["bright", "champs", "coding", "students"]
word = random.choice(words)
playername= input("Please enter your name.")
guesstheletter= ""
chance = 10
while chance>0:
    guessed = input("Please guess a letter form the word.")
    guesstheletter = guesstheletter + guessed
    wrong = 0
    for i in word:
        if i in guesstheletter:
            print(i)
        else:
            print("_")
            wrong = 1
    if wrong == 0:
        print("Congrats you got the word right.")
        break
    if guessed not in word:
        chance  = chance - 1
        print("You got the letter worong you have {} chances remaining." .format (chance))
    if chance == 0:
        print("You lost all the chances. The corect word is ", word) 
    

