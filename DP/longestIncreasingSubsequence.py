class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #number of elements
        n = len(nums)
        #initialize the array holding subsequences lengths
        L = [1]*n
        #compute L[i] values in bottom up manner
        # do for each element in subarray `arr[0…i-1]`
        for i in range(1,n):
            #do for each element in subarray `arr[0…i-1]`
            for j in range(0,i):
                #find the longest increasing subsequence that ends with `arr[j]`
                #where `arr[j]` is less than the current element `arr[i]`
                if nums[j] < nums[i] and L[i] < L[j] + 1:
                    L[i] = L[j] + 1
                    
                    
        #find the longest increasing subsequence (having maximum length)
        #Initialize maximum to 0 to get the maximum of all LIS        
        maximum = 0
        for i in range(n):
            maximum = max(L[i],maximum)
        return maximum