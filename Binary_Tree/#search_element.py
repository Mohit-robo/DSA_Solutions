'''
https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

Search an element in a sorted and rotated array

An element in a sorted array can be found in O(log n) time via binary search. 
But suppose we rotate an ascending order sorted array at some pivot unknown to you beforehand. So for instance, 1 2 3 4 5 might become 3 4 5 1 2. 
Devise a way to find an element in the rotated array in O(log n) time.

Approach: 

    The idea is to find the pivot point, divide the array into two sub-arrays and perform a binary search.
    The main idea for finding a pivot is - for a sorted (in increasing order) and pivoted array, the pivot element is the only element for which the next element to it is smaller than it.
    Using the above statement and binary search pivot can be found.
    After the pivot is found divide the array into two sub-arrays.
    Now the individual sub-arrays are sorted so the element can be searched using Binary Search.

Implementation:  

Input arr[] = {3, 4, 5, 1, 2}
Element to Search = 1
  1) Find out pivot point and divide the array in two
      sub-arrays. (pivot = 2) /*Index of 5*/
  2) Now call binary search for one of the two sub-arrays.
      (a) If element is greater than 0th element then
             search in left array
      (b) Else Search in right array
          (1 will go in else as 1 < 0th element(3))
  3) If element is found in selected sub-array then return index
     Else return -1.

'''


def findpivot(arr,low ,high):

    if high < low:
        return -1
    
    if high == low:
        return low
    
    mid = int((low+high)/2)
    
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid

    if mid > low and arr[mid] < arr[mid - 1]:
        return (mid-1)

    if arr[mid] <= arr[low]:
        return findpivot(arr,low,(mid - 1))
    
    return findpivot(arr,(mid+1),high)

def binarysearch(arr,low,high,key):

    if high < low:
        return -1
    
    mid = int((low+high)/2)
    
    if arr[mid] == key:
        return mid
    
    if arr[mid] < key:
        return binarysearch(arr,(mid+1),high,key)

    return binarysearch(arr,low,(mid - 1),key)

def pivoted_binary_search(arr,high,key):
    
    pivot = findpivot(arr,0,(high-1))

    if pivot == -1:
        return binarysearch(arr,0,(high-1),key)
    
    if arr[pivot] == key:
        return pivot
    
    if arr[0] <= key:
        return binarysearch(arr,0,pivot -1,key)
    
    return binarysearch(arr,pivot + 1,(high-1),key)


arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
# arr1 = [30, 40, 50, 10, 20]
n = len(arr1)
key = 10
print("Index of the element is : ",
      pivoted_binary_search(arr1,n,key))