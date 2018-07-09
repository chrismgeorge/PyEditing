import cv2

pic = cv2.imread('chap.jpg', cv2.IMREAD_COLOR)
cv2.imwrite('iconCopy.jpg', pic)
picCopy = cv2.imread('iconCopy.jpg', cv2.IMREAD_COLOR)
k = 32
colorPallete = []

for row in range(0, len(picCopy), k):
    curRow = []
    for col in range(0, len(picCopy[0]), k):
        for xcol in range(k):
            for jrow in range(k):
                if (row + jrow < 3488 and col+xcol < 2581):
                    picCopy[row+jrow, col+xcol] = picCopy[row,col]
        curRow.append([picCopy[row][col][2]//1, picCopy[row][col][1]//1, picCopy[row][col][0]//1])

    colorPallete.append(curRow)

print(colorPallete)
#print(len(colorPallete) * len(colorPallete[0]))

cv2.imwrite('iconCopy2.jpg', picCopy)

# image 2272x1704
# depth maps 55x305

# b = 2272 rows
# a = 1704 columns
# c = 55 rows
# d = 
# print(b/c)
