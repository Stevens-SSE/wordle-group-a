import wordle_ui as ui

def game_logger(wordle, user_input, gamesPlayed, gamesWon, guessDistribution):
    f = open("gameplay.log", "a+")
    f.write(f"Wordle: "+wordle+"\n")
    f.write(f"User_Input: ")
    for i in user_input:
        f.write(f"{i}\t")
    f.write("\nGAME STATISTICS \n")
    f.write(f"Number of games played {gamesPlayed} \n")
    f.write(f"Win percentage {(gamesWon*100/gamesPlayed): .2f} \n")
    f.write(f"Guessed in 1st attempt: {guessDistribution[0]} \n")
    f.write(f"Guessed in 2nd attempt: {guessDistribution[1]} \n")
    f.write(f"Guessed in 3rd attempt: {guessDistribution[2]} \n")
    f.write(f"Guessed in 4th attempt: {guessDistribution[3]} \n")
    f.write(f"Guessed in 5th attempt: {guessDistribution[4]} \n")
    f.write(f"Guessed in 6th attempt: {guessDistribution[5]} \n")
    f.close()
