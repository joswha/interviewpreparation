def binarySearch(nums, low, high, target):
    if high >= low:
        mid = (low + high) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            return binarySearch(nums, low, mid - 1, target)
        else:
            return binarySearch(nums, mid + 1, high, target)
    else:
        return False

def searchMatrix(matrix, target):
        for row in matrix:
            if binarySearch(row, 0, len(row), target):
                return True
        return False
            

