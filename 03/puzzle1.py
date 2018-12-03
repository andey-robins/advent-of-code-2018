def main():

    matrix = [['-' for x in range(1001)] for y in range(1001)]

    idCheck = {}

    with open("input.txt") as f:
        for line in f:
            id, at, coor, size = line.split()

            coor = coor[:-1]
            x, y = coor.split(',')

            width, height = size.split('x')

            idCheck[id] = int(width) * int(height)


            for xcoord in range(int(x), int(width) + int(x)):
                for ycoord in range(int(y), int(height) + int(y)):

                    if matrix[xcoord][ycoord] == '-':
                        matrix[xcoord][ycoord] = id
                    else:
                        matrix[xcoord][ycoord] = 'X'

    count = 0

    for eachx in matrix:
        for eachy in eachx:
            if eachy == 'X':
                count += 1

    for id in idCheck.keys():
        custCount = 0

        for eachx in matrix:
            for eachy in eachx:
                if eachy == id:
                    custCount += 1

        if custCount == idCheck[id]:
            print(id)

    print(count)


    return

if __name__ == '__main__':
    main()
