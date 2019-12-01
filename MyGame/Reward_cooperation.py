import random
import numpy as np

def reward_coop(numbers = 3,points = None):
    print('----- Investment Bonus -----')
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1,11)
        points.append(point)
        numbers = numbers - 1
    return points

reward = reward_coop()
ave = np.mean(reward)
if reward[0] > ave:
    
