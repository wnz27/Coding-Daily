class Date:
    # 构造函数
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    def tomorrow(self):
        self.day += 1
    
    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)
    
if  __name__ == "__main__":
    new_day = Date(2019, 10, 16)
    print(new_day)
    new_day.tomorrow()
    print(new_day)
    '''
    这里没有传递任何东西，python解释器会自动把调用变成：tomorrow(new_day)，所以不用传递变量
    '''
    # 2019-10-16
    data_str = "2019-10-16"
    year, month, day = tuple(data_str.split("-"))
    

