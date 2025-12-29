#! -*- encoding=utf-8 -*-
# Python生成器的send()方法详解 - 向生成器传递值

'''
生成器的双向通信：

1. 生成器的两大功能：
   - 可以产出值（yield）
   - 可以接收值（send）

2. send()方法的作用：
   - 传递值进入生成器内部
   - 重启生成器执行到下一个yield
   - 返回yield表达式的值

3. 启动生成器的两种方式：
   - next(gen)      # 方法1
   - gen.send(None) # 方法2

4. 重要规则：
   - 在调用send发送非None值之前，必须先启动生成器
   - 可以用next(gen)或gen.send(None)启动
'''

print("=" * 50)
print("生成器的send()方法详解")
print("=" * 50)

def gen_func():
    """可以接收和产出值的生成器
    
    功能：
    1. 可以产出值（yield）
    2. 可以接收值（调用方通过send传递进来）
    
    Yields:
        str: URL地址
        int: 数字
        
    Returns:
        str: 最终返回"fzk"
    """
    # 第一个yield：产出URL
    html = yield "http://projectsedu.com"
    print(f"接收到的html内容: {html}")
    
    # 第二个yield：产出2
    yield 2
    
    # 第三个yield：产出3
    yield 3
    
    # return会抛出StopIteration异常，值在value属性中
    return "fzk"


if __name__ == "__main__":
    print("""
    send()方法的特点：
    1. 可以传递值进入生成器内部
    2. 同时重启生成器执行到下一个yield位置
    3. 返回下一个yield表达式的值
    """)
    
    # ==================== 方法1：使用next()启动 ====================
    print("\n" + "=" * 50)
    print("方法1：使用next()启动生成器")
    print("=" * 50)
    
    gen = gen_func()
    # 第一步：使用next()启动生成器，执行到第一个yield
    url = next(gen)
    print(f"1. 从生成器获取URL: {url}")
    
    # 模拟下载URL后的html内容
    html = "<html>fzk's page</html>"
    
    # 第二步：使用send()传递html并获取下一个值
    result = gen.send(html)
    print(f"2. 发送html并获取下一个值: {result}")
    
    # ==================== 方法2：使用send(None)启动 ====================
    print("\n" + "=" * 50)
    print("方法2：使用send(None)启动生成器")
    print("=" * 50)
    
    gen = gen_func()
    # 第一步：使用send(None)启动生成器
    url = gen.send(None)  # 等价于next(gen)
    print(f"1. 从生成器获取URL: {url}")
    
    # 模拟下载URL后的html内容
    html = "<html>fzk's page</html>"
    
    # 第二步：使用send()传递html
    result = gen.send(html)
    print(f"2. 发送html并获取下一个值: {result}")
    
    print("\n" + "=" * 50)
    print("总结")
    print("=" * 50)
    print("""
    send()方法的执行流程：
    
    1. 启动阶段：
       gen = gen_func()        # 创建生成器对象
       url = next(gen)         # 或 gen.send(None)
       # 执行到第一个yield，返回URL
    
    2. 发送阶段：
       result = gen.send(html) # 发送html给生成器
       # html被赋值给第一个yield表达式
       # 继续执行到下一个yield
       # 返回2
    
    3. 关键点：
       - send(None) 等价于 next()
       - 第一次必须用send(None)或next()
       - send(非None值)会把yield表达式的值设为发送的值
       - send()返回下一个yield的值
    
    4. 应用场景：
       - 协程：实现协程的双向通信
       - 流程控制：根据上一步结果决定下一步操作
       - 数据管道：构建数据处理管道
    """)