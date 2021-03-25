# 82. 删除排序链表中的重复元素 II
# 存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。
#
# 返回同样按升序排列的结果链表。
#
# 示例 1：
#
# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
#
# 示例 2：
#
# 输入：head = [1,1,1,2,3]
# 输出：[2,3]

# 方法一：递归

# 1.1 递归函数定义
# 1.2 递归终止条件
# 1.3 递归调用
# 1.4 返回结果

class Solution(object):
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
        else:
            move = head.next
            while move and head.val == move.val:
                move = move.next
            return self.deleteDuplicates(move)
        return head

# 时间复杂度：O(N)，每个节点访问了一次。
# 空间复杂度：O(N)，递归调用的时候会用到了系统的栈。

# 方法二：一次遍历
# 这里说的一次遍历，是说一边遍历、一边统计相邻节点的值是否相等，如果值相等就继续后移找到值不等的位置，然后删除值相等的这个区间。

class Solution(object):
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        while cur:
            # 跳过当前的重复节点，使得cur指向当前重复元素的最后一个位置
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if pre.next == cur:
                 # pre和cur之间没有重复节点，pre后移
                pre = pre.next
            else:
                # pre->next指向cur的下一个位置（相当于跳过了当前的重复元素）
                # 但是pre不移动，仍然指向已经遍历的链表结尾
                pre.next = cur.next
            cur = cur.next
        return dummy.next

# 时间复杂度：O(N)，对链表每个节点遍历了一次；
# 空间复杂度：O(1)，只使用了常量的空间。

# 方法三：利用计数，两次遍历

# 这个做法忽略了链表有序这个性质，使用了两次遍历，第一次遍历统计每个节点的值出现的次数，
# 第二次遍历的时候，如果发现 head.next 的 val 出现次数不是 1 次，则需要删除 head.next。

class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next
        counter = collections.Counter(val_list)
        head = dummy
        while head and head.next:
            if counter[head.next.val] != 1:
                head.next = head.next.next
            else:
                head = head.next
        return dummy.next

# 时间复杂度：O(N)，对链表遍历了两次；
# 空间复杂度：O(N)，需要一个字典保存每个节点值出现的次数。
