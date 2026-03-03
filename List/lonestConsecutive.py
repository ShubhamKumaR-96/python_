# Given an unsorted list. find the length of longest consecutive element sequence
nums = [100, 4, 200, 1, 3, 2]

def longestConsecutive(nums):
    if not nums:
        return 0

    nums.sort()
    
    longest = 1
    current_length = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            continue  # duplicate ignore karo
        elif nums[i] == nums[i - 1] + 1:
            current_length += 1
        else:
            longest = max(longest, current_length)
            current_length = 1

    return max(longest, current_length)


print(longestConsecutive(nums))