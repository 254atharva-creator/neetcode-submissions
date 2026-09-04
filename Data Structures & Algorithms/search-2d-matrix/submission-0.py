class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        L0=0
        R0=m-1
        while L0<=R0:
            X0=L0+(R0-L0)//2
            if matrix[X0][0]<=target<=matrix[X0][n-1]:
                L=0
                R=n-1
                while L<=R:
                    X=L+(R-L)//2
                    if target==matrix[X0][X]:
                        return True
                    elif target>matrix[X0][X]:
                        L=X+1
                    else:
                        R=X-1
                return False
            elif target>matrix[X0][n-1]:
                L0=X0+1
            else:
                R0=X0-1
        return False

            


            
