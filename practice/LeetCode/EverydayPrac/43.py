# 给你单链表的头节点 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
#
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        count = 1
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while pre.next and count < left:
            pre = pre.next
            count += 1
        cur = pre.next
        tail = cur
        while cur and count <= right:
            nxt = cur.next
            cur.next = pre.next
            pre.next = cur
            tail.next = nxt
            cur = nxt
            count += 1
        return dummy.next

# 时间复杂度：O(N)
# 空间复杂度：O(1)

# https://leetcode-cn.com/problems/reverse-linked-list-ii/solution/dong-hua-tu-jie-fan-zhuan-lian-biao-de-z-n4px/
