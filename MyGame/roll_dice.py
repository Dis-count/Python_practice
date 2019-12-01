import random

def roll_dice(numbers = 3,points = None):
    print('----- 摇骰子 -----')
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1,7)
        points.append(point)
        numbers = numbers - 1
    return points


def roll_result(total):
    isBig = 11 <= total <=18
    isSmall = 3 <= total <= 10
    if isBig:
        return '大'
    elif isSmall:
        return '小'


def start_game():
    your_money = 1000
    while your_money > 0:
        print('----- 游戏开始 -----')
        choices = ['大','小']
        your_choice = input('请下注，大 or 小：')
        your_bet = input('下注金额：')
        if your_choice in choices:
            points = roll_dice()
            total = sum(points)
            youWin = your_choice == roll_result(total)
            if youWin:
                print('骰子点数：',points)
                print('恭喜，你赢了 {} 元，你现在有 {} 元本金'.format(your_bet,your_money + int(your_bet)))
                your_money = your_money + int(your_bet)
            else:
                print('骰子点数：',points)
                print('很遗憾，你输了 {} 元，你现在有 {} 元本金'.format(your_bet, your_money - int(your_bet)))
                your_money = your_money - int(your_bet)
        else:
            print('格式有误，请重新输入')
    else:
        print('游戏结束')

start_game()
