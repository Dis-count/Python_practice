#coding:gbk
import random

joker = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
JOKER = joker + joker + joker + joker
# ����δ�㻨ɫ������ȼ����Ϊ�ĸ�A~K���ƣ���52��
cards = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}
#���ֵ����ڶԱȴ�С
nums = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}
#���ֵ����ڼ������
gongpai = ["J","Q","K"]
n_num = 0
n_dian = 0
player="player"

def create_cards():                       #����
    cards=[]
    a = random.choice(JOKER)
    JOKER.remove(a)
    cards.append(a)
    b = random.choice(JOKER)
    JOKER.remove(b)
    cards.append(b)
    c = random.choice(JOKER)
    JOKER.remove(c)
    cards.append(c)
    return cards

def player_cards_n(n):                    #����n�������
    global dict
    dict={}
    for i in range(n):
        dict[player+str(i)] = create_cards()
    return dict

def dianshu(n=["A","2","3"]):                 #�жϵ���
    n_num = nums[n[0]] + nums[n[1]] + nums[n[2]]
    n_dian = n_num % 10
    return n_dian

def judge(n=["A","2","3"]):                 #2�����С������1�����������0������
    if n[0]==n[1]==n[2]:
        return [2,cards[n[0]]]
    elif n[0] in gongpai and n[1] in gongpai and n[2] in gongpai:
        return [1,0]
    else:
        m = dianshu(n)
        return [0,m]

def compare(player0=[0,2],player1=[0,0]):
    if player0[0]>player1[0]:
        return "ׯ��Ӯ"
    elif player0[0]<player1[0]:
        return "�м�Ӯ"
    else:
        if player0[0]==1:
            return "ƽ��"
        else:
            if player0[1]==player1[1]:
                return "ƽ��"
            elif player0[1]>player1[1]:
                return "ׯ��Ӯ"
            elif player0[1]<player1[1]:
                return "�м�Ӯ"

game = "��Ϸ˵��"
Introduction = "������Ϸ��������Ϸ����һ���˿����е�52���ƣ���С�����⣩����������A��9֮�����Щ��Ϊ�����ƶ�Ӧ\n����1-9��" \
               "����10Ϊ0���ƣ�����J��Q��K��Ϊ���ơ�ϵͳ��ÿλ��ҷ��������ƺ�ׯ�����мһ���Ƚ��Ƶ�\n��С��" \
               "�����������ж�ׯ�е���Ӯ������player0��ׯ�ң������Ϊ�мҡ�"
print game.center(100)
print Introduction
while True:
    ipt = raw_input("��ʼ&�˳�Y/N\n")
    if ipt == 'Y' or ipt == 'y':
        n = input("���������������1~6����")
        players_dict=player_cards_n(n)
        if n==1:
            com = create_cards()
            print "player0�����ǣ�",players_dict["player0"]
            print "���Ե����ǣ�",com
            print "ׯ��player0���мҵ��Ե���Ӯ�ǣ�",compare(judge(players_dict["player0"]),judge(com))
        else:
            for i in range(n):
                any = raw_input("�����"+player+str(i)+"�����Y")              #�ɹ������ѡ�����˳��
                print player+str(i)+"�����ǣ�",players_dict[player+str(i)]
            for i in range(1,n):
                print "������ׯ�Һ��мҵ���Ӯ�����"
                print "ׯ��player0���м�"+player+str(i)+"����Ӯ�ǣ�",compare(judge(players_dict["player0"]),judge(players_dict[player+str(i)]))
    elif ipt == 'N' or ipt == 'n':
        print "��Ϸ������лл���룡"
        break
