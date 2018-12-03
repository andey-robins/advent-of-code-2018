def main():

    frequency = 0

    with open("input.txt") as f:
        for line in f:
            if line[0] is '-':
                frequency = frequency - int(line[1:])
            else:
                frequency = frequency + int(line[1:])

    print(frequency)

    return

if __name__ == '__main__':
    main()
