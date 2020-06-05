#牛牛有一个鱼缸。鱼缸里面已经有n条鱼，每条鱼的大小为fishSize[i] (1 ≤ i ≤ n,均为正整数)，牛牛现在想把新捕捉的鱼放入鱼缸。鱼缸内存在着大鱼吃小鱼的定律。经过观察，牛牛发现一条鱼A的大小为另外一条鱼B大小的2倍到10倍(包括2倍大小和10倍大小)，鱼A会吃掉鱼B。考虑到这个，牛牛要放入的鱼就需要保证：
# 1、放进去的鱼是安全的，不会被其他鱼吃掉
# 2、这条鱼放进去也不能吃掉其他鱼
# 鱼缸里面已经存在的鱼已经相处了很久，不考虑他们互相捕食。放入的新鱼之间也不会相互捕食。现在知道新放入鱼的大小范围[minSize,maxSize](考虑鱼的大小都是整数表示),牛牛想知道有多少种大小的鱼可以放入这个鱼缸。

import sys
lines = sys.stdin.readlines()
minsize,maxsize =[int(i) for i in lines[0].split()]
n = int(lines[1])
fishsize = list(map(int, lines[2].split()))
k=0;
for i in range(minsize,maxsize+1):
    for j in range(0,len(fishsize)):
        if (i>=2*fishsize[j] and i<=10*fishsize[j]) or (i<=1/2*fishsize[j] and i>=1/10*fishsize[j]):
            k=k+1
            break
num= maxsize-minsize+1-k
print(int(num))



a1=raw_input()
a2=a1.split(' ')
a3=list(map(int,a2))
a_min=min(a3)
a_max=max(a3)
b1=raw_input()
b=int(b1)
c1=raw_input()
c2=c1.split(' ')
c3=list(map(int,c2))
c=list(c3)
d=list(range(a_min,a_max+1))
e=[]
for x in range(a_min,a_max+1):
    for y in c:
        if 2*x <= y <= 10* x or 2*y <= x <= 10*y:
            e.append(x)
        else:
            pass
f=set(d)
g=set(e)
h=len(f-g)
print(h)
