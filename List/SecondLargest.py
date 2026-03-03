# Write a function  to find the second largest element in a list without using any built in sorting functions

nums=[12,35,1,10,34,1]

def secondMax(nums):

    if (len(nums)< 2):
        return None

    firstMax=float('-inf')

    secMax=float('-inf')

    for num in nums:
        if num > firstMax:
            secMax=firstMax
            firstMax=num
        elif firstMax > num > secMax:
            secMax=num  

    if secMax==float('-inf'):
        return None
                
    return secMax

print(secondMax([1,2]))        
            