# 请你给一个停车场设计一个停车系统。停车场总共有三种不同大小的车位：大，中和小，每种尺寸分别有固定数目的车位。
#
# 请你实现 ParkingSystem 类：
#
# ParkingSystem(int big, int medium, int small) 初始化 ParkingSystem 类，三个参数分别对应每种停车位的数目。
# bool addCar(int carType) 检查是否有 carType 对应的停车位。 carType 有三种类型：大，中，小，分别用数字 1， 2 和 3 表示。一辆车只能停在 carType 对应尺寸的停车位中。如果没有空车位，请返回 false，否则将该车停入车位并返回 true 。
#
# 示例 1：
#
# 输入：
# ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
# [[1, 1, 0], [1], [2], [3], [1]]
# 输出：
# [null, true, true, false, false]
#
# 解释：
# ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
# parkingSystem.addCar(1); // 返回 true ，因为有 1 个空的大车位
# parkingSystem.addCar(2); // 返回 true ，因为有 1 个空的中车位
# parkingSystem.addCar(3); // 返回 false ，因为没有空的小车位
# parkingSystem.addCar(1); // 返回 false ，因为没有空的大车位，唯一一个大车位已经被占据了

# class ParkingSystem(object):
#
#     def __init__(self, big, medium, small):
#         self.park = [0, big, medium, small]
#
#     def addCar(self, carType):
#         if self.park[carType] == 0:
#             return False
#         self.park[carType] -= 1
#         return True

# 时间复杂度： O(1)，每次 addCar 操作是 O(1)的是时间复杂度。
# 空间复杂度： O(1)，只用了常量个空间。

# 今天的题目其实可以拓展：
#
# 如果允许车离开停车位，该怎么做？
# 如果允许小车停放在比它更大的停车位上，该怎么做？
# 如果车离开车位的时候必须按照指定的顺序，比如先进先出，该怎么做？
# 如果在并发场景的停入和离开车，如何保证结果正确？

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.size = [0, big, medium, small]
        self.car = [0, big, medium, small]
        self.dic = []

    def addCar(self, carType: int) -> bool:
        if self.car[carType] <= 0:
            return False
        self.car[carType] -= 1
        return True

    # 如果允许车离开停车位，该怎么做？
    def removeCar(self, carType: int) -> bool:
        if self.car[carType] >= self.size[carType]:
            return False
        self.car[carType] += 1
        return True

    # 如果允许小车停放在比它更大的停车位上，该怎么做？
    def addSmallCar(self, carType: int) -> bool:
        if sum(self.car[1:carType + 1]) <= 0:
            return False
        for i in range(carType ,0 ,-1):
            if self.car[i] : # 小车优先小车位
                self.car[i] -= 1
                return True
    # 如果给每个车增加 id，车离开车位的时候必须按照指定的顺序，比如先进先出，该怎么做？
    # 我理解是要存一个，hashmap然后，弹出指定的车辆
    def addCarList(self, carType: int) -> bool:
        dic.append(carType)
        return self.addCar(carType)
    def removeCarList(self) -> bool:
        if not dic : return False
        return self.removeCar(dic.pop(0))

    # 如果在并发场景的停入和离开车，如何保证结果正确？
    # 是否可以参考concurrenthashmap分段锁来设计，蹲一个大佬
