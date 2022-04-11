import random
#Function to remove blank spaces from the dictionary
class Word_Dictionary:
    finalList = []
    myList = []
    def __init__(self):
        self.finalList = []
        self.myList = []
        
    def __str__(self) -> str:
        return f"Word_Dictionary(myList:{str(self.myList)},finalList:{str(self.finalList)})"

    def remove(self, string):
        return string.replace("\n", "")
    
    def filter_dic(self):
        #Imports the dictionary
        d = open("words.txt", "r")
        f = open("word_list.txt", "w")
        for x in d:
            x = self.remove(x)
            if len(x) == 5:
                self.myList.append(x)
                f.write(x+"\n")
        f.close()
    #Chooses the wordle
    def wordleAns(self):
        #return random.choice(list)
        r = open("word_list.txt", "r")
        files = r.read()
        dictList = files.split("\n")
        self.finalList = list(dictList)
        wordle = random.choice(self.finalList)
        r.close()
        return wordle

