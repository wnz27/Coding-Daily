#! -*- encoding=utf-8 -*-

class Date:
    # 构造函数
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    def tomorrow(self):  # 实例方法
        self.day += 1
    
    @staticmethod  # 不需要接受self, 缺点是类名修改，返回那里也需要修改。
    def parse_from_string(data_str):
        year, month, day = tuple(data_str.split("-"))
        return Date(int(year), int(month), int(day))
    
    # 比如要判断字符串是否合法，那么使用staticmethod更合适一些，因为不需要把类传递进来
    @staticmethod
    def valid_str(data_str):
        year, month, day = tuple(data_str.split("-"))
        if int(year) >0 and (int(month)>0 and int(month)<12) and (int(day) >0 and int(day)<31):
            return True
        else:
            return False

    @classmethod
    def from_string(cls, date_str):
        year, month, day = tuple(data_str.split("-"))
        return cls(int(year), int(month), int(day))
        
    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)
    
if  __name__ == "__main__":
    new_day1 = Date(2019, 10, 16)
    print(new_day1)
    new_day1.tomorrow()
    print(new_day1)
    print("#" * 100)
    '''
    这里没有传递任何东西，python解释器会自动把调用变成：tomorrow(new_day)，所以不用传递变量
    '''
    # 2019-10-16
    data_str = "2019-10-16"
    year, month, day = tuple(data_str.split("-"))
    new_day2 = Date(int(year), int(month), int(day))
    print(new_day2)
    print("#" * 100)

    # 用staticmethod完成初始化
    new_day3 = Date.parse_from_string(data_str)
    print(new_day3)
    print("#" * 100)

    # 用classmethod完成初始化
    new_day4 = Date.from_string(data_str)
    print(new_day4)
    print("#" * 100)

    # 判断字符串合法
    print(Date.valid_str("2019-08-33"))