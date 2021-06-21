# 401. Binary Watch
# A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.
#
# For example, the below binary watch reads "4:51".
#
#
# Given an integer turnedOn which represents the number of LEDs that are currently on, return all possible times the watch could represent. You may return the answer in any order.
#
# The hour must not contain a leading zero.
#
# For example, "01:00" is not valid. It should be "1:00".
# The minute must be consist of two digits and may contain a leading zero.
#
# For example, "10:2" is not valid. It should be "10:02".
#
# Example 1:
#
# Input: turnedOn = 1
# Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
#
# Example 2:
#
# Input: turnedOn = 9
# Output: []

#  枚举时分  由于 4个时bit 可组成16以内数 8个分bit 可组成64以内数  因此不用进行校验
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = list()
        for h in range(12):
            for m in range(60):
                if bin(h).count("1") + bin(m).count("1") == turnedOn:
                    ans.append(f"{h}:{m:02d}")
        return ans

# 复杂度分析
# 时间复杂度：O(1)。枚举的次数是一个与输入无关的定值。
# 空间复杂度：O(1)。仅使用了常数大小的空间。注意返回值不计入空间复杂度。
h = 10
m = 4
print(f"{h}:{m:02d}")


#  二进制枚举
#  枚举所有可能情况并且满足时分要求（需要验证）
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = list()
        for i in range(1024):
            h, m = i >> 6, i & 0x3f   # 用位运算取出高 4 位和低 6 位
            if h < 12 and m < 60 and bin(i).count("1") == turnedOn:
                ans.append(f"{h}:{m:02d}")
        return ans

# 0x3f = bin(63)
