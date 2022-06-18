'''
Arrange the string in a lexicographical order.
'''
## Solution 1

class User(object):
    @classmethod
        
    def smalleststring(cls,ip1,ip2):
        
        ray = [ip2]
        kevin = []

        for i in range (len(ray)):
            
            item = ray[i]

            ray.remove(item)
            kevin.append(item)
            
        S = User.solve(kevin[0])

        return S

    def solve(s):
        temp = [0]*len(s)   ## An array of size of string with all 0's
        m=len(s)-1
        for i in range(len(s)-1, -1, -1):     ## Loop in reverse order
            
            if s[i]<s[m]: m=i
            temp[i] = m
        for i in range(len(s)):
            a = temp[i]
            if s[a] != s[i]:
                return s[:i]+s[a]+s[i+1:a]+s[i]+s[a+1:]
        return s
  
# Solution 2

def smalleststring(ip1,ip2):
        
    nw_string = ''
    b_list = sorted(ip2, key=str.lower)
    for i in b_list:
        nw_string += i

    return nw_string

ip2 = 'avlleeaavvvgghhhrrrwww'
ip1 = len(ip2)
print(User.smalleststring(ip1,ip2))