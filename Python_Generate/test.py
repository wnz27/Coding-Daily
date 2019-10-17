#! -*- encoding=utf-8 -*-

def pivotIndex(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 空数组
        if not nums:
            return -1
        
        sum_nums = sum(nums)
        left = 0        
        # 遍历比较
        for i in range(len(nums)):
            if left * 2 == sum_nums - nums[i]:
                return i
            left += nums[i]
        return -1