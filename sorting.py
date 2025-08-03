# MERGE SORT
'''An array is divided into two equal parts until each elemnts become single and then the elements are arranged in 
the sorted order. After the sorting of the elemnts the array is merged
TIME COMPLEXITY = O(nlogn) in best,worst and average.1'''

class Solution(object):
    def merge(self,nums):  #FUNCTION FOR DIVIDING A ARRAY INTO 2 EQUAL PARTS AS LEFT AND RIGHT & ARRANGE THE ELEMENTS
        i=j=0
        k=0
        left= [low:mid+1]
        right= [mid+1:high+1]
        
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                nums[k]=left[i]
                i+=1
            else:
                nums[k]=right[j]
                j+=1
            i+=1
            j+=1
        while i < len(left) :
            nums[k]=left[i]
            i+=1
            k+=1           
        while j < len(right) :
            nums[k]=right[j]
            j+=1
            k+=1      
    def mergeSort(nums,low,mid,high):    #FUNCTION FOR MERGING LEFT & RIGHT BY ELEMENTS 
        if low<=high:
            mid(low+mid)//2
            mergeSort(nums,low,mid+1)
            mergeSort(nums,mid+1,high)
            merge(nums,low,mid,high)     
            
# SELECTION SORT
'''In selection sort, firstly the minimum number of elements is find and the  this minimum element is the is swaped
with the first element
TIME COMPLEXITY = O(N^2)
'''

class Solution(object):
    def selection_sort(arr):
        n=len(arr)
        for i in range(n):
            mini_index=i
            for j in range(i+1,n):
                if arr[j]<arr[mini_index]:
                    mini_index=j
            if mini_index != i:
                arr[i],arr[mini_index]=arr[mini_index],arr[i]   
                
# BUBBLE SORT
'''In bubble sort, greater number of elements always swap and placed at the last.....there is multiple passes occur
then entire array become sorted.........{do do elemnts he bss adjacent chck kr k max wal ko right side put krenge }

TIME COMPLEXITY = {BEST: O(N), AVG & WORST: O(N^2)}
SPACE COMPLEXITY = O(1)'''

class Solution(object):
    def bubble_sort(self,arr):
        n=len(arr)
        for i in range(n):           
            for j in range(0,n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j] 
        return arr       
    
#INSERTION SORT
'''Elements directly arrange in the sorted order simply by swapping 
TIME COMPLEXITY = {BEST: O(N), AVG: O(N^2), WORST:O(N^2)}'''

class Solution(object):
    def insertion_sort(self,arr):
        n=len(arr)
        for i in range(1,n):
            while j<=0 and arr[j+1]>key:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=key    
        return arr                     
                   
               