import os

class Node(object):
    def __init__(self, action, root, state):
        self.action = action
        self.root = root
        self.state = state


SURFACE = [
    '#######',
    '#--#--#',
    '#--#-b#',
    '#--#--#',
    'e-----#',
    '#-----#',
    '#######'
]

FILENAME = 'maze.txt'
DIRECTIONS = {'LEFT': (0, 1), 'RIGHT': (0, -1), 'UP': (1, 0), 'DOWN': (-1, 0)}

def read_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            surf = [line.rstrip('\n') for line in f.readlines()]
        return surf
    else:
        return SURFACE

def write_to_file(filename, surf):
    with open(filename, 'w') as f:
        for line in surf:
            f.write(line)
            f.write('\n')

def parse_maze():
    pass

def get_start_and_goal(maze):
    start, goal = None, None

    for x in range(len(maze)):
        for y in range(len(maze[0])):
            ch = maze[x][y]
            if ch == 'b':
                start = (x, y)
            if ch == 'e':
                goal = (x, y)
    return start, goal

def is_inside(neighbour, maze):
    h, w, x, y = len(maze), len(maze[0]), neighbour[0], neighbour[1]

    # Check if the neighbour is not a wall and is inside the maze
    if (0 <= x < w) and (0 <= y < h) and maze[x][y] != '#':
        return True
    return False

def get_neighbours(maze, node):
    neighbours = list()
    for action in DIRECTIONS.keys():
        neighbour = tuple(map(lambda i, j: i + j, node.state, DIRECTIONS[action]))

        if is_inside(neighbour, maze):
            neighbours.append((action, neighbour))
    return neighbours

def is_empty(frontier):
    if not len(frontier):
        return True
    return False

def remove(frontier, key='bfs'):
    node = None

    if key == 'bfs':
        node = frontier[0]
        frontier = frontier[1:]
    elif key == 'dfs':
        node = frontier.pop()
    else:
        return
    return node, frontier

def contains(frontier, state):
    for item in frontier:
        if item.state == state:
            return True
    return False

def algorithm(start, goal, maze):
    frontier = list()
    explored = list()
    start_node = Node(action=None, root=None, state=start)
    frontier.append(start_node)

    while not is_empty(frontier):
        node, frontier = remove(frontier)

        if node and node.state == goal:
            explored = list()
            while node.root:
                explored.append(node)
                node = node.root
            break

        neighbours = get_neighbours(maze, node)
        for action, current_neighbour in neighbours:
            if not contains(frontier, current_neighbour) and not contains(explored, current_neighbour):
                child_node = Node(action=action, root=node, state=current_neighbour)
                frontier.append(child_node)
        explored.append(node)

    return reversed(explored)

def s(s, index, ch):
    s = [char for char in s]
    s[index] = ch
    return ''.join(s)

if __name__ == '__main__':
    default_state = (2, 5)
    start, goal = get_start_and_goal(read_file(FILENAME))
    route = list(algorithm(start, goal, SURFACE))
    action = route[0].action
    x, y = route[0].state

    if (x, y) != goal:
        SURFACE[start[0]] = s(SURFACE[start[0]], start[1], '-')
        SURFACE[default_state[0]] = s(SURFACE[default_state[0]], default_state[1], '-')
        SURFACE[x] = s(SURFACE[x], y, 'b')
        write_to_file(FILENAME, SURFACE)
        print(action)
    else:
        os.remove(FILENAME)
        print('YOU WON!')

