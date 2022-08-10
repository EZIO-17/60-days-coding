class Solution(object):
    def threeSum(self, nums):
        
        res, i = [], 0
        nums.sort()
        
        while i < len(nums):
            l, r = i + 1, len(nums)-1
            
            if i > 0 and nums[i] == nums[i-1]: i+=1; continue
            while l < r:
                
                sum_ = nums[i] + nums[l] + nums[r]
         
                if sum_ < 0:
                    l += 1
                
                elif sum_ > 0: r -= 1
                
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    
            i += 1
           
            
                    
        return res