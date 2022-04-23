
def find_min_lines(mtx):
    line_r = []
    line_c = []
    for i in range(len(mtx[0])):
        line_r.append(1)
        line_c.append(1)

    rows_0ed = []
    for row in range(len(mtx)):
        if min(mtx[row]) == 0:
            rows_0ed.append(row)
    # print(rows_0ed)

    mask = 0
    for i in rows_0ed:
        mask = mask | i
    mask = ~(mask)&0b1111111111111111
    # print(bin(mask))

    n = len(mtx)
    range__ = (1 << n) -1
    for i in range(range__+1):
        x=0
        y=i
        # print(str(y))
        if y&mask:
            # print("skipping: "+bin(y)+ " "+str(y))
            continue
        else:
            # print("checking: "+bin(y)+ " "+str(y))
            rows_to_count = []
            columns_to_count = []
            while y>0:
                if(y&1==1):
                    rows_to_count.append(n-1-x)
                x+=1
                y = y >> 1

            #sum all lines
            # find any column with zero not accounted by row.
            for row in range(n):
                if row not in rows_to_count and min(mtx[row]) == 0:
                    for j in range(n):
                        if mtx[row][j] == 0 and j not in columns_to_count:
                            columns_to_count.append(j)

            if (len(rows_to_count) + len(columns_to_count)) < (len(line_r) + len(line_c)):
                line_r, line_c = rows_to_count[:], columns_to_count[:]

    print("row: " + str(line_r) + " column: " + str(line_c))
    return line_r, line_c



mtx = [[108, 125, 150],[150, 135, 175],[122,148, 250]]
line_r, line_c = find_min_lines(mtx)
timer = 0

while ((len(line_r) + len(line_c)) < len(mtx)) and timer < 20: #not optimal number of zeroes yet
    print(str(len(line_r) + len(line_c)) + " " + str(len(mtx)))
    min_value = max(max(mtx));
    for i in range(len(mtx)):
        for j in range(len(mtx[i])):
            if mtx[i][j] < min_value and (i not in line_r) and (j not in line_c):
                min_value = mtx[i][j]

    print(min_value)

    # subtract from uncovered lines
    for row in range(len(mtx)):
        if row not in line_r:
            mtx[row] = [x-min_value for x in mtx[row]]
    # add to covered columns
    for column in range(len(mtx)):
        if column in line_c:
            for row in range(len(mtx)):
                mtx[row][column] = mtx[row][column] + min_value


    line_r, line_c = find_min_lines(mtx)
    print(str(len(line_r) + len(line_c)) + " " + str(len(mtx)))
    timer += 1

    print(mtx)
    print(str(123456789 + 663035648 + 163882767 + 52838563 + 96549194))
