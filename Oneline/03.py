# 无聊的时候，猜猜数字也是很有乐趣的嘛。1~99范围内的整数，如果猜对了会给你一个“Y”，如果猜高了会给出一个“H”；猜低了，你会得到一个“L”（Y、H、L可以根据你希望它给出的提示进行更换），你有六次机会猜出正确的结果哦！

python3 -c "import random;n=random.randint(1,99);[(lambda a:print('Y' if a==n else 'H' if a>n else 'L'))(int(input())) for i in range(6)]"
