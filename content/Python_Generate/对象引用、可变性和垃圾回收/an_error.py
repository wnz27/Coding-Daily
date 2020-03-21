#! -*- encoding=utf-8 -*-
def add(a, b):
    a += b
    return a

class Company:
    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs
    def add(self, staff_name):
        self.staffs.append(staff_name)
    def remove(self, staff_name):
        self.staffs.remove(staff_name)

if __name__ == "__main__":
    
    com1 = Company("com1", ["fzk1","fzk2","fzk3"])
    com1.add("fzk4")
    com1.remove("fzk1")
    print(com1.staffs)

    com2 = Company("com2")
    com2.add("fzk")
    print(com2.staffs)

    print(Company.__init__.__defaults__)

    com3 = Company("com3")
    com3.add("fzk5")
    print(com2.staffs)
    print(com3.staffs)
    print(com2.staffs is com3.staffs)
    '''
    在类定义的时候是一个空[]
    而[]是一个可变对象，com2和com3创建的时候都没有传递进list
    所以就共用了一个默认的list,所以就造成了冲突
    所以就解释了为什么com2和com3的staffs是一样的
    这个默认值用Company可以取到：
    '''
    print(Company.__init__.__defaults__)
    '''
    所以在没有传list进来的时候，就会取到这个__defaults__值
    而如果传进来了，staffs就会指向传进来的list
    '''

    print("*" * 80)
    a = 1
    b = 2
    c = add(a, b)
    print(c)
    print(a, b)

    print("*" * 80)

    d = [1,2]
    e = [3,4]
    f = add(d, e)
    print(f)
    print(d,e)

    print("*" * 80)

    g = (1,2)
    h = (3,4)
    i = add(g, h)
    print(i)
    print(g, h)

    print("*" * 80)
    '''
    我们发现在传入数字和元组的时候a都没有第一个数都没有受到影响，而list的第一个数受到了影响
    '''
    '''
    当我们传递一个list和dict进函数时候，我们心里要清楚，他们是有可能被更改的，
    add就是会把第一个参数的list修改，所以受到了影响
    '''

