#54. Spiral Matrix
#Given an m x n matrix, return all elements of the matrix in spiral order.

class Matrix():
    def spiralorder(self,matrix):
        left = 0
        right = len(matrix[0])
        top =0
        bottom = len(matrix)
        res=[]

        while(left<right and top<bottom):

            for i in range(left,right):
                res.append(matrix[top][i])
            top=top+1
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right=right-1
            if not(left<right and top<bottom):
                break
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            bottom=bottom-1
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
            left=left+1

        return(res)

m = Matrix()
print(m.spiralorder([[1,2,3],[4,5,6],[7,8,9]]))
print(m.spiralorder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))