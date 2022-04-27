'''

Link: https://www.hackerrank.com/challenges/strong-password

'''
# Solution 1


def contains(chars,word):
    for c in chars:
        if c in word:
            return True
    return False

def minimumNumber(n, password):

    NUMBERS = "0123456789"
    LOWER_CASE = "abcdefghijklmnopqrstuvwxyz"
    UPPER_CASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    SPECIAL_CHARS = "!@#$%^&*()-+"
    MIN_REQUIREMENT = 6

    if n < MIN_REQUIREMENT:
        val_1 = MIN_REQUIREMENT-n    
    else:
        val_1 = 0
        
    if not contains(NUMBERS,password):
        val_2 = 1
    else:
        val_2 = 0
    
    if not contains(LOWER_CASE,password):
        val_2 += 1

    if not contains(UPPER_CASE,password):
        val_2 += 1

    if not contains(SPECIAL_CHARS,password):
        val_2 += 1

    return max(val_1,val_2)

 # Solution 2

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    n_bool = 1
    l_bool = 1
    u_bool = 1
    s_bool = 1
    for c in password:
        if c in numbers: n_bool = 0
        elif c in lower_case: l_bool = 0
        elif c in upper_case: u_bool = 0
        elif c in special_characters: s_bool = 0
    return max(6-n, n_bool + l_bool + u_bool + s_bool)
  
  
if __name__ == '__main__':

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    print(answer)
