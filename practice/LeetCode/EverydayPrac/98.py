# 690. Employee Importance
# You are given a data structure of employee information, which includes the employee's unique id, their importance value and their direct subordinates' id.
#
# For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.
#
# Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all their subordinates.
#
# Example 1:
#
# Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
# Output: 11
#
# Explanation:
# Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
#
# Note:
#
# One employee has at most one direct leader and may have several subordinates.
# The maximum number of employees won't exceed 2000.

# 递归 / DFS

# Definition for Employee.
from typing import List
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employees_dict = {employee.id: employee for employee in employees}

        def dfs(employee_id):
            employee = employees_dict[employee_id]
            return employee.importance + sum(dfs(emp_id) for emp_id in employee.subordinates)

        return dfs(id)

employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
id = 1
b = []
for i in employees:
    b.append(Employee(i[0],i[1],i[2]))
b[0].id
for i in b:
    print(i.id)
# 想想怎么用 list 加入 list  append, insert

a  = Solution()
a.getImportance(employees, id)

# 时间复杂度：O(n)
# 空间复杂度：O(n)

# 迭代 / BFS
# 另外一个做法是使用「队列」来存储所有将要计算的 Employee 对象，每次弹出时进行统计，并将其「下属」添加到队列尾部。

# 其实用队列用栈都没问题哒~因为每个员工只有一个直系领导
# 虽然写着 queue 但实际上是 stack (因为写的时候想着python的pop()比pop(0)要快不少)

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # hashmap 是 id -> emoloyees 下标的映射
        n = len(employees)
        imp = dict()
        for i in range(n):
            imp[employees[i].id] = i
        ans = 0
        queue = [imp[id]]
        while queue:
            cur = queue.pop()
            ans += employees[cur].importance
            for sub in employees[cur].subordinates:
                queue.append(imp[sub])
        return ans

# 时间复杂度：O(n)
# 空间复杂度：O(n)
