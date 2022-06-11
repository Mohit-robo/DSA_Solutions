'''
Exmaple 1:

Input: 

Two space spererated Strings
1 st: Original string eg: Bling
2 nd: Shuffled string eg  GlibN

Output:
3L1O2O4U0U

Conditions:
1: Index of each element present in the 2nd string of that in the 1st string
2: If case change:
    a: Upper to Lower -- 'L'
    b: Lower to Upper -- 'U'
    c: No change -- 'O'

In the above example 
Bling GlibN

B -- index 0 and Upper case changes to b index 3 lower case -- 3L      (index starting from 0)
l -- 1 lower case remains unchnaged -- 1O
i -- 2 lower case remains unchnaged -- 2O
n -- index 3 and lower case changes to N index 4 Upper case -- 4U
g -- index 4 and lower case changes to G index 0 Upper case -- 0U

Hence -- 3L1O2O4U0U


Example 2:

Input: 
Mohit moTiH

Output:
0L1O4U3O2U
'''

## This solution works when there are no duplicate elements

def find_transformations(in_n_out):

    seperated = in_n_out.split(' ', 1 )
    str_1,str_2 = str(seperated[0]),str(seperated[1])
    
    final = ''
    for i in range(len(str_1)):
        
        if str_1[i] == str_2[i]:
            i = str(i)
            final += (i+'O')
            # print("Matching: ",(str(i),'O'))
            # print("Matching: ",(i,str_1[i],str_2[i],'O'))
        else:
            for j in range(len(str_2)):
                if str_1[i] == str_2[j].upper():
                    j = str(j)
                    final += (j+'L')
                    # print("Matching Second: ",(j,'L'))
                elif str_1[i].upper() == str_2[j]:
                    j = str(j)
                    final += (j+'U')
                    # print("Matching Second: ",(j,'U'))

    return str(final)
    
in_n_out = input()

result = find_transformations(in_n_out)
print(result)

