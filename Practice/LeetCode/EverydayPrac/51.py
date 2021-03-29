# 83. 删除排序链表中的重复元素
# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。
#
# 返回同样按升序排列的结果链表。
#
# 示例 1：
#
# 输入：head = [1,1,2]
# 输出：[1,2]
#
# 示例 2：
#
# 输入：head = [1,1,2,3,3]
# 输出：[1,2,3]

#  递归

class Solution(object):
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
        else:
            move = head.next
            while move.next and head.val == move.next.val:
                move = move.next
            return self.deleteDuplicates(move)
        return head

# 时间复杂度：O(N)，每个节点访问了一次。
# 空间复杂度：O(N)，递归调用的时候会用到了系统的栈。

#  迭代

class Solution(object):
    def deleteDuplicates(self, head):
        if not head: return None
        prev, cur = head, head.next
        while cur:
            if cur.val == prev.val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return head

# 时间复杂度：O(N)，对链表每个节点遍历了一次；
# 空间复杂度：O(1)，只使用了常量的空间。
