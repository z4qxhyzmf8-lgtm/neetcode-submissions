class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #
        #binary search rows and then columns
        #
        #n = len(matrix) #nr of rows
        #m = len(matrix[0]) #nr of columns
        #l = 0 
        #r = n - 1
        #row = -1
        #while l <= r:
        #    mid = (l + r) // 2
        #    if matrix[mid][0] <= target and target <= matrix[mid][m - 1]:
        #        row = mid
        #        break
        #    elif target > matrix[mid][m - 1]:
        #        l = mid + 1
        #    else:
        #        r = mid - 1
        #if row == -1:
        #    return False
        # 
        #l = 0 
        #r = m - 1
        #while l <= r:
        #    mid = (l + r) // 2
        #    if matrix[row][mid] == target:
        #        return True
        #    elif matrix[row][mid] > target:
        #        r = mid - 1
        #    else:
        #        l = mid + 1
        #return False
        #
        #single pass binary search
        n = len(matrix)
        m = len(matrix[0])
        l = 0
        r = n * m - 1
        while l <= r:
            mid = (l + r) // 2
            row = mid // m
            col = mid % m
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                l = mid + 1
            else:
                r = mid - 1
        return False

                
        