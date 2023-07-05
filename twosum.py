class Solution:
    def twoSum(self, nums:list[int], target:int) -> list[int]:
        for i in range(len(nums)):
            val = target - nums[i]
            if val in nums and i!=nums.index(val):
                return [i,nums.index(val)]

s = Solution()
res = s.twoSum([2,3,5,3],6)
print(res)
        
