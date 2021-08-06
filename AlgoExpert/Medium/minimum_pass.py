class Neighbour():
    def __init__(self, value, left, right, up, down):
        self.value = value
        self.left = left
        self.right = right
        self.up = up
        self.down = down

a = Neighbour(1, None, None, None, None)
b = Neighbour(2, a, None, None, None)
a.value += 1
print(b.left.value)


# def minimumPassesOfMatrix(matrix):
