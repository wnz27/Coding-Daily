#! -*- encoding=utf-8 -*-
# 实现可切片对象, 该例子只实现sequence，即不可修改序列
import numbers
class Group:
      # 支持切片操作
    def __init__(self, group_name, company_name, staffs):
        '''
        group_name      组名
        company_name    所属公司名
        staffs          员工，list
        '''
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs
    
    def __reversed__(self):
        self.staffs.reverse()
    
    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.group_name,staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.group_name,staffs=[self.staffs[item]])

    def __len__(self):
        return len(self.staffs)
    
    def __iter__(self):
        return iter(self.staffs)
    
    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False
    
staffs = ["fzk1", "fzk2", "fzk3", "fzk4"]
group = Group(company_name="imooc", group_name="user", staffs=staffs)
a = group[:2]
print(a.staffs)
print(len(group))
if "fzk1" in group:
    print("yes!")

for user in group:
    print(user)

reversed(group)
for user in group:
    print(user)