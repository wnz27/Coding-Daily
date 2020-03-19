'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-19 12:04:52
@LastEditTime: 2020-03-20 05:08:22
@FilePath: /Coding-Daily/self-problem/习题1/p1.py
@description: type some description
'''
'''
1. 请实现一个 Python 方法：输入一组域名，返回一个正则，
使其能判断一个 URL 是否在这些域名下
思路：
正则确实很不熟，但是我查了查，正则是回溯，而且如果遇见* ? 
会进行贪婪匹配，尝试各种匹配组合，会非常慢，复杂度是指数级，
所以我尝试其他的方式解决这个需求。
如果实现一个前缀字典树，自己去一个一个从根节点往下找，
只要找到某个节点且该节点标记为终止节点，那一路的寻找路径就是父域名了，
而且是最短父域名。
所以暂时假设一组域名用list传进来。
暂时定每段字符对应一个节点，那这样的话复杂度应该是O(段数)？貌似没错吧。。。
这样的话效率肯定很高，等下写完再看下复杂度
'''
class Node:
    def __init__(self, isSeg=False):
        self.isSeg = isSeg      # 在这个节点是否是一段域名
        self.next = {}          # 存储：segment(str) : Node
class URLTrie:
    def __init__(self):
        self.size = 0   # 可以统计传入的域名个数
        self.root = Node()
    def getSize(self):
        return self.size
    def add(self, formated_domain):
        cur = self.root
        for segment in formated_domain[::-1]:
            if segment not in cur.next:
                cur.next[segment] = Node()
            cur = cur.next[segment]
        if not cur.isSeg:
            cur.isSeg = True
            self.size += 1
    def isPrefix(self, formated_domain):
        '''
        写到这发现正着加有问题，判断子域名的话，前缀作用不大，
        字典树应该从后往前匹配。而且从头往尾添加的话头是不齐的，尾巴是齐的
        往往第一个可能就匹配不到，但是尾巴不会骗人~~，所以改一下添加的策略，
        反着添加，查询前缀
        '''
        cur = self.root
        for segment in formated_domain[::-1]:
            if segment not in cur.next:
                return False
            else:
                cur = cur.next[segment]
        # 反向无需关心标识，利用标识是完全匹配，肯定是有问题的。
        # 只要都在树里，那么就是子域名了,也就是前缀查询
        return True
        
class HandleURL:
    def __init__(self, domain_list):
        '''
        思考这个需求是内部使用的话貌似不需要对输入做验证吧？？
        做验证的话正则？还是第三方验证框架（没必要？）？
        '''
        self.urlTrie = self.__generate_url_trie(domain_list)
    def __generate_url_trie(self, raw_domain_list):
        '''
        构建字典树, 深度优先即可，从顶级域名加起
        '''
        # 拿到格式化好的二元数组
        format_domain_list = self.__format_domain_list(domain_list)
        urltrie = URLTrie()
        for formated_domain in format_domain_list:
            urltrie.add(formated_domain)
        return urltrie

    def __format_domain_list(self, raw_domain_list):
            '''
        辅助构建字典树，格式化一下传进来的域名字符串列表去掉点保留顺序，
        变成列表
        O(n), 与所给域名个数有关
        '''
        res = []
        for raw_domain in domain_list:
            res.append(self.__format_domain(raw_domain))
        return res

    def __format_domain(self, raw_domain):
        '''
        单一的格式化domain的方法，因为最后判断域名的那个方法可以使用
        返回分割好的list
        '''
        return domain.replace(".", " ").replace("/", " ").replace(":", " ").split()
   
    
    def judge_domain_is_in(self, row_domain):
        '''
        这个方法里使用我们构建的字典树self.urlTrie
        来判断url是否在这些域名之下
        '''
        domain = self.__format_domain(row_domain)
        return self.urlTrie.isPrefix(domain)
    

