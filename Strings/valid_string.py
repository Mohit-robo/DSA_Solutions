'''
https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?isFullScreen=true
'''

def isValid(s):
    #Create array to store frequency of each character
    arr=[0 for i in range(26)]
    for i in s:
        arr[ord(i)-97]+=1
    xset=set(arr)
    print(xset)
    #Discard elements with count=0 
    xset.discard(0)
    if len(xset)==1:    #If length==1, the string is already valid
        return "YES"
    elif len(xset)==2:  
        a,b=xset.pop(),xset.pop()   #Pop out both the counts from set
        #If (difference between count is 1 or that element occurs a single time) and that occurs only once in array, we can remove that character once and string would be valid
        if (abs(b-a)==1 or a==1) and arr.count(a)==1:
            return "YES"
        #Same for the other element
        elif (abs(b-a)==1 or b==1) and arr.count(b)==1:
            return "YES"
        #Otherwise we cannot convert to a valid stringy
        else:
            return "NO"
    else:               #If length>2, we cannot convert string to a valid string
        return "NO"

s = input()

result = isValid(s)
print(result)