class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list
    
    def __getitem__(self, item):
        return self.employee[item]

company = Company(["tom", "bob", "jane"])

employee = company.employee
for em in employee:
    print(em)

'''
输出：
tom
bob
jane
'''
'''
以双下划线开头，以双下划线结尾的方法,一定使用python提供给我们的魔法函数
魔法函数为了增强自建类的特性
'''
for em in company:
    print(em)
'''
输出：
tom
bob
jane
说明会自动去找构建时list里的值，for循环会自动找迭代器，而__iter__才会
生成迭代器，pyhton自身的优化就是在for拿不到迭代器的时候，会找这个__getitem__，
会一次一次的把数据全部取完。
'''
