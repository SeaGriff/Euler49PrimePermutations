""" Solves project euler problem 49.
"""

# Imports
import prime_tools as pt

# Constants
NUM_DIGITS = 4

""" Accepts a set of characters and returns a set of all strings which are permutations of those characters.
Accepts: set<char> charSet
Returns: set<string> """
def permuteCharacters(charSet):
    result = set()
    for a in charSet:
        toCheck = queue.Queue()
        toCheck.put(a)
        while not toCheck.empty():
            currentString = toCheck.get()
            if len(currentString) == len(charSet):
                result.add(currentString)
            else:
                for newChar in charSet:
                    if not newChar in currentString:
                        toCheck.put(currentString + newChar)
    return(result)

""" Builds a set of all primes with exactly NUM_DIGITS digits.
Returns: set<int> """
def buildPrimeSet():
    latest = 2
    result = set()
    while len(str(latest)) <= NUM_DIGITS:
        if len(str(latest)) == NUM_DIGITS:
            result.add(latest)
        latest = pt.nextPrime(latest)
    return result

def main():
    