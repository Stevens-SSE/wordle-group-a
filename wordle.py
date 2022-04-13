#Wordle
#Pseudocode
#This program is an attempt to implement the Wordle game

#function compare_wordle(Argument one, Argument two){

    #FOR every character in the two strings compare with each other
        #IF a character is equal to a character in the wordle THEN it checks
            #if the letter is in the same position as the wordle
                #print prompt "(The character) is in the correct position"
            #ELSE
                #print prompt "(The character) is in the wordle but not in the correct position"
            #ENDIF
        #ENDIF
#end
#}

#{
#In the main function
    #print prompt "Welcome to Wordle"
    #Initialize the counter to 0, declare the wordle "SONAR", initialize the user attempt_list

    #WHILE counter < 6
    #{
        #Initialize boolean to False
        #print prompt "Enter the word: "
        #Accept user_input from the user and convert it to Upper Case
        #IF the user_input length is not equal to 5 THEN
            #print prompt "The word must consist of 5 alphabets only"
            # counter is reduced by 1
        #ELSE IF the user_input contains anything but alphabets
            #print prompt "The word must consist of alphabets only"
        #ELSE
            #IF the user_input is not in the attempt_list THEN add the user_input to the attemp_list
                #IF the user_input is equal to the wordle THEN
                    #print prompt "Congratulations! You have solved the Wordle!"
                    #BREAK
                #ELSE call the function compare_wordle(user_input, wordle)
                    #Initialize an attempt counter equal to 5-counter
                    #print prompt "Remaining Attempts: " (attempt)"
            #ELSE
                #print prompt "You have attempted this word earlier. Please try another word."
                #Decrement the counter by 1 and #Initialize an attempt counter equal to 5-counter
                #print prompt "Remaining Attempts: " (attempt)"
    #Increment counter by 1
    #}ENDWHILE
#IF counter is greater than 5 THEN
    #print prompt"Sorry, but you have failed to solve the wordle!!! Please try again!!! "

#Code
#Function to compare the Wordle
class Wordle:

    def compareWord(self, a, b):
        if (a == b):
            return True
        else:
            return False

    def compare_wordle(self, word, answer):
        status = []
        letter_counts: dict = {}  # making a dictionary to store the number of letters
        for letter in answer:  # loop used to store the number of letters in the answer
            if letter in letter_counts.keys():
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
        for index in range(len(answer)):  # loop used to store the status
            if word[index] == answer[index]:
                status.append(' ')
                letter_counts[answer[index]] -= 1
            else:
                status.append('"')
        for index in range(len(answer)):
            if word[index] != answer[index]:
                if word[index] in letter_counts:
                    if letter_counts[word[index]] > 0:
                        letter_counts[word[index]] -= 1
                        status[index] = "`"
        out = ''.join(status)
        print(" " * 16 + out)

        # op = [None] * 5 #output variable
        # rp = []         #right position list
        # wp = []         #wrong position list
        # # Code for right position
        # for i in range(len(str1)):
        #     if str1[i] == str2[i]:
        #         # Condition to check if the letter is in correct position
        #         op[i] = " "
        #         if str1[i] not in rp:
        #             rp.append(str1[i])
        #     else:
        #         op[i] = '"'
        #
        # for i in range(len(str1)):
        #     for j in range(len(str2)):
        #         if op[i] == '"':
        #             #Condition to check if letter is present in the wordle
        #             if str1[i] == str2[j] and str1[i] in rp and wp:
        #                 op[i] = '"'
        #             elif str1[i] == str2[j] and str1[i] in rp:
        #                 op[i] = '"'
        #             elif str1[i] == str2[j] and str1[i] in wp:
        #                 op[i] = '"'
        #             elif str1[i] == str2[j]:
        #                 op[i] = "`"
        #                 wp.append(str1[i])
        #         else:
        #             continue
        #
        # out = ''.join(op)
        # print(" " * 16 + out)
        # return out
