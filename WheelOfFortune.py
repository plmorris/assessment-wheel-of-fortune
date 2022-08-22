import random
from threading import Timer
players={0:{"roundtotal":0,"gametotal":0,"name":""},
         1:{"roundtotal":0,"gametotal":0,"name":""},
         2:{"roundtotal":0,"gametotal":0,"name":""}
        }

roundNum = 0
dictionary = [] # this is not a python dictionary, this is a just a list of words
turntext = ""
wheellist = ['BANKRUPT', 'LOSE TURN', 100, 150, 200, 250, 300, 350, 400, 450, 500,
            550, 600, 650, 700, 750, 800, 850, 900]
roundWord= ""
blankWord = ""
vowels = {"a", "e", "i", "o", "u"}
consonants = {"b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r",
              "s", "t", "v", "w", "x", "y", "z"}
roundstatus = ""
finalroundtext = ""

filepath = (r'assessment-wheel-of-fortune\data-txt-files\Data TXT Files\dictionary.txt')
f = open(filepath)
dictionary = f.readlines() # Store each word in a list.
f.close()
for i in range(len(dictionary)):
    dictionary[i] = dictionary[i].replace('\n','')

print("\n================")
print("Wheel of Fortune")
print("================\n")
for i in players.keys():
    Name = input(f"Enter name of Player {i+1}: ").title() # read in player names from command prompt input
    players[i]["name"] = Name

def mysteryWord (): # get random word
    global roundWord
    roundWord = dictionary[random.randint(0,len(dictionary)-1)]
    return roundWord

def bookkeeping (): # keep track of the money after each round
    for n in players.keys():
        players[n]["gametotal"] += players[n]["roundtotal"]
        players[n]["roundtotal"] = 0

mysteryWord()
# print(mysteryWord())
print(roundWord)
blankWord = '_'*len(roundWord)

print("\n~~~~~~~~~~~~~~~")
print("Round 1 Begins!")
print("~~~~~~~~~~~~~~~")

print(f"\nThe mystery word has {len(blankWord)} letters.")

guessedList = []

while roundNum == 0:
    num = [0,1,2]
    r = random.randrange(len(num)) # randomize order of starting player
    while i in range(len(num)):
        for i in range(len(num)):
            playerNum = num[(r+i)%len(num)]
            name = players[playerNum]["name"]
            print(f"\n{name} is up to go.\n")
            print(blankWord)
            breakOuterWhile = False
            next = False
            while next is False:
                option = str(input(f"\nWould {name} like to (s)pin the wheel, (b)uy a vowel, or (g)uess the word? ")).lower()
                if option == 's': # choose spin wheel
                    print(f"\n{name} will spin the wheel.\n")
                    result = random.choice(wheellist) # Get random value for wheellist
                    print(f"The wheel landed on {result}.\n")
                    if result == 'BANKRUPT':
                        print("Sorry, your round total is zero, and you lose your turn.\n")
                        players[playerNum]["roundtotal"] = 0
                        next = True
                        breakFor = False
                    if result == 'LOSE TURN':
                        print("Sorry, your turn is over.\n")
                        next = True
                        breakFor = False
                    if str(result).isnumeric() == True:
                        consonant = str(input("Enter a consonant: "))
                        if len(consonant) > 1:
                            print("You cannot guess more than one letter. Try again.")
                        if consonant in guessedList:
                            print(f"The '{consonant}' has already been found/guessed! Try again.")
                        while consonant not in guessedList and consonant not in vowels:
                            guessedList.append(consonant)
                            if consonant in roundWord:
                                i = 0
                                breakFor = False
                                while roundWord.find(consonant, i) != -1: # extract letter(s) in blank word
                                    i = roundWord.find(consonant, i)
                                    blankWord = blankWord[:i] + consonant + blankWord[i+1:]
                                    i += 1
                                players[playerNum]["roundtotal"] += result
                                print(f"\n{players[playerNum]}")
                                print(f"\n{blankWord}")
                                if blankWord == roundWord:
                                    print(f"Correct! {name} wins Round {roundNum + 1}.")
                                    next = True
                                    roundNum += 1
                                    next = True
                                    breakFor = True
                                    breakOuterWhile = True
                            else:
                                print("Sorry, not in word.\n")
                                next = True
                                breakFor = False
                                breakOuterWhile = False
                                break
                        if consonant in vowels:
                            print(f"You haven't paid for an '{consonant}'! Try again.")
                if option == 'b' and players[playerNum]["roundtotal"] < 250:
                    print("Not enough $$\n")
                if option == 'b' and players[playerNum]["roundtotal"] >= 250:
                    print(f"\n{name} will buy a vowel\n")
                    aeiou = str(input("Enter a vowel: "))
                    if len(aeiou) > 1:
                        print("You cannot guess more than one letter. Try again.")
                    if aeiou in guessedList:
                            print(f"The '{aeiou}' has already been found/guessed! Try again.")
                    while aeiou in vowels and aeiou not in guessedList:
                        players[playerNum]["roundtotal"] -= 250
                        guessedList.append(aeiou)
                        if aeiou in roundWord:
                            j = 0
                            while roundWord.find(aeiou, j) != -1:
                                j = roundWord.find(aeiou, j)
                                blankWord = blankWord[:j] + aeiou + blankWord[j+1:]
                                j += 1
                            print(players[playerNum])
                            print(blankWord)
                            if blankWord == roundWord:
                                print(f"Correct! {name} wins Round {roundNum + 1}.")
                                next = True
                                roundNum += 1
                                next = True
                                breakFor = True
                                breakOuterWhile = True
                        else:
                            print("Sorry, not in word.\n")
                            next = True
                            breakFor = False
                            breakOuterWhile = False
                            break
                if option == 'g':
                    print(f"\n{name} will guess the word\n")
                    guess = str(input("Your word is: "))
                    if guess == roundWord:
                        print(f"Correct! {name} wins Round {roundNum + 1}.")
                        next = True
                        roundNum += 1
                        breakFor = True
                        breakOuterWhile = True
                        break
                    else:
                        print(f"Sorry, {guess} is not correct.\n")
                        next = True
                        breakFor = False
                        breakOuterWhile = False
                if next is True:
                    break
            if breakFor is True:
                break
        if breakOuterWhile is True:
            break
    if roundNum == 1:
        break


bookkeeping()

print(f"\n{players}")

gametotal = []
for i in players.keys():
    gametotal.append(players[i]["gametotal"])
jackpot = max(gametotal)
lead = gametotal.index(jackpot)
print(f"\nSo far {players[lead]} is in the lead.")

# new round word
mysteryWord()
print(roundWord)
blankWord = '_'*len(roundWord)

print("\n~~~~~~~~~~~~~~~")
print("Round 2 Begins!")
print("~~~~~~~~~~~~~~~")

print(f"\nThe mystery word has {len(blankWord)} letters.")

# new empty list of gueses
guessedList = []

while roundNum == 1:
    num = [0,1,2]

    r = random.randrange(len(num)) # randomize order of starting player
    while i in range(len(num)):
        for i in range(len(num)):
            playerNum = num[(r+i)%len(num)]
            name = players[playerNum]["name"]
            print(f"\n{name} is up to go.\n")
            print(blankWord)
            breakOuterWhile = False
            next = False
            while next is False:
                option = str(input(f"\nWould {name} like to (s)pin the wheel, (b)uy a vowel, or (g)uess the word? ")).lower()
                if option == 's': # choose spin wheel
                    print(f"\n{name} will spin the wheel.\n")
                    result = random.choice(wheellist) # Get random value for wheellist
                    print(f"The wheel landed on {result}.\n")
                    if result == 'BANKRUPT':
                        print("Sorry, your round total is zero, and you lose your turn.\n")
                        players[playerNum]["roundtotal"] = 0
                        next = True
                        breakFor = False
                    if result == 'LOSE TURN':
                        print("Sorry, your turn is over.\n")
                        next = True
                        breakFor = False
                    if str(result).isnumeric() == True:
                        consonant = str(input("Enter a consonant: "))
                        if len(consonant) > 1:
                            print("You cannot guess more than one letter. Try again.")
                        if consonant in guessedList:
                            print(f"The '{consonant}' has already been found/guessed! Try again.")
                        while consonant not in guessedList and consonant not in vowels:
                            guessedList.append(consonant)
                            if consonant in roundWord:
                                i = 0
                                breakFor = False
                                while roundWord.find(consonant, i) != -1:
                                    i = roundWord.find(consonant, i)
                                    blankWord = blankWord[:i] + consonant + blankWord[i+1:]
                                    i += 1
                                players[playerNum]["roundtotal"] += result
                                print(players[playerNum])
                                print(blankWord)
                                if blankWord == roundWord:
                                    print(f"Correct! {name} wins Round {roundNum + 1}.")
                                    next = True
                                    roundNum += 1
                                    next = True
                                    breakFor = True
                                    breakOuterWhile = True
                            else:
                                print("Sorry, not in word.\n")
                                next = True
                                breakFor = False
                                breakOuterWhile = False
                                break
                        if consonant in vowels:
                            print(f"You haven't paid for an '{consonant}'! Try again.")
                if (option == 'b' and players[playerNum]["gametotal"] < 250 and players[playerNum]["roundtotal"] < 250):
                    print("Not enough $$\n")
                if (option == 'b' and (players[playerNum]["gametotal"] >= 250 or players[playerNum]["roundtotal"] >= 250)):
                    print(f"\n{name} will buy a vowel\n")
                    aeiou = str(input("Enter a vowel: "))
                    if len(aeiou) > 1:
                        print("You cannot guess more than one letter. Try again.")
                    if aeiou in guessedList:
                            print(f"The '{aeiou}' has already been found/guessed! Try again.")
                    while aeiou in vowels and aeiou not in guessedList:
                        if players[playerNum]["gametotal"] > 250:
                            players[playerNum]["gametotal"] -= 250
                            players[playerNum]["roundtotal"] += 250
                        players[playerNum]["roundtotal"] -= 250
                        guessedList.append(aeiou)
                        if aeiou in roundWord:
                            j = 0
                            while roundWord.find(aeiou, j) != -1:
                                j = roundWord.find(aeiou, j)
                                blankWord = blankWord[:j] + aeiou + blankWord[j+1:]
                                j += 1
                            print(players[playerNum])
                            print(blankWord)
                            if blankWord == roundWord:
                                print(f"Correct! {name} wins Round {roundNum + 1}.")
                                next = True
                                roundNum += 1
                                next = True
                                breakFor = True
                                breakOuterWhile = True
                        else:
                            print("Sorry, not in word.\n")
                            next = True
                            breakFor = False
                            breakOuterWhile = False
                            break
                if option == 'g':
                    print(f"\n{name} will guess the word\n")
                    guess = str(input("Your word is: "))
                    if guess == roundWord:
                        print(f"Correct! {name} wins Round {roundNum + 1}.")
                        next = True
                        roundNum += 1
                        breakFor = True
                        breakOuterWhile = True
                        break
                    else:
                        print(f"Sorry, {guess} is not correct.")
                        next = True
                        breakFor = False
                        breakOuterWhile = False
                if next is True:
                    break
            if breakFor is True:
                break
        if breakOuterWhile is True:
            break
    if roundNum == 1:
        break

bookkeeping()

print(f"\n{players}")

# third round random word
mysteryWord()
blankWord = '_'*len(roundWord)

guessedList = []

letters = ['r','t','l','n','e']
for l in letters:
    if l in roundWord:
        i = 0
        while roundWord.find(l, i) != -1:
            i = roundWord.find(l, i)
            blankWord = blankWord[:i] + l + blankWord[i+1:]
            i += 1

vowelTry = 1
consTry = 3

gametotal = []
for i in players.keys():
    gametotal.append(players[i]["gametotal"])
jackpot = max(gametotal)
winNum = gametotal.index(jackpot)

print(f"\n{players[winNum]}")

winner = players[winNum]["name"]
print(f"\n{winner} moves on to the Final Round.\n")
print(f"\nRSTLNE will be unveiled, if any, in the Final Round's word.")
print(f"The mystery word has {len(blankWord)} letters.\n")
print("If you are successful, your game total money will be multiplied\nby the number of letters in the final round word.")
print(blankWord)

amount = players[winNum]["gametotal"]

timeout = 5
t = Timer(timeout, print, [f'Sorry, time\'s up! The word was {roundWord}. {winner} earns ${amount}.'])

while roundNum == 2:
    next = False
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print("The Final Round Begins!")
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    while next is False:
        while consTry > 0 or vowelTry > 0:
            option = str(input(f"\nWould {winner} like to guess a (c)onsonant or (v)owel? ")).lower()
            if option == 'c' and consTry > 0:
                consTry -= 1
                print(f"\n{winner} will guess a consonant.\n")
                consonant = str(input("Enter a consonant: "))
                if len(consonant) > 1:
                    print("You cannot guess more than one letter. Try again.")
                if consonant in guessedList:
                    print(f"The '{consonant}' has already been found/guessed! Try again.")
                while consonant not in guessedList and consonant not in vowels:
                    guessedList.append(consonant)
                    if consonant in roundWord:
                        i = 0
                        while roundWord.find(consonant, i) != -1:
                            i = roundWord.find(consonant, i)
                            blankWord = blankWord[:i] + consonant + blankWord[i+1:]
                            i += 1
                        print(f"You have {consTry} consonant(s) left.\n")
                        print(blankWord)
                        if blankWord == roundWord:
                            print(f"Congratuliations! You win Wheel of Fortune!")
                            players[winNum]["gametotal"] *= 10
                            roundNum += 1
                    else:
                        print(f"Sorry, not in word. You have {consTry} consonant(s) left.\n")
                if consonant in vowels:
                    print(f"Consonant required. Cannot redo.")
            if consTry == 0 and option == 'c':
                print("Out of consonants.")
            if option == 'v' and vowelTry > 0:
                vowelTry -= 1
                print(f"\n{winner} will guess your only vowel.\n")
                vowel = str(input("Enter a vowel: "))
                if len(vowel) > 1:
                    print("You cannot guess more than one letter. Cannot redo.")
                if vowel in blankWord:
                    print(f"The '{vowel}' has already been found/guessed! Cannot redo.")
                while vowel not in guessedList and vowel in vowels:
                    guessedList.append(vowel)
                    if vowel in roundWord:
                        i = 0
                        while roundWord.find(vowel, i) != -1:
                            i = roundWord.find(vowel, i)
                            blankWord = blankWord[:i] + vowel + blankWord[i+1:]
                            i += 1
                        print(blankWord)
                        if blankWord == roundWord:
                            print(f"Congratuliations! You win Wheel of Fortune!\n")
                            players[winNum]["gametotal"] *= len(roundWord)
                            next = True
                            roundNum += 1
                            break
                    else:
                        print(f"Sorry, not in word. You have {vowelTry} vowels left.\n")
                if vowel not in vowels:
                    print(f"Vowel required. Cannot redo.")
            if vowelTry == 0 and option == 'v':
                print("Out of vowels.")
        print(blankWord)
        t.start()
        prompt = "GUESS THE WORD IN %d SECONDS! Your word is: " % timeout
        guess = input(prompt)
        t.cancel()
        if guess == roundWord:
            print(f"Congratuliations! {winner} wins Wheel of Fortune!")
            players[winNum]["gametotal"] *= len(roundWord)
            next = True
            roundNum += 1
            break
        else:
            print(f"Sorry, {guess} is not correct.")
        next = True
        if next is True:
            break
    if roundNum != 2:
        break
earning = players[winNum]["gametotal"]
print(f"{winner} will take home ${earning}.")
