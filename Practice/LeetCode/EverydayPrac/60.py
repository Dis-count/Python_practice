# 1006. Clumsy Factorial
# Normally, the factorial of a positive integer n is the product of all positive integers less than or equal to n.  For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.
#
# We instead make a clumsy factorial: using the integers in decreasing order, we swap out the multiply operations for a fixed rotation of operations: multiply (*), divide (/), add (+) and subtract (-) in this order.
#
# For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.  However, these operations are still applied using the usual order of operations of arithmetic: we do all multiplication and division steps before any addition or subtraction steps, and multiplication and division steps are processed left to right.
#
# Additionally, the division that we use is floor division such that 10 * 9 / 8 equals 11.  This guarantees the result is an integer.
#
# Implement the clumsy function as defined above: given an integer N, it returns the clumsy factorial of N.
#
# Example 1:
#
# Input: 4
# Output: 7
# Explanation: 7 = 4 * 3 / 2 + 1
# Example 2:
#
# Input: 10
# Output: 12
# Explanation: 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1


class Solution(object):
    def clumsy(self, N):
        op = 0
        stack = [N]
        for i in range(N - 1, 0, -1):
            if op == 0:
                stack.append(stack.pop() * i)
            elif op == 1:
                stack.append(int(stack.pop() / float(i)))
            elif op == 2:
                stack.append(i)
            elif op == 3:
                stack.append(-i)
            op = (op + 1) % 4
        return sum(stack)

# 时间复杂度：O(N)
# 空间复杂度：O(N)
