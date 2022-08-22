# every player goes to zero unless they already banked money
# dictionary one word per entry: makes it simpler
# you have to bank up to $250 before you buy a vowel
# if they do not successfully guess the answer, their turn is over
# Normally it's spin,  guess a letter and then as long as the letter was there
#   they can either a.) buy a vowel b.) spin again or c.) try to solve the puzzle
# tbh, they may let people buy a vowel whenever

# store in list?
# google "timer in python"

# rounds function
# if round = 1 or 2
    # random choice of starting player
    # for loop iterating over players
        # ask player: spin wheel and guess consonant [1], buy a vowel [2], or guess whole word [3]
        # if player chooses 1:
            # wheel outcomes function
        # if player chooses 2:
            # player bank has -250
            # prompt player for vowel
            # if vowel is in word
                # display blank word with vowel unveiled
            # else
                # end player turn
                # go to next player
        # if player chooses 3
            # prompt player for full word
            # if word = blank word
                # display blank word
                # print they won the that round
                # break for loop and go to round 2
            # else
                # go to next player
    # print round is over
# if round = 3
    # get winning player and bank info
    # random word
    # for each character in blank word
        # reveal any and all RSTLNE in blank word
    # prompt user to guess one letter at a time or full word
    # if guess one letter
        # prompt for letter
        # number of consonants entered
        # number of vowels entered
        # if user enters consonant
            # while number of consonants <= 3
                # if consonant is in word
                    # display letter in word
                # else
                    # end
                    # return to prompt for letter
        # if user enters vowel
            # while number of vowels <= 1
                # if vowel in word
                    # display letter in word
                # else
                    # end
                    # return to prompt for letter
    # else
        # prompt for word
        # if word = blank word
            # win
        # else
            # lose final round


# round number increments

# wheel outcomes function
# get player bank information
# while loop for spinning wheel on a player's turn
    # pick random number out of 19: each number corresponds to either a dollar amount, bankrupt, or turn end
    # if lands on number
        # player guesses consonant
        # if consonant is in word
            # reveal letter in masked word
            # add money to player's bank
            # 
        # else
            # go to next player
    # if lands on bankrupt
        # player bank = 0
        # go to next player
    # if lands on turn end
        # go to next player