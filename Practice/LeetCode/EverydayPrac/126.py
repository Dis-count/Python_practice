# 1190. Reverse Substrings Between Each Pair of Parentheses
# You are given a string s that consists of lower case English letters and brackets.
#
# Reverse the strings in each pair of matching parentheses, starting from the innermost one.
#
# Your result should not contain any brackets.
#
#
# Example 1:
#
# Input: s = "(abcd)"
# Output: "dcba"
#
# Example 2:
#
# Input: s = "(u(love)i)"
# Output: "iloveu"
# Explanation: The substring "love" is reversed first, then the whole string is reversed.
#
# Example 3:
#
# Input: s = "(ed(et(oc))el)"
# Output: "leetcode"
# Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
#
# Example 4:
#
# Input: s = "a(bcdefghijkl(mno)p)q"
# Output: "apmnolkjihgfedcbq"

# 法一：栈
#  使用栈模拟字符串入栈出栈过程

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ')':
                stack.append(c)
            elif c == ')':
                tmp = []
                # 注意stack不为空才可以读取栈顶
                while stack and stack[-1] != '(':
                    tmp.append(stack.pop())
                if stack:
                    stack.pop() # 将左括号抛出
                stack += tmp
        return "".join(stack)

a = Solution()
s = "(u(love)i)"
s = "(ab(cd(ef)))"

a.reverseParentheses(s)

#   还是存在 逆向输出的 过程 时间复杂度较高

# 法二：括号预处理
# 这种方法的好处是, 预先把括号的对应关系和他们所在的index保存起来, 方便来回跳转到不同层次的括号中去处理字符串.

#  step
# 1.构建数组 pair 将左右括号互相对应的 index 关系保存下来
# 2. step 用来表示向左还是向右走
# 3. 一旦遇到括号就进入括号, step 方向取反
# 4. 处理完一层括号, 进入更深的一层, 处理完深层, 再回到上一层进行遍历, 直至结束


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        n = len(s)
        pair = [0] * n

        # 预先存储左右括号的映射关系
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            if s[i] == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i

        index = 0
        # step = 1 表示向右走, step = -1 表示向左走
        step = 1
        result = []
        while index < n:
            if s[index] == '(' or s[index] == ')':
                index = pair[index]
                # 走的方向反转
                step = -step
            else:
                result.append(s[index])
            index += step
        return "".join(result)

#  只多了 跳转的复杂度   时间复杂度较小
