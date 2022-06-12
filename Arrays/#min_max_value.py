'''
Write a function to return minimum and maximum in an array. Your program should make the minimum number of comparisons. 

https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/
'''

'''
Initialize values of min and max as minimum and maximum of the first two elements respectively.
Starting from 3rd, compare each element with max and min, and change max and min accordingly 
(i.e., if the element is smaller than min then change min, else if the element is greater than max then change max, else ignore the element) 

'''

### Linear Search ###
import time

class pair():
    def __init__(self):
        self.max = 0
        self.min = 0

def getminmax(arr : list):

    minmax = pair()

    len_of_array = len(arr)

    if len_of_array == 1:
        minmax.max = arr[0]
        minmax.min = arr[0]
        return minmax

    if arr[0] > arr[1]:
        minmax.max = arr[0]    
        minmax.min = arr[1]
    else:
        minmax.min = arr[0]    
        minmax.max = arr[1]    

    for i in range (2,len_of_array):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]
    
    return minmax

start = time.time()

arr = [1000, 11, 445, 1, 330, 3000]
arr_size = 6
minmax = getminmax(arr)
print("Minimum element is", minmax.min)
print("Maximum element is", minmax.max)

end = time.time()

print("Time Taken to run:",(end - start)*1000)


##########  Recusion Method ########
'''
Divide the array into two parts and compare the maximums and minimums of the two parts to get the maximum and the minimum of the whole array.

Pair MaxMin(array, array_size)
   if array_size = 1
      return element as both max and min
   else if arry_size = 2
      one comparison to determine max and min
      return that pair
   else    /* array_size  > 2 */
      recur for max and min of left half
      recur for max and min of right half
      one comparison determines true max of the two candidates
      one comparison determines true min of the two candidates
      return the pair of max and min

'''

def minmax_recur(arr:list,low ,high ):

    arr_max = arr[low]
    arr_min = arr[low]

    if high == low:
        arr_max = arr[high]
        arr_min = arr[low]
        return (arr_min,arr_max)
    
    elif high == low+1:
        if arr[low] > arr[high]:
            arr_max = arr[low]    
            arr_min = arr[high]
        else:
            arr_min = arr[low]    
            arr_max = arr[high]
        return (arr_min, arr_max)
    else:
        mid = int((high+low)/2)

        arr_1_min,arr_1_max = minmax_recur(arr,low,mid)
        arr_2_min,arr_2_max = minmax_recur(arr,mid + 1, high)
    
    return (min(arr_1_min,arr_2_min),max(arr_1_max,arr_2_max))


arr = [1000, 11, 445, 1, 330, 3000,3000]
high = len(arr) - 1
low = 0

start_rec = time.time()
min_val,max_val = minmax_recur(arr,low,high)

print("Max value: ",max_val)
print("MIN value: ",min_val)

end_rec = time.time()

print("Time Taken to run rec:",(end_rec - start_rec)*1000)
