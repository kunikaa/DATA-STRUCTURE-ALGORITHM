# MERGE SORT
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
                   
               