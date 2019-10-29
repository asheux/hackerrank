"""
imports
"""
import math
import random

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

D_COORDS = {
        'n': (0, -1),
        'e': (1, 0),
        'w': (-1, 0),
        'ne': (1, -1),
        'nw': (-1, -1),
        's': (0, 1),
        'se': (1, 1),
        'sw': (-1, 1)
        }

bot_dir = {'n': 'UP', 's': 'DOWN', 'e': 'RIGHT', 'w': 'LEFT'}


def e_f_c(legend, ch):
    if ch == '-':
        return None
    element = legend[ch]()
    element.origin_char = ch
    return element


def get_char(element):
    if not element:
        return '-'
    return element.origin_char


class Bot:
    """
    the bot to play the game
    """
    def __init__(self):
        self.d = 'e'

    def get_dir(self, r, v):
        space = self.find('-', r, v)
        ch = self.look(self.d, r, v)
        door = self.find_all('e', r, v)
        if ch != '-' and space:
            self.d = space
        return self.d

    def move(self, r, v):
        d = self.get_dir(r, v)
        dest = r.get_destination(d, v)
        bot_pos = r.bots_pos()
        d_x, d_y = dest
        b_x, b_y = bot_pos
        bot = r.g.get_pos_holder(v(b_x, b_y))
        r.g.set_pos_holder(None, v(b_x, b_y))
        r.g.set_pos_holder(bot, v(d_x, d_y))

    def look(self, d, r, v):
        x, y = r.bots_pos()
        x1, y1 = D_COORDS[d]
        n_v = v.plus(v(x1, y1), x, y)
        if r.g.is_inside(n_v):
            el = r.g.get_pos_holder(n_v)
            return get_char(el)
        return '#'

    def find_all(self, char, r, v):
        """find bots 8 adjacent cells"""
        found = []
        for d in DIRECTIONS:
            if d in bot_dir:
                ch = self.look(d, r, v)
                if ch == char:
                    found.append(d)
        return found

    def find(self, ch, r, v):
        found = self.find_all(ch, r, v)
        if len(found) == 0:
            return None
        return found[math.floor(random.random() * len(found))]


class Wall:
    pass


class Door:
    pass


class Vector:
    """
    a vector to determine bots coordinates
    """
    def __init__(self, x, y):
        self.x, self.y = x, y

    @classmethod
    def plus(cls, other_v, x, y):
        """
        other_v represents the other vector we want to
        add and get the coordinates
        """
        return cls(other_v.x + x, other_v.y + y)


class Grid:
    """
    this is the surround of the bot
    """
    def __init__(self, height, width):
        self.h = height
        self.w = width
        self.space = [' '] * (self.w * self.h)

    def is_inside(self, v):
        """
        checks to see if the bot is inside the grid on not
        v: represents the vector instance
        """
        return (0 <= v.x < self.w) and (0 <= v.y < self.h)

    def get_pos_holder(self, v):
        """
        gets the position of the bot in the grid
        """
        return self.space[v.x + self.h * v.y]

    def set_pos_holder(self, value, v):
        """
        set the bot to a new position
        """
        self.space[v.x + self.h * v.y] = value


class Room:
    """
    this class handles all the activities in the room
    """
    def __init__(self, surf, legend):
        self.s = surf
        self.l = legend
        self.g = Grid(len(surf), len(surf[0]))
        self.create_room()

    def create_room(self):
        """this creates the room the bots are in"""
        for x, line in enumerate(reversed(self.s)):
            for y in range(len(line)):
                self.g.set_pos_holder(e_f_c(self.l, line[y]), Vector(x, y))

    def bots_pos(self):
        """find bots position in the room(grid)"""
        coords = None
        for i, el in enumerate(self.g.space):
            if get_char(el) == 'b':
                c = i // self.g.w, i % self.g.w
                coords = c
        return coords

    def get_destination(self, d, vector):
        x1, y1 = D_COORDS[d]
        x, y = self.bots_pos()
        v = vector.plus(vector(x1, y1), x, y)
        return v.x, v.y


if __name__ == '__main__':
    legend = {
            '#': Wall,
            'b': Bot,
            'e': Door
            }
    room = Room(SURFACE, legend)
    bot = Bot()
    bot.move(room, Vector)
