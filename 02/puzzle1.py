def main():

    twos = 0
    threes = 0

    with open("input.txt") as f:

        for line in f:

            letters = {}

            for char in line:
                if not char in list(letters.keys()):
                    letters[char] = 0

                letters[char] += 1

            if 2 in list(letters.values()):
                twos += 1

            if 3 in list(letters.values()):
                threes += 1

    print("twos = " + str(twos))
    print("threes = " + str(threes))
    print("checksum = " + str(twos * threes))


    return

if __name__ == '__main__':
    main()
