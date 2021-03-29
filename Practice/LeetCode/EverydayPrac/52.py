# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。

# 输入：head = [1,2,3,4,5], k = 2
# 输出：[4,5,1,2,3]

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next: return head
        # 求链表长度
        _len = 0
        cur = head
        while cur:
            _len += 1
            cur = cur.next
        # 对长度取模
        k %= _len
        if k == 0: return head
        # 让 fast 先向后走 k 步
        fast, slow = head, head
        while k:
            fast = fast.next
            k -= 1
        # 此时 slow 和 fast 之间的距离是 k；fast 指向第 k+1 个节点
        # 当 fast.next 为空时，fast 指向链表最后一个节点，slow 指向倒数第 k + 1 个节点
        while fast.next:
            fast = fast.next
            slow = slow.next
        # newHead 是倒数第 k 个节点，即新链表的头
        newHead = slow.next
        # 让倒数第 k + 1 个节点 和 倒数第 k 个节点断开
        slow.next = None
        # 让最后一个节点指向原始链表的头
        fast.next = head
        return newHead

# 时间复杂度：O(N)
# 空间复杂度：O(1)
