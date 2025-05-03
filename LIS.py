#Longest Increasing subsequence

def length_of_LIS(nums):
    if not nums:
        return 
    # dp[i] will hold the length of LIS ending at index i
    dp = [1] * len(nums)
    # Fill dp array
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    # The answer is the maximum in dp
    return max(dp)
# Example usage
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print("Input list:", nums)
print("Length of Longest Increasing Subsequence:", length_of_LIS(nums))