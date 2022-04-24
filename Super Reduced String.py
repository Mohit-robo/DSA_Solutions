'''

Link: https://www.hackerrank.com/challenges/reduced-string


Reduce a string of lowercase characters in range ascii[‘a’..’z’]by doing a series of operations. In each operation, select a pair of adjacent letters that match, and delete them.

Delete as many characters as possible using this method and return the resulting string. If the final string is empty, return Empty String

Example:

s = 'aab' --> aab shortens to b in one operation: remove the adjacent a characters.

s = 'abba' Remove the two 'b' characters leaving 'aa'. Remove the two 'a' characters to leave ''. Return 'Empty String'.


Function Description

Complete the superReducedString function in the editor below.

superReducedString has the following parameter(s):

    string s: a string to reduce

Returns

    string: the reduced string or Empty String

Input Format

A single string, s.

Constraints

Sample Input 0

aaabccddd

Sample Output 0

abd

Explanation 0

Perform the following sequence of operations to get the final string:

aaabccddd → abccddd → abddd → abd

Sample Input 1

aa

Sample Output 1

Empty String

Explanation 1

aa → Empty String

Sample Input 2

baab

Sample Output 2

Empty String

Explanation 2

baab → bb → Empty String

'''

## Solution 1:

def superReducedString(s):
    
    changed = True
    if s != '':    
        while changed:
            changed = False
            for i in range (len(s) - 1):
                if s[i] == s[i+1]:
                    changed = True
                    s = s[:i] + s[i+2:]
                    break
        return s
    
    else:
        return 'Empty String'
      
## Solution 2:
  
def super_reduced_string(s):
    stack = []
    
    for c in s:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)

    return ''.join(stack)
  
## Solution 3:
  
def superReducedString(s):
    if not s:
        return "Empty String"
    for i in range(0,len(s)):
        if i < len(s)-1:
            if s[i] == s[i+1]:
                return superReducedString(s[:i]+s[i+2:])
    return s
  
if __name__ == '__main__':
    s = input()

    result = super_reduced_string(s)
    if result:
        print(result)
    else:
        print("Empty String")  
  
## Solution 4:
import re

def superReducedString(s):
    while re.search(r"(\w)\1", s):
        s = re.sub(r"(\w)\1", "", s)
    return s or "Empty String"
  
print(superReducedString(input()))

