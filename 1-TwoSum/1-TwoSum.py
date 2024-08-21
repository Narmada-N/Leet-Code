
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_indx = {}
        for i, itm in enumerate(nums):
            match = target - itm
            if match in dict_indx:
                return(dict_indx[match],i)
            dict_indx[itm]=i
            
