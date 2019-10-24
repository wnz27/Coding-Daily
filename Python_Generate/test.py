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
print(id(a), id(b))
a = 2
print(b)
print(id(a), id(b))

print("*" * 80)

# 引用类型影响，他们指向同一个对象
c = {"age":2}
d = c
print(id(c), id(d))
d["age"] = 3
print(c.get("age"))
print(id(c), id(d))

print("*" * 80)
# 值类型互不影响，开辟了新的内存空间
e = None
f = e
print(id(e), id(f))
f = "123"
print(e)
print(id(e), id(f))

print("*" * 80)
# 值类型互不影响，开辟了新的内存空间
g = True
h = g
print(id(g), id(h))
h = False
print(g)
print(id(g), id(h))
