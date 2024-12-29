class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1

        nums = sorted(list(set(nums)))

        hit = 0
        for i in range(len(nums)):
            if nums[i]>0:
                nums = nums[i:]
                hit = 1
                break       
        if not hit:
            return 1

        # print("nums:", nums)

        if not nums:
            return 1

        if nums[0]>1:
            return 1

        elif (nums[-1]-nums[0]==len(nums)-1):
            return nums[-1]+1
        else:
            for i in range(0,len(nums)-1):
                if nums[i+1]-nums[i]>1:
                    return nums[i]+1
 