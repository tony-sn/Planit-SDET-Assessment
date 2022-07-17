''' Challenge 002:
Write a solution to find the character that has the highest number of occurrences within a certain lookup_string, ignoring case.
If there is more than one character with equal highest occurrences, return the character that appeared first within the lookup_string
'''
from collections import Counter

def getMaxOccurringChar(str):
    return Counter(str.lower()).most_common(1)[0][0] 

lookup_string = 'Ice-ice-ice-Creami'

print("Most occurring (and appear first) character in the word {} is".format(
    lookup_string), getMaxOccurringChar(lookup_string))
