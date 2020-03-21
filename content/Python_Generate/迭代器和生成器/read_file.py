#! -*- encoding=utf-8 -*-
# 500G文件  实际上只有一行，但是有特殊的分隔符 {|}

def myreadLines(f, newline):
    '''
    newline：分隔符
    f：文档对象
    '''
    buf = ""
    while True:
        # 内循环剔除所有读取出来的内容的分隔符，并顺便输出内容
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]
        chunk = f.read(4096*10)
        if not chunk:
            # 说明已经读到结尾
            yield buf
            break
        buf += chunk

with open("input.txt") as f:
    for line in myreadLines(f, "{|}"):
        print(line)
