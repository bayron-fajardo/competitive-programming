class Solution:
    def containsDuplicate(self, nums) -> bool:
        
        dic = set()
        for num in nums:
            if num in dic:
                return True
            dic.add(num)
            
        return False
    
        """
        dic = {
            
        }
        for num in nums:
            if num in dic:
                return True
            else:
                dic[num] = 1
        return False
        """