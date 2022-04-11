import dictionary as dic
from wordle import Wordle as wrd
import logger as logger
from helper import Helper as helper
# UI for playing the the wordle game 
class UI:
    gamesPlayed = 0
    gamesWon = 0
    guessDistribution = []
    def __init__(self):
        self.wrd = wrd()
        self.dic = dic.Word_Dictionary()
        self.gamesPlayed = 0
        self.gamesWon = 0
        self.guessDistribution = [0,0,0,0,0,0]

    def __str__(self) -> str:
        return f"UI(wrd:{str(self.wrd)},dic:{str(self.dic)},gamesPlayed:{str(self.gamesPlayed)},gamesWon:{str(self.gamesWon)},guessDistribution:{str(self.guessDistribution)})"
    
    def main(self):
        print("Welcome to Wordle")
        self.dic.filter_dic()
        
        while(True):
            self.gamesPlayed += 1
            counter = 0
            wordle = self.dic.wordleAns()
            print(wordle)
            #print(self.dic.myList)
            attempt_list = []
            bad_letters_list = []
            while counter < 6:
                boolean = False
                try:
                    user_input = input("Rules of the game: \n 1. A player must guess a random five-letter word. \n 2. You have 6 attempts to solve the game. \n 3. A letter in green means it’s correct and in the right place. A letter in yellow means it’s in the word but in the wrong place. \n 4. The word needs to be typed in all caps \n\n\n Enter the word: ")
                    user_input = user_input.lower()
                except:
                    print("Error in user input")
                # Chgecking length of user input 
                if (self.exit_game(user_input)):
                    quit()
                if self.check_len(user_input):
                    print("The word must have of 5 alphabets ")
                    counter = counter - 1
                # Checking for correct user input i.e only alphabets
                elif (self.check_char(user_input)):
                    print("The word must consist of only alphabets")
                    counter = counter - 1
                else:
                    # Condition to check if user input is in the dictionary provided
                    if self.check_dic(user_input):
                        print("Word not found in Dictionary")
                        counter = counter - 1
                        attempt = 5 - counter
                        print("Attempts Remaining: ", attempt)
                    elif user_input in self.dic.myList:
                        if user_input not in attempt_list:
                            attempt_list.append(user_input)
                            # Condition to check if user input matches the puzzle word 
                            if user_input == wordle:
                                self.gamesWon += 1
                                self.guessDistribution[counter] += 1
                                print("Congratulations! You have solved the Wordle!")
                                break
                            # Condition to call the compare_wordle function
                            else:
                                self.wrd.compare_wordle(user_input, wordle)
                                attempt = 5 - counter
                                print("Attempts Remaining: ", attempt)
                                helper_input = input("Do you want to use the Wordle Helper?(Y/N): ")
                                if helper_input == "Y" or "y":
                                    good_letters = input("Enter good letters separated by space: ")
                                    good_letters = good_letters.lower()
                                    good_letters_list = good_letters.split(" ")
                                    bad_letters = input("Enter the bad letters separated by space: ")
                                    bad_letters = bad_letters.lower()
                                    temp_bad_letters_list = bad_letters.split(" ")
                                    bad_letters_list.extend(temp_bad_letters_list)
                                    print(bad_letters_list)
                                    #bad_letters_list = bad_letters_list, bad_letters.split(" ")
                                    print("Helper Function Output: ")
                                    helper_words = helper.rankedWords(good_letters_list, bad_letters_list)
                                    if len(helper_words) <= 0:
                                        print("No output to display from the helper!")
                                    else:
                                        print(helper_words)
                        else:
                            # Condition to check if the word is used previously in game and reset counter
                            print("You have attempted this word earlier. Please try another word.")
                            counter = counter - 1
                            attempt = 5 - counter
                            print("Remaining Attempts: ", attempt)
                counter += 1
            if counter > 5:
                print("Sorry, but you have failed to solve the wordle!!! Please try again!!! ")
            print("GAME STATISTICS")
            print(f"Number of games played {self.gamesPlayed}")
            print(f"Win percentage {(self.gamesWon*100/self.gamesPlayed): .2f}")
            print(f"Guessed in 1st attempt: {self.guessDistribution[0]}")
            print(f"Guessed in 2nd attempt: {self.guessDistribution[1]}")
            print(f"Guessed in 3rd attempt: {self.guessDistribution[2]}")
            print(f"Guessed in 4th attempt: {self.guessDistribution[3]}")
            print(f"Guessed in 5th attempt: {self.guessDistribution[4]}")
            print(f"Guessed in 6th attempt: {self.guessDistribution[5]}")
            logger.game_logger(wordle, attempt_list, self.gamesPlayed, self.gamesWon, self.guessDistribution)

    def exit_game(self, a):
        # Condition to check length of user input
        try:
            if(len(a)== 0):
                return True
            else:
                return False
        except:
            print("Error Exiting Game")

    def check_char(self, a):
        # Condition to check whether the user input contains only alphabets or not
        try:
            if(a.isalpha()):
                return False
            else:
                return True
        except:
            print("Error in checking character")

    def check_dic(self, a):
        try:
            if(a not in self.dic.myList):
                return True
            else:
                return False
        except:
            print("Error in checking word in dictionary")

    def check_len(self, a):
        try:
            if(len(a) != 5):
                return True
            else:
                return False
        except:
            print("Error in checking length of character")

if __name__ == "__main__":
    ui = UI()
    ui.main()


