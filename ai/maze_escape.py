"""
imports
"""
import math
import random


class Wall:
    """
    Room wall object
    """
    pass


class Door:
    """
    room door object
    """
    pass


DIRECTIONS = ['n', 'e', 'w', 's']

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
        self.d_f = False

    def get_dir(self, r, v):
        found = self.find_all(r, v)
        if isinstance(found, list):
            self.d = self.find(found, r, v)
        else:
            self.d, self.d_f = found, True
        return self.d, self.d_f

    def move(self, d, r, v):
        dest = r.get_destination(d, v)
        bot = r.g.get_pos_holder(v)
        r.g.set_pos_holder(None, v)
        r.g.set_pos_holder(bot, dest)

    def look(self, d, r, v):
        x, y = D_COORDS[d]
        n_v = v.plus(Vector(x, y))
        if r.g.is_inside(n_v):
            el = r.g.get_pos_holder(n_v)
            return get_char(el)
        return '#'

    def find_all(self, r, v):
        """find bots 8 adjacent cells"""
        found = []
        for d in DIRECTIONS:
            ch = self.look(d, r, v)
            if ch != '#':
                if ch == 'e':
                    return d
                else:
                    found.append(d)
        return found

    def find(self, found, r, v):
        if len(found) == 0:
            return None
        return found[math.floor(random.random() * len(found))]


class Vector:
    """
    a vector to determine bots coordinates
    """
    x, y = None, None
    def __init__(self, vx, vy):
        self.x, self.y = vx, vy
        type(self).x, type(self).y = self.x, self.y

    @classmethod
    def plus(cls, other_v):
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

    def to_string(self):
        l = []
        for x in range(self.g.w):
            output = ''
            for y in range(self.g.h):
                output += get_char(self.g.space[x + y * self.g.w])
            l.append(output)
        return l

    @classmethod
    def act(cls, surf, legend):
        return cls(surf, legend)

    def get_destination(self, d, vector):
        x, y = D_COORDS[d]
        v = vector.plus(Vector(x, y))
        return v


if __name__ == '__main__':
    legend = {'#': Wall, 'b': Bot, 'e': Door}

    surf = SURFACE
    room = Room(surf, legend)
    x, y = room.bots_pos()

    while True:
        bot = Bot()
        v = Vector(x, y)
        d, f = bot.get_dir(room, v)
        bot.move(d, room, v)
        ds = room.get_destination(d, v)
        x, y = ds.x, ds.y
        if f:
            break
        surf = room.to_string()
        room = Room.act(surf, legend)
