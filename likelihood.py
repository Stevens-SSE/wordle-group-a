from csv import DictReader
import string
import dictionary as dic
def letter_likelihood():
    wrd_occurence = dict( (key, [0,0,0,0,0]) for key in string.ascii_lowercase )
    for wrd in dic.myList:
        count = 0
        for letter in wrd:
            wrd_occurence[letter][count] += 1
            count+=1
    
    for letter in string.ascii_lowercase:
        flag = 0
        for wrd in dic.myList:
            if wrd.__contains__(letter):
                flag += 1
        for i in range(5):
            wrd_occurence[letter][i] = round((wrd_occurence[letter][i] / flag),4)

    f = open("letterFrequency.csv", 'w')
    for letter in string.ascii_lowercase:
        f.write(f"{letter}, first_pos_{wrd_occurence[letter][0]}, second_pos_{wrd_occurence[letter][1]}, third_pos_{wrd_occurence[letter][2]}, fourth_pos_{wrd_occurence[letter][3]}, fifth_pos_{wrd_occurence[letter][4]}\n")

    return wrd_occurence

def list_To_tuple(dict):
    for key in dict.keys():
        dict[key] = tuple(dict[key])

def statsTodicTuples():
    #f = open("letterFrequency.csv", 'w')
    # open file in read mode
    with open('letterFrequency.csv', 'r') as read_obj:
        # pass the file object to DictReader() to get the DictReader object
        dict_reader = DictReader(read_obj)
        # get a list of dictionaries from dct_reader
        tuple_of_dict = tuple(dict_reader)
        # print list of dict i.e. rows
        print(tuple_of_dict)
        

print(letter_likelihood())
print()
print(list_To_tuple(dic.myList))
print()
print(statsTodicTuples())