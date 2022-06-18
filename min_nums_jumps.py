'''

Given an array of integers where each element represents the max number of steps that can be made forward from that element. 
The task is to find the minimum number of jumps to reach the end of the array (starting from the first element). 
If an element is 0, then cannot move through that element.

Solution: This problem is famously called as end of array problem. We want to determine the minimum number of jumps required in order to reach the end. 
The element in the array represents the maximum number of jumps that, that particular element can take.

Let us understand how to approach the problem initially. 

We need to reach the end. Therefore, let us have a count that tells us how near we are to the end. Consider the array A=[1,2,3,1,1]

```
In the above example we can go from 
> 2 - >3 - > 1 - > 1 - 4 jumps
1 - > 2 - > 1 - > 1 - 3 jumps
1 - > 2 - > 3 - > 1 - 3 jumps
```

Hence, we have a fair idea of the problem. Let us come up with a logic for the same. 

Let us start from the end and move backwards as that makes more sense intuitionally. We will use variables right and prev_r denoting previous right to keep track of the jumps. 

Initially, right = prev_r = the last but one element. We consider the distance of an element to the end, and the number of jumps possible by that element. 
Therefore, if the sum of the number of jumps possible and the distance is greater than the previous element, 
then we will discard the previous element and use the second element’s value to jump.
Try it out using a pen and paper first. The logic will seem very straight forward to implement. 
Later, implement it on your own and then verify with the result.

'''

def min_jmp(arr):

    n = len(arr)
    right = prev_r = n-1
    count = 0
    
    # We start from rightmost index and travesre array to find the leftmost index
    # from which we can reach index 'right'
    while True:
        for j in (range(prev_r-1,-1,-1)):
            if j + arr[j] >= prev_r:
                right = j
                
        if prev_r != right:
            prev_r = right
        else:
            break

        count += 1

    return count if right == 0 else -1

# Enter the elements separated by a space
arr = list(map(int, input().split()))
print(min_jmp(n, arr))
