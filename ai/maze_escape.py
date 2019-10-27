DIRECTIONS = ['n', 'e', 'w', 'ne', 'nw', 's', 'se', 'sw']

SURFACE = [
        '#######',
        '#--#-b#',
        '#--#--#',
        '#--#--#',
        'e-----#',
        '#-----#',
        '#######',
        ]

class Vector(object):
    """
    a vector to determine bots coordinates
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def plus(cls, other_v):
        """
        other_v represents the other vector we want to
        add and get the coordinates
        """
        return cls(other_v.x + self.x, other_v.y + self.y)


class Grid(object):
    """
    this is the surround of the bot
    """
    def __init__(self, height, width):
        self.h = height
        self.w = width
        self.space = [' '] * (self.w * self.h)

    def in_side(self, v):
        """
        checks to see if the bot is inside the grid on not
        v: represents the vector instance
        """
        return (0 <= v.x < self.w) and (0 <= v.y < self.h)

    def get_postion(self, v):
        """
        gets the position of the bot in the grid
        """
        return self.space[v.x + self.w * v.y]

    def set_position(self, value, v):
        """
        set the bot to a new position
        """
        self.space[v.x + self.w * v.y] = value


class Room(object):
    """
    this class handles all the activities in the room
    """
    def __init__(self):
        self.grid = Grid(len(SURFACE), len(SURFACE[0]))
        self.create_room()

    def create_room(self):
        """this creates the room the bots are in"""
        for y, line in enumerate(SURFACE):
            for x in range(len(line)):
                self.grid.set_position(line[x], Vector(x, y))


