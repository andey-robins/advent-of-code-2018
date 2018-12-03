def main():

    frequency = 0
    hits = {0: 1}
    inputs = []

    with open("input.txt") as f:
        for line in f:
            inputs.append(line)

    i = 0

    while not 2 in list(hits.values()):

        if inputs[i][0] is '-':
            frequency -= int(inputs[i][1:])
        else:
            frequency += int(inputs[i][1:])

        if i >= len(inputs) - 1:
            i = 0
        else:
            i += 1

        if not frequency in hits.keys():
            hits[frequency] = 0

        hits[frequency] += 1

    for key in hits.keys():
        if hits[key] == 2:
            print(key)

    return

if __name__ == '__main__':
    main()
