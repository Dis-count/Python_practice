# 猜数字不过瘾？不如再来试试迷你老虎机，用随机的unicode字符打样出来，完美模拟了老虎机的效果！

python3 -c "import random;p=lambda:random.choice('7♪♫♣♠♦♥◄☼☽');[print('|'.join([p(),p(),p()]),end='\r') for i in range(8**5)]"
