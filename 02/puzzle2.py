def main():

    ids = []

    with open("input.txt") as f:
        for line in f:
            ids.append(line)

    for top in ids:
        for each in ids:
            if not each == top:
                if diff(each, top) == 1:
                    print(each + " " + top)
                    break


    return

def diff(one, two):

    difference = 0

    for i in range(0, len(one)):
        if not one[i] == two[i]:
            difference += 1

    return difference

if __name__ == '__main__':
    main()
