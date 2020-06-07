#  给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为k[0],k[1],...,k[m]。请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

# DP
class Solution:
    def cutRope(self, number):
        # write code here
        res=1
        if number<=1:
            return 0
        elif number<=2:
            return 1
        elif number<=3:
            return 2
        prod=[0,1,2,3]
        for i in range(4,number+1):
            max=0
            for j in range(1,i//2+1):
                pro=prod[j]*prod[i-j]
                if pro>max:
                    max=pro
            prod.append(max)
        return prod[number]
T = Solution()
T.cutRope(4)

# Greedy
class Solution:
    def __init__(self):
        print('Please input integer number.')

    def cutRope(self, number):
        # write code here
        res=1
        if number<=1:
            return 0
        elif number<=2:
            return 1
        elif number<=3:
            return 2
        elif number>3:
            if number%3==0:
                res=3**(number//3)
            elif number%3==1:
                res=3**(number//3-1)*4
            else:
                res=3**(number//3)*(number%3)
        return res
T = Solution()
T.cutRope(8)
