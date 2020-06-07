# 如果一个单词通过循环右移获得的单词，我们称这些单词都为一种循环单词。 例如：picture 和 turepic 就是属于同一种循环单词。 现在给出n个单词，需要统计这个n个单词中有多少种循环单词。

def _match(s1,s2):
    s1 = list(s1)
    s2 = list(s2)
    if s1[0] in s2:
        start = s2.index(s1[0])
    else:
        return False
    flag = True
    for i in range(len(s1)):
        if s1[i]!=s2[(start+i)%len(s1)]:
            flag = False
            break
    return flag

n = int(input())
words = []
for i in range(n):
    words.append(str(input()))
i = 0
while i<len(words):
    j = i+1
    while j<len(words):
        if len(words[i])==len(words[j]):
            string = words[i]+words[i]
            if words[j] in string:
                del(words[j])
            else:
                j = j+1
        else:
            j = j+1
    i = i+1
print(len(words))
