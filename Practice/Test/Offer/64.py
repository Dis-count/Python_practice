# 滑动窗口最大值
# 给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。


# 1. 利用python性质每次求固定size的最大值，时间复杂度O(n*size)

res, i = [], 0
while size > 0 and i + size - 1 < len(num):
    res.append(max(num[i:i + size]))
    i += 1
return res

# 2. 双向队列，queue存入num的位置，时间复杂度O(n)

queue,res,i = [],[],0
while size>0 and i<len(num):
    if len(queue)>0 and i-size+1 > queue[0]: #若最大值queue[0]位置过期 则弹出
        queue.pop(0)
    while len(queue)>0 and num[queue[-1]]<num[i]: #每次弹出所有比num[i]的数字
        queue.pop()
    queue.append(i)
    if i>=size-1:
        res.append(num[queue[0]])
    i += 1
return res
