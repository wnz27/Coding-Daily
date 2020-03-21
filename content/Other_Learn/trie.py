'''
@Author: 27
@LastEditors: 27
@Date: 2020-03-20 02:36:12
@LastEditTime: 2020-03-20 04:10:16
@FilePath: /Coding-Daily/Other_Learn/trie.py
@description: type some description
'''
'''
尝试实现trie字典树，也叫前缀树
'''
class Node:
    def __init__(self, isWord=False):
        self.is_word = isWord       # bool
        self.next = {}              # k:字符 ：v:node

class VocabularyTrie:
    def __init__(self):
        self.root = Node()
        self.size = 0
    
    # 获得树中存储的单词数
    def getSize(self):
        return self.size
    
    # 向trie中添加一个新的单词word
    def add(self, word):
        cur = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in cur.next:
                cur.next[char] = Node()
            cur = cur.next[char]
        if not cur.is_word:     # 当前word不在的时候才设置size，因为上面的循环有可能每次都判断在字典里
            cur.is_word = True
            self.size += 1
    
    # 查询单词word是否在Trie中
    def contains(self, word):
        cur = self.root
        for i in word:
            if i in cur.next:
                cur = cur.next[i]
            else:
                return False
        # if cur.is_word:
        #     return True
        # else:
        #     return False
        return cur.is_word
    
    def __str__(self):
        q = []
        q.append(self.root)
        res = "root::"
        while q:
            tem = q.pop(0)
            for k,v in tem.next.items():
                q.append(tem.next[k])
                res += k + ","
        res += "::end"
        return res
       
v = VocabularyTrie()
print(v.size)
v.add("word")
v.add("panda")
v.add("pan")
print(v.size)
print(v)
