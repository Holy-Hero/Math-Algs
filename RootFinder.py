import numpy


def main():
    print("Enter in the coefficient as well as the powers one at a time, Ex: 5x^2 ->5,2\n"
          "Enter 'stop' to stop\n"
          "Re-enter the same power to change")

    nums = {}
    powers = []

    while True:
        n = input("->")
        if n == "stop":
            break
        try:
            n = n.split(",")
            n = list(map(float, n))
        except:
            print("Please enter numbers, Ex: 5x^2 ->5,2")
        else:
            nums[n[1]] = n[0]
            powers.append(n[1])
        print("The inputs so far")
        for key in nums.keys():
            print(f"coefficient: {nums[key]}, power: {key}")

    coefficients = []
    counter = max(powers)
    while len(powers) > 0:
        if counter in powers:
            coefficients.append(nums[counter])
            powers.remove(counter)
        else:
            coefficients.append(0)

        counter -= 1
    print(numpy.roots(numpy.poly1d(coefficients)))


if __name__ == "__main__":
    main()