'''
Link: https://www.hackerrank.com/challenges/camelcase

There is a sequence of words in CamelCase as a string of letters,s, having the following properties:

    It is a concatenation of one or more words consisting of English letters.
    All letters in the first word are lowercase.
    For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.

Given s, determine the number of words in s.

Example:
s =  oneTwoThree 

There are 3 words in the string: 'one', 'Two', 'Three'.

Function Description

Complete the camelcase function in the editor below.

camelcase has the following parameter(s):

    string s: the string to analyze

Returns

    int: the number of words in s

Input Format

A single line containing string s.


Sample Input

saveChangesInTheEditor

Sample Output

5

Explanation

String

contains five words:

    save
    Changes
    In
    The
    Editor


'''


## Solution 1:


def camelcase(s):

    return len("".join([(" "+i if i.isupper() else i) for i in s]).strip().split())


## Solution 2
import re

def camelcase(s):

    return len(re.findall('.[^A-Z]*', s))

## Solution 3

import re

def camelcase(s):

    return len(re.split('(?=[A-Z])', s))
  
  
if __name__ == '__main__':

    s = input()

    result = camelcase(s)
    print(result)
