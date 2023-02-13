def main(): 
    base = int(input("Enter the base number to find the ord of: "))

    while True:
        num = int(input("Enter a number to find the ord of: "))
        scale = num
        count = 1

        while True:
            if num % base == 1:
                break
            num = num * scale
            count += 1

        print(count, num)

if __name__ == "__main__":
    main()
    