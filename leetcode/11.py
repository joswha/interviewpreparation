def maxArea(height):
    l, r = 0, len(height) - 1
    area = 0
    for width in range(len(height) - 1, 0, -1):
        if height[l] < height[r]:
            area = max(area, width * height[l])
            l += 1
        else:
            area = max(area, width * height[r])
            r -= 1
    return area

height = [2,3,4,5,18,17,6]
maxArea(height)
