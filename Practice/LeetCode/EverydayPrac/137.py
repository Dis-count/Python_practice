# 203. Remove Linked List Elements
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
#
# Example 1:
#
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
#
# Example 2:
#
# Input: head = [], val = 1
# Output: []
#
# Example 3:
#
# Input: head = [7,7,7,7], val = 7
# Output: []

#  递归
# 通过递归的方法去删除节点

# 递归程序会先一路遍历来到节点尾部
# 从后往前把 val 符合的节点进行删除, 并重新把链表连接起来

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head

        # removeElement方法会返回下一个Node节点
        head.next = self.removeElements(head.next, val)
        if head.val == val:
            next_node = head.next
        else:
            next_node = head
        return next_node

# 时间复杂度: O(n)
# 空间复杂度: O(1)


#  迭代
# 新增一个 dummy 节点, 方便遍历和最后返回结果
# p 指针向后遍历, 向前探一个节点, 如果 val 相等, 则需要跳过 next 节点

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        p = dummy
        while p is not None:
            # 向前探一个节点检查是否等于val
            if p.next and p.next.val == val:
                # 跳过 p.next 节点
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next
