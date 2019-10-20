#! -*- encoding=utf-8 -*-
# clear 清空dict
a = {
    "fzk": {"company": "yuner"},
    "fzk2": {"company": "yuner2"}
}
# copy, 返回浅拷贝
new_dict = a.copy()
new_dict["fzk"]["company"] = "lalalal"
print(new_dict)
print("vs")
print(a)
print("a的地址为： %s" % id(a))
print("new_dict的地址为： %s" % id(new_dict))
# 浅拷贝影响原来的值

# 深拷贝需要引入python的copy模块调用deepcopy
import copy as cp
new_dict1 = cp.deepcopy(a)
new_dict1["fzk"]["company"] = "12344556"
print(a)
print("vs")
print(new_dict1)

# fromkeys, 第一个参数是接收一个iterable对象，第二个参数是生成的dict的value的默认值
new_list = ["yuenr1", "yuner2"]
new_dict2 = dict.fromkeys(new_list, {"company": "nimahai"})
print(new_dict2)

# setdefault
default_value = new_dict2.setdefault("fzk", "hahahahah")
print(default_value)
print(new_dict2)

# update
new_dict2.update({"1992": "0825"})
new_dict2.update(fzk="999",fzk2="888")
print(new_dict2)

# update也可以接收一个iterable对象,比如list里面放tuple的形式
new_dict2.update([("000","111"),("222","333"),("444","555")])
print(new_dict2)

# tuple里面放tuple也是可以的嘛
new_dict2.update((("666","777"),("888","999"),("aaa","bbb")))
print(new_dict2)