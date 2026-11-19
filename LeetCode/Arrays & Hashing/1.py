class Solution:
    def twoSum(self, nums:list[int], target:int):
        
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in hashmap:
                return [hashmap[complement], i]
            else:
                hashmap[nums[i]] = i
        
        return None