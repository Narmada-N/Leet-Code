
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        list_ele = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i+1
            right = len(nums)-1
            while(left<right):
                sum = nums[i]+nums[left]+nums[right]
                if sum == 0:
                    list_ele.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left +=1
                    right -=1
                elif sum>0:
                    right-=1
                else:
                    left+=1
        return list_ele

