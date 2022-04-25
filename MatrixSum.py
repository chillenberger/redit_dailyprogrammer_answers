
#date 7/12/21
# https://www.reddit.com/r/dailyprogrammer/comments/oirb5v/20210712_cha#llenge_398_difficult_matrix_sum/
# this program uses hungarian method to find optimal sum or matrix such
# that every number summed belongs to a unique row and column.
# This program works for 5x5 and 20x20 but no 97x97 due to numbe of iteration
# checked in find_min_lines exceeding capabilities of range(). This can be
# fixed by intelligently choosing rows combinations to check.


import math
import csv
import itertools

# finds how to draw fewest number of lines through all 0's in the
# represetitive matrix, all lines follow row or column
def find_min_lines(mtx):
    # mtx size
    n = len(mtx)
    # permutation of rows to check
    range__ = (1 << n)

    # containers to save lines for rows and columns
    line_r = [1]*n
    line_c = [1]*n

    # find all rows with zeroes
    zeroed_rows = [x for x in range(len(mtx)) if min(mtx[x]) == 0]

    # make a mask so we dont have to check all row combinations
    mask = 0
    for i in zeroed_rows:
        mask = mask | 1<<i
    print(bin(mask))
    mask = ~mask
    # iterate all combinations of
    for i in range(range__):
        x=0
        y=i
        if y&mask:
            continue
        else:
            rows_to_count = []
            columns_to_count = []
            while y>0:
                if(y&1==1):
                    rows_to_count.append(x)
                x+=1
                y = y >> 1

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


# using Hungarian method https://brilliant.org/wiki/hungarian-matching/
def matrixsum1(matrix):

    mtx_c = [x[:] for x in matrix] #so we don't contaminate original matrix.
    n = len(matrix) # n by n matrix size

    #subtract smalles number of row from row for all rows.
    mtx_c = [[ c-min(row) for c in row] for row in mtx_c]

    #subtract smallest number of column from column for all columns.
    for column_n in range(n):
        column = [ mtx_c[x][column_n] for x in range(n)]
        for row_n in range(n):
            mtx_c[row_n][column_n] = mtx_c[row_n][column_n] - min(column)

    # find the minimum number of lines we can draw through all cols and rows
    # according to hungarian method.
    line_r, line_c = find_min_lines(mtx_c)
    print(line_r, line_c)

    timer = 0 # timer to prevent infinite loops.
    # Continue zeroing until lines drawn equals matrix columns size at least
    # or timer expires.
    while ((len(line_r) + len(line_c)) < len(mtx_c)) and timer < 20: #not optimal number of zeroes yet
        # find min value in matrix
        min_value = max(max(mtx_c));
        for i in range(len(mtx_c)):
            for j in range(len(mtx_c[i])):
                if mtx_c[i][j] < min_value and (i not in line_r) and (j not in line_c):
                    min_value = mtx_c[i][j]

        # subtract from uncovered lines
        for row in range(len(mtx_c)):
            if row not in line_r:
                mtx_c[row] = [x-min_value for x in mtx_c[row]]

        # add to covered columns
        for column in range(len(mtx_c)):
            if column in line_c:
                for row in range(len(mtx_c)):
                    mtx_c[row][column] = mtx_c[row][column] + min_value

        # find new min number of lines
        line_r, line_c = find_min_lines(mtx_c)
        # incriment timer to avoid infinite loop if error
        timer += 1

        print(mtx_c)

    # find original values at coordinates dictated by 0's
    # find which columns have zeroes arranged by row
    zeroed_cols = [[ x for x in range(len(row)) if row[x] == 0] for row in mtx_c]
    # find all combinations of 0's columns
    zeroed_map = [ x for x in itertools.product(*zeroed_cols)]
    # if repteat columns, delete
    zeroed_map = [[ c for c in row if row.count(c) == 1] for row in zeroed_map]
    # delete any iteration that is not correct length
    zeroed_map = [ row for row in zeroed_map if len(row) == n]
    # sum numbers in original matrix specivied by
    rsp = sum([matrix[row][zeroed_map[0][row]] for row in range(n)])

    return(rsp)


if __name__ == "__main__":
    with open('resources/20x20matrix.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        matrix = [[int(i) for i in row] for row in reader]

    rsp = matrixsum1(matrix)
    print("rsp: "+str(rsp))
