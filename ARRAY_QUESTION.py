#LARGEST ELEMENT OF THE ARRAY
class Solution(Object):
    def largest(slef,arr):
        largest=arr[0]
        for i in range(len(arr)):
            if arr[i]>largest:
                largest=arr[i]
        return largest

#SECOND LARGEST ELEMETNS OF THE ARRAY
class Solution(Object) :
    def secondLargest(self,arr):
        largest=arr[0]
        second_largest=-1
        for i in range(len(arr)):
            if arr[i]>largest:
                second_largest=largest
                largest=arr[i]
            elif arr[i] < largest and  arr[i] > second_largest :          
                second_largest = arr[i]
        return second_largest   

#CHECKING ARRAY IS SORTED OR NOT
class Solution(Object):
    def sorted(self,arr):
        if arr[i]<=arr[i-1]:
            return True
        return False

# REMOVES DUPLICATES IN THE PLACE FROM SORTED ARRAY
class Solution(Object):
    def removeDuplicates(self,k,arr)
        k=0
        for i in range(len(arr)):
            if arr[i]!=arr[k]:
                arr[k]=arr[i]
                k+=1
        return k    
               
# LEFT ROTATE THE ARRAY BY  "D" PLACES
class Solution(object):
    def rotate(self,arr):
        n=len(arr) 
        d=d%n
        rotate= arr[-d:] + arr[:-d]
        for i in range(n):
            nums[i]=rotate[i]   

#MOVE ALL THE ZEROS TO THE END OF THE ARRAY 
class Solution(Object):
    def removeZeros(self,arr):
        n=len(arr)
        k=0
        for i in range(n):
            if arr[i]!=0:
                arr[k]=arr[i]
                k+=1
        for i in range(k,n):
            nums[i]=0
         
# LINEAR SEARCH
class Solution(Object):
    def linearSerach(self,arr,target):
        for i in range(len(arr)):
            if arr[i]==target:
                return i
            else:
                return -1

#UNION OF TWO SORTED ARRAY
class Solution(Object):
    def unionOfArray(self,arr1,arr2):
        i=j=0
        result=[]
        while i<=len(arr1) and j<=len(arr2):
            if arr1[i]==arr2[j]:
                if not in result or result[-1]!=arr1[i]:
                    result.append(arr[i])
                i+=i
                j+=1
            elif arr1[i]<arr2[j]:
                result.appen(arr1[i])
                i+=1
            else:
                result.append(arr1[j])
                j+=1    
        while i<len(arr1):
            if result[-1]!=arr1[i]:
                result.append(arr1[i])
            i+=1  
        while j<len(arr2):
            if result[-1]!=arr2[j]:
                result.append(arr2[j])
            j+=1  
        print(result)  
        
# INTERSECTION OF TWO SORTED ARRAY
class Solution(Object):
    def intersectionOfArray(self,arr1,arr2):
        i=j=0
        result=[]
        while i<=len(arr1) and j<=len(arr2):
            if i<0 and arr1[i]==arr1[i-1]:
                i+=1
                continue
            elif arr1[i] == arr2[j]:
                result.append(arr1[i])
                i+=1
                j+=1
            elif i<len(arr1):
                result.append(arr1[i])
                i+=1
            else:
                result.append(arr2[j])
                j+=1    
        print(result)        

# MISSING "N" NUMBERS  FROM ARRAY
class Solution(Object):
    def missingElements(self,arr,n):
        actual_sum=0
        for i in range (len(arr)):
            actual_sum+=arr[i]
        total_sum=n*(n+1)//2
        return (total_sum - actual_sum) 
    
#MAXIMUM CONSECUTIVE ONE
class Solution(Object):
    def consecutiveElement(self,nums):
        if not nums:
            return 0
        max=1            #max number of occurence
        count=1          #vo no. tbhi tk count hoga jb tk consecutivness break na ho
        for i in range(len(nums)):
            if arr[i]==arr[i-1]:
                count+=1
                if count>max:
                    max=count
            else:
                count=1
        return max

# FIND THE NUMBER WHICH APPEARS ONCE, AND THE OTHER TWICE
class Solution(Object):
    def unique(self,nums):
        result=0
        for num in nums:
            result = result ^ num
        return result    
                      
# VALID PARANTHESIS
class Solution(Object):
    def validParanthesis(self,s):
        stack=[]
        hashmap={")":"(", "]":"[", "}":"{"}  
        for i in s:
            if i in hashmap:
                if stack and stack[-1]==hashmap[i]:
                    stack.pop()
                else:
                    return False    
            else:    
                stack.append(i)                        
        return not stack
                            
# FIRST AND LAST POSITION OF THE ELEMENTS IN THE  SORTED ARRAY                          
class Solution(Object):
    def firstAndLast(self,nums,target):
        start= -1
        end= -1
        for i in range(len(nums)):
            if nums[i]==target:
                if start==-1:
                    start=i
                end=i   
        return (start,end)
# SEARCH INSERT POSITION 
class Solution(object):
    def searchInsertPosition(self,nums,target):
        for i in range(len(nums)):
            if nums[i]== target:
                return i        
        return len(nums)          #in the case when the elemnets is not present then return the expected place

#SEARCH IN A 2D ARRAY
class Solution(object):
    def searchInMatrix(self,matrix,target) :
        if not in matrix or not matrix[0]:
            return False
        row=len(matrix)
        cols=len(matrix[0])
        
        low=0
        high=(row*cols) -1
        
        while low<=high:
            mid=(low+high)//2
             row=mid//cols
            columns=mid%cols
            mid_value=matrix[row][cols]
            
            if mid_value==target:
                return True
            elif mid_value<target:
                low=mid+1
            else:
                high= mid+1    
        return False        
           
#LEADER IN AN ARRAY
class Solution(Object):
    def leader(self,arr):
        n=(len(arr))
        leaders=[]
        max_from_right=arr[-1]
        leaders.append(max_from_right)
        for i in range(n-2,-1,-1):
            if arr[i]>max_from_right:
                max_from_right=arr[i]
                leaders.append(max_from_right)  
        leaders.reverse()  
        return leaders       
    
# MAXIMUM SUBARRAY SUM
class Solution(object):
    def maximum_subarray(self,arr):
        max_sum=[0]
        current_sum=arr[0]            
        for i in range(len(arr)):
            current_sum=max(current_sum + arr[i], current_sum)   
            max_sum=(max_sum,current_sum) 
        return max_sum 
# FIND THE DUPLICATE NUMBER IN THE ARRAY
class Solution(Object):
    def duplicateNumber(self,nums):
        seen=set()                             #finding duplicate using hashset
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
            
# REARRANGE THE ELEMENTS BY THE SIGN
class Solution (Object):
    def rarrangement(self,arr):
        pos=[]
        neg=[]
        for i in range(len(arr)):
            if arr[i]>0:
                pos.append(arr[i])
            else:
                neg.append(arr[i])  
        result=[]
        for i in range(len(pos)):
            result.append(pos[i])     
            result.append(neg[i])                    
        return result 
    
#in the case there are more numbers as negative or positive
i=j=0
while i<=len(pos) and j<=len(neg):
    result.append(pos[i])     
    result.append(neg[i])
    i+=1
    j+=1
while i<=len(pos):
    result.append(pos[i])  
    i+=1
while j<=len(neg):
    result.append(neg[i])
    j+=1
return result    
    
        
               
                    
                                      