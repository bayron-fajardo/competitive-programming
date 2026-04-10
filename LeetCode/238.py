#Product of Array Except Self
"""
Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""
def productExceptSelf(self, nums):
        resultado = []
        L = []
        R = []
        acum = 1
        for i in range(len(nums)):
            L.append(acum)
            acum *= nums[i]
        
        acum = 1
        for i in range(len(nums)-1,-1,-1):
            R.append(acum)
            acum *= nums[i]

        R.reverse()
        for i in range(len(nums)):
            resultado.append(R[i] * L[i])
