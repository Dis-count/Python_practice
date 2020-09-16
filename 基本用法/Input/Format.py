from typing import List

def test(b: List[int]) -> str:
    print(b)
    return test


if __name__ == '__main__':
    test(['n', 'a'])
