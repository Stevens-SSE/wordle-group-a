
from copy import copy


class Helper:
    
    def rankedWords(correctWords, incorrectWords):
        rankDic = {}
        import csv
        with open('wordRank.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                rankDic[row[0].split(',')[0]] = row[1].split(',')[0]
        rankDic.pop('Rank')
        myList = []
        defaultList = []
        if correctWords == None and incorrectWords == None:
            for i in range(1,51):
                defaultList.append(rankDic[str(i)])
            return defaultList
        if correctWords != None:
            for key in range(1,len(rankDic)):
                flag = 0
                for letter in correctWords:
                    if letter not in rankDic[str(key)]:
                        flag = 1
                if flag == 0:
                    myList.append(rankDic[str(key)])
        else:
            for key in rankDic:
                myList.append(rankDic[key])
        defaultList = myList.copy()
        if incorrectWords != None:
            for word in myList:
                flag = 0
                for letter in incorrectWords:
                    if letter in word:
                        flag = 1
                if flag == 1:
                    defaultList.remove(word)
        return defaultList

    #testcall to check the function is working right
    #print(rankedWords(['t','r','s'],['b','o','l','i','e']))