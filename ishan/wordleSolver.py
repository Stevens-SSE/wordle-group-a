"""
__author__ = "Ishan Aryendu"
__credits__ = ["Tech With Tim (YouTube)", "geeksforgeeks.org", stackoverflow]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Ishan Aryendu"
__email__ = "iaryendu@stevens.edu"
__status__ = "Development"
__packages__ = ['string', 're']

"""
import re
import string

from singleLL import SLinkedList


class Solve():

    # do some checks to the user regex
    def error_msg(self):
        print("Second argument should be exactly 5 characters long, consisting of letters and underscores only")
        exit()

    def solve(self, flag: bool, match: str = '?', mismatch: str = '?', pattern: str = '?'):
        """Solve the word using list of match and unmatched characters and the pattern"""
        dictionary = open("resource/word5.txt", "r")
        words = dictionary.readlines()
        # print("Loaded " + str(len(words)) + " words from dictionary.")
        dictionary.close()
        max = 51

        # this will be the array with the possible answers
        solutions = []

        # remove new lines from words in array, put them into solutions array
        for word in words:
            solutions.append(word.strip())

        # remove words without the necessary chars
        if match != '?':
            solutions = [x for x in solutions if all(y in x for y in match)]

        # remove words with characters that we know aren't in the solution
        if mismatch != '?':
            solutions = [x for x in solutions if all(y not in x for y in mismatch)]

        regex = pattern

        if regex == '?':
            regex = "_____"
        allowed = set(string.ascii_lowercase + '_')
        if not set(regex) <= allowed:
            self.error_msg()
        if len(regex) != 5:
            self.error_msg()

        regex = regex.replace("_", ".")

        # match based on regex
        regex_pattern = "^" + regex + "$"
        pattern = re.compile(regex_pattern)

        # llist = SLinkedList()
        lst = []

        for word in solutions:
            if pattern.match(word):
                if flag:
                    max -= 1
                    if max == 0:
                        # return llist
                        return lst
                # print(word)
                # llist.AtBegining(word)
                lst.append(word)

        # return llist
        return lst


if __name__ == '__main__':
    s = Solve()
    llist = s.solve(True, 'smile', '?', '?')
    llist.return_first()
    llist.listprint()
