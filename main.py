from typing import Union

def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y

if __name__ == "__main__":
    print(add(1, 2))
    print(add(1.5, 2.5))
    print(add(1, 2.5))
    print(add(1.5, 7))