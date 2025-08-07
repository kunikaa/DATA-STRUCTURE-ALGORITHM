#print numbers 1 to n 
'''n=5
for i in range (1,n+1):
    print (i)
    '''
    
#print n to 1
'''
n=10
for i in range(n,0,-1):
    print(i)    
'''

#print sum of N numbers
'''
n=5
sum=0
for i in range(1,n+1):
    sum=sum+i
print (sum)    
 '''
#print fibbonacci number               WITHOUT RECURSION
'''
n=8
if n<=0:
    print (n)
previous=0
current=1
for i in range(2,n+1):
    next=previous + current
    previous=next
    current=next
print(current)  '''   

#WITH RECURSION
'''
def fibo(n):
    if n==0:
        return(0)
    elif n==1:
        return(1)
    else:
        for i in range (n):
            return (fibo(n-1) + fibo(n-2))
print(fibo(3))        
''' 
