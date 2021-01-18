# Globals for the directions
# Change the values as you see fit
EAST = 1
NORTH = 2
WEST = 3
SOUTH = 4


class Robot:
    def __init__(self, direction = NORTH, x = 0, y = 0):
        self.direction = direction
        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)

    def move(self, way):
        for w in way:
            if w == "R":
                if self.direction == NORTH:
                    self.direction = EAST
                elif self.direction == EAST:
                    self.direction = SOUTH
                elif self.direction == SOUTH:
                    self.direction = WEST
                else:
                    self.direction = NORTH
            if w == "L":
                if self.direction == SOUTH:
                    self.direction = EAST
                elif self.direction == NORTH:
                    self.direction = WEST
                elif self.direction == WEST:
                    self.direction = SOUTH
                else:
                    self.direction = NORTH
            elif w == "A":
                if self.direction == EAST:
                    self.x += 1
                elif self.direction == WEST:
                    self.x -= 1
                elif self.direction == NORTH:
                    self.y +=1
                elif self.direction == SOUTH:
                    self.y -= 1
        self.coordinates = (self.x, self.y)

# robot = Robot(NORTH, 7, 3)
# robot.move("RAALAL")

# print(robot.coordinates)
