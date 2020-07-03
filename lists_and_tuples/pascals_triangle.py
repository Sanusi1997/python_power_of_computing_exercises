pascal_triangle = [[1],[1,1],[1,2,1],[1,3,3,1]]
space = " "
number_space=" "
counter = 10
n= 0
for rows in pascal_triangle:
    print("\n", end='')
    for number in rows:
        while n < counter:
            print(f"{space}",end='')
            n += 1
        print(f"{number_space}{number}", end='')



