# Given a list of integers, moves all zeros to end while maintaing the releative order of non - zero elements.


nums=[0,1,0,3,12]

def moveZeros(nums):
    insertPostion=0

    for num in nums:
        if num!=0:
            nums[insertPostion]=num
            insertPostion+=1  

    while insertPostion < len(nums):
        nums[insertPostion]=0
        insertPostion+=1

    return nums

print(moveZeros(nums))              





