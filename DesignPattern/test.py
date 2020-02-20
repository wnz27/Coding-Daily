b = [1,7,5,9,2,12,3]
a = range(len(b))
c = {k:v for k,v in zip(a, b)}
print(c)
result = []
for value in b:
    if (value + 2) in b:
        result.append((value, value+2))
print(result)

d = "asdfasdf asdfafads asdfasdf"
s = d.split(' ')
g = '%20'.join(s)
print(g)
print(max(1, 1))

print("fzk".join(" 13 13 21 ".split(" ")))

from numpy import random
lala = random.randint(1,5, 10)
print("*"*40,lala)

print(list(range(0, 10, 3)))

a = [2,2,2,2,2,2,2]
b = []
print(max(b, default=100))