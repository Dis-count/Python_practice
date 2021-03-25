# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
#
# 整数除法仅保留整数部分。
#
# 示例 1：
#
# 输入：s = "3+2*2"
# 输出：7

# 注意利用栈的时候， 一定要记住  加减对应的操作一定是压入栈的 因为操作在  乘除之后，  当遇到乘除时，就可以 出栈数字 然后计算出来 入栈。  一定要分清这样的逻辑关系。


class Solution:
    def calculate(self, s):
        stack = []
        pre_op = '+'
        num = 0
        for i, each in enumerate(s):
            if each.isdigit():
                num = 10 * num + int(each)
            if i == len(s) - 1 or each in '+-*/':
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    stack.append(stack.pop() * num)
                elif pre_op == '/':
                    top = stack.pop()
                    if top < 0:
                        stack.append(int(top / num))
                    else:
                        stack.append(top // num)
                pre_op = each
                num = 0
        return sum(stack)

a = Solution()
a.calculate('3+2*2') 
# 时间复杂度：O(N)
# 空间复杂度：O(N)
