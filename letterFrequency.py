import csv
import string

class Letter_Frequency:
    wrd_occurence = dict()
    myList = []
    def __init__(self):
        self.myList = []
        self.wrd_occurence = dict( (key, [0,0,0,0,0]) for key in string.ascii_lowercase )
    
    def __str__(self) -> str:
        return f"Letter_Frequency(myList:{str(self.myList)},wrd_occurence:{str(self.wrd_occurence)})"
    
    #Calculates the Letter Likelihood
    def letter_likelihood(self):
        r = open("word_list.txt", "r")
        files = r.read()
        dictList = files.split("\n")
        self.myList = list(dictList)
        r.close()
        for wrd in self.myList:
            count = 0
            for letter in wrd:
                self.wrd_occurence[letter][count] += 1
                count+=1
        
        for letter in string.ascii_lowercase:
            flag = 0
            for wrd in self.myList:
                flag += 1
            for i in range(5):
                self.wrd_occurence[letter][i] = round((self.wrd_occurence[letter][i] / flag),4)

        f = open("letterFrequency.csv", 'w')
        for letter in string.ascii_lowercase:
            f.write(f"{letter}, {self.wrd_occurence[letter][0]}, {self.wrd_occurence[letter][1]}, {self.wrd_occurence[letter][2]}, {self.wrd_occurence[letter][3]}, {self.wrd_occurence[letter][4]}\n")

        return self.wrd_occurence

    #Converting the list to Tuple
    def list_To_tuple(self, diction):
        for key in diction.keys():
            diction[key] = tuple(diction[key])
        return diction

    #Convert the Statistics into a Dictionary of Tuples
    def statsTodicTuples(self):
        file = open("letterFrequency.csv")
        csvreader = csv.reader(file)
        wrd_occurence_csv = {}
        for row in csvreader:
            wrd_occurence_csv[row[0]] = (row[1], row[2], row[3], row[4], row[5])
        #print(word_occurence_csv)
        file.close()
        return wrd_occurence_csv

    #Calculates the Occurence Likelihood      
    def occ_likelihood(self):
        occ_like = {}
        if self.check_len(wrd):
            for wrd in self.myList:
                occurence_likelihood = float(self.wrd_occurence[wrd[0]][0]) * float(self.wrd_occurence[wrd[1]][1]) * float(self.wrd_occurence[wrd[2]][2]) * float(self.wrd_occurence[wrd[3]][3]) * float(self.wrd_occurence[wrd[4]][4])
                if self.check_likelihood_range(occurence_likelihood):
                    occ_like[wrd] = occurence_likelihood

        sorted_list = sorted(occ_like.items(), key=lambda x:x[1])
        sorted_list.reverse()
        f = open("wordRank.csv", 'w')
        f.write("Rank, Word, Likelihood \n")
        flag = 1
        for wrd in sorted_list:
            f.write(f"{flag}, {wrd[0]}, {wrd[1]}\n")
            flag += 1
        f.close()
        return sorted_list

    #Checks the length of the word
    def check_len(self, wrd):
        if len(wrd) == 5:
            return True
        else:
            return False

    def check_likelihood_range(self, likelihood):
        if likelihood<1:
            return True
        else:
            return False


    #print(letter_likelihood())
    #print()
    #print(list_To_tuple(wrd_occurence))
    #print()
    #print(statsTodicTuples())
    #print()
    #print(occ_likelihood())