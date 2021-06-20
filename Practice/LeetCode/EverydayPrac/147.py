# 483. Smallest Good Base
# Given an integer n represented as a string, return the smallest good base of n.
#
# We call k >= 2 a good base of n, if all digits of n base k are 1's.

# Example 1:
#
# Input: n = "13"
# Output: "3"
# Explanation: 13 base 3 is 111.

# Example 2:
#
# Input: n = "4681"
# Output: "8"
# Explanation: 4681 base 8 is 11111.

# Example 3:
#
# Input: n = "1000000000000000000"
# Output: "999999999999999999"
# Explanation: 1000000000000000000 base 999999999999999999 is 11.

#  思路： 1. 根据 k^m 等比数列求和公式 首先确定 ‘位数 m’ 的取值范围--上界  从上界向下枚举或者二分  之后检验对应的 k 值是否合法。
#  2. 确定 k 的取值范围 k=⌊m\sqrt(n)​⌋
import time
class Solution:
    def smallestGoodBase(self, n: str) -> str:

        num = int(n)
        def check(x, m):
            ans = 0
            for _ in range(m+1):
                ans = ans*x + 1
            return ans   # This function is used to calculate the geometric series.
        ans = float("inf")
        for i in range(64,0,-1):
        # for i in range(1,64):
            l = 2
            r = num
            while l < r:
                mid = l + (r - l)//2
                tmp = check(mid, i)
                if tmp == num:
                    ans = min(ans, mid)
                    break
                elif tmp < num:
                    l = mid + 1
                else:
                    r = mid

        return str(ans)

a = Solution()

start = time.time()
a.smallestGoodBase(1000000000000000000)
end = time.time()
print(end-start)

check(5,3)
