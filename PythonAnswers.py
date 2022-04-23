import math
import csv

#date 7/12/21
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

def matrixsum(matrix):

    matrix_copy = [x[:] for x in matrix] #so we don't contaminate original matrix.
    rows = len(matrix) # so we only call this once
    total_sums = []
    iteration_sum = 0

    for iteration in range(rows): #must repeat numbe of row times to get all possibilities.
        for row in range(rows): #need to find min for every row
            # print("row "+str(matrix_copy[row]))
            rsp = min(matrix_copy[row])
            # print("min "+str(rsp))
            iteration_sum += rsp
            column = matrix_copy[row].index(rsp) #track which column had min so we dont use that column twice.
            # print("column "+ str(column))
            for i in range(rows): #need to remove column from every row so we dont choose 2 numbers from same column
                matrix_copy[i].pop(column)
                # print(matrix_copy[i])
        # print(iteration_sum)
        # print(matrix)
        matrix.append(matrix.pop(0)) #move first row to end for new iteration
        print(matrix)
        total_sums.append(iteration_sum) # collect every iteration sum.
        iteration_sum = 0
        matrix_copy = [x[:] for x in matrix]

    print("total sums: " + str(total_sums))
    return min(total_sums)

# using Hungarian method
def matrixsum1(matrix):

    mtx_c = [x[:] for x in matrix] #so we don't contaminate original matrix.
    n = len(matrix) # n by n matrix size

    rows_0ed = 0
    columns_0ed = 0

    #find zeroed rows
    for row in mtx_c:
        if min(row) == 0:
            rows_0ed += 1;

    print(rows_0ed)

    for column_n in range(n):
        column = [ mtx_c[x][column_n] for x in range(n)]
        if min(column) == 0:
            columns_0ed += 1

    print(columns_0ed)

    #subtract smalles number of row from row for all rows.
    mtx_c = [[ c-min(row) for c in row] for row in mtx_c]

    for i in mtx_c:
        print(i)

    #subtract smalles number of column from column for all columns.
    for column_n in range(n):
        column = [ mtx_c[x][column_n] for x in range(n)]
        for row_n in range(n):
            mtx_c[row_n][column_n] = mtx_c[row_n][column_n] - min(column)

    for i in mtx_c:
        print(i)

    line_r, line_c = find_min_lines(mtx_c)
    print(line_r, line_c)

    timer = 0
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

    #find original values in coordinates dictated by 0's
    



# date 4/21/22
def lettersum(text):
    return sum(ord(c)-ord('a')+1 for c in text)



if __name__ == "__main__":

    matrix = []

    with open('resources/5x5matrix.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        matrix = [[int(i) for i in row] for row in reader]

    rsp = matrixsum1(matrix)
    print("rsp: "+str(rsp))
