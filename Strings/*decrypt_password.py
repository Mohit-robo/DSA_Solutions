'''
The password string is encrypted in this way"

1. If lower case letter followed by UPPER case letter 
    a. swap
    b. put a * after that
    c. proceed

2. If it is a number except 0:
    a. replace with 0
    b. put original number at the start -- (last number will be at the very first)
    c, proceed

3. Else:
    proceed to next element

hAck3rr4nk --> 43Ah*ck0rr0nk

************

We need to decrypt this string to get the original password

Case 1:

Input: 51Pa*0Lp*0e 

Output:
aP1pL5e

1. The very first number in the string replaced with the last 0 in the string and so forth.
2. UPPER CASE letter followed by lower case and followe by * becomes lower case followed by UPPER CASE and * being removed.
3. Just add the other elemnts apart from these as they are to the string.

Case 2:

Input: pTo*Ta*o
Output: poTaTO
'''

def decryptPassword(s):
    
    zer0_count_= 1
    output_str = ''
    out_list = [s]
    for i in range(len(out_list[0])-1):
 
        if s[i] == ('0'):

            output_str += out_list[0][zer0_count_]
            zer0_count_ -= 1
                
        elif s[i] == ('*'):
            output_str += out_list[0][i-1]
            output_str += out_list[0][i-2]
        
        elif s[i].islower() and (s[i - 1].islower() or s[i+1] != ('*')):
            output_str += out_list[0][i]

    return output_str + out_list[0][-1]


s = input()

result = decryptPassword(s)

print(result)