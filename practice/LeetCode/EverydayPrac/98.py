# 递归 / DFS

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employees_dict = {employee.id: employee for employee in employees}

        def dfs(employee_id):
            employee = employees_dict[employee_id]
            return employee.importance + sum(dfs(emp_id) for emp_id in employee.subordinates)

        return dfs(id)

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
