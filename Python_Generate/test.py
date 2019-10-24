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
        left = 0        # 左起求的和
        # 遍历比较
        for i in range(len(nums)):
            if left * 2 == sum_nums - nums[i]:
                return i
            left += nums[i]
        return -1
# 值类型互不影响，开辟了新的内存空间
a = 1
b = a
a = 2
print(b)
print(id(a), id(b))

# 引用类型影响，他们指向同一个对象
c = {"age":2}
d = c
d["age"] = 3
print(c.get("age"))
print(id(c), id(d))
