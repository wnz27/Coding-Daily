#! -*- encoding=utf-8 -*-
import bisect

# 用来处理已排序的序列，用来维持已排序的序列， 升序
# 二分查找实现，效率高
inter_list = []
bisect.insort(inter_list,"c")
bisect.insort(inter_list,"b")
bisect.insort(inter_list,"e")
bisect.insort(inter_list,"a")
bisect.insort(inter_list,"f")
print(inter_list)

print(bisect.bisect(inter_list, "c"))
# bisect方法是返回这个值应该插入的位置，默认调用bisect_right，靠后
print(bisect.bisect_left(inter_list,"c"))
# bisect_left 靠前
