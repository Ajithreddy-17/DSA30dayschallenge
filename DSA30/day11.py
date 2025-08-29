########set matrix zero###########
a = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9],]
row=len(a)
col=len(a)
rows_zero=[False]*row
cols_zero=[False]*col
for i in range(row):
    for j in range(col):
        if a[i][j]==0:
            rows_zero[i]=True
            cols_zero[j]=True
            print(rows_zero)
            print(cols_zero)
for i in range(row):
    for j in range(col):
        if rows_zero[i] or cols_zero[j]:
            a[i][j]=0
print("new set zero matrix is")
for row in a:
    print(row)
print()

#######rotate array 90 degree #########

a=[
[7, 4, 1],
[8, 5, 2],
[9, 6, 3]
]
row=len(a)
col=len(a)
rotated=[[0]*row for i in range(col)]
for i in range(row):
    for j in range(col):
        rotated[j][row-1-i] = a[i][j]
print("rotated matrix is")
for row in rotated:
    print(row)
 


