import math


def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if num1 >= num2:
        num3 = gcd(num1, num2)
    else:
        num3 = gcd(num2, num1)
    print("GCD({}, {}) = {}".format(num1, num2, num3))


def gcd(a: int, b: int) -> int:
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def divRemainder(a: int, b: int) -> int:
    return math.floor(a/b)


def euclidean(nums: list[int]) -> list[int]:
    if a % b == 0:
        return [a, b, math.floor(a/b), 1]
    return [a, b]


if __name__ == "__main__":
    main()
