import numpy as np

def directions_from_coordinates(a, b):
    x1, y1 = a
    x2, y2 = b
    delx = x1 - x2
    dely = y1 - y2
    if delx > 0: # west (left)
        if dely > 0: # north (top)
            if delx > 1:
                if dely > 1:
                    return "nw"
                else:
                    return "west"
            else:
                return "north"
        else:
            if delx > 1:
                if dely > 1:
                    return "sw"
                else:
                    return "west"
            else:
                return "south"

    else: # east or flat
        if dely > 0: # north (top)
            if delx > 1:
                if dely > 1:
                    return "ne"
                else:
                    return "east"
            else:
                return "north"
        else:
            if delx > 1:
                if dely > 1:
                    return "ne"
                else:
                    return "east"
            else:
                return "south"


def closest_point(arr, pt): # arr is array of row and columns
    rows, cols = arr
    n = len(rows)
    distances = np.array([abs(rows[i] - pt[0]) + abs(cols[i] - pt[1]) for i in range(n)])
    closest = np.argmin(distances)
    return (rows[closest], cols[closest])
    

def scanboard(board, pos, teammate): # for now, just gives directions for nearest enemy and powerup
    enemies = np.where(board > 9)
    powerups = np.where((9 > board) & (board > 5) & (board != teammate))

    if enemies[0].size != 0:
        closest_enemy = directions_from_coordinates(pos, closest_point(enemies, pos))
    else:
        closest_enemy = "nowhere"

    if powerups[0].size != 0:
        closest_powerup = directions_from_coordinates(pos, closest_point(powerups, pos))
    else:
        closest_powerup = "nowhere"

    return closest_enemy , closest_powerup

def scanboard_richer(board, pos, self_id): 
    enemies = np.where((board > 9) & (board != self_id))
    #print(self_id)
    #print(board[pos])
    closest_enemy_coords = closest_point(enemies, pos) # as long as we're alive, at least one will exist
    return closest_enemy_coords

def get_agent_new_pos(board, enemy_id, last_pos): #O(5), as if anyone cares though
    m, n = board.shape
    x, y = last_pos
    for xn, yn in [(x, y), (x + 1, y), (x - 1, y), (x, y -1), (x, y + 1)]:
        if 0 <= xn < m and 0 <= yn < n and board[xn, yn] == enemy_id:
            return (xn, yn)
    # else enemy is dead

"""
def get_agent_new_pos(board, enemy_id):
    enemy_coords = np.where((board == enemy_id))
    xs, ys = enemy_coords
    if len(xs) < 1:
        return None
    else:
        return xs[0], ys[0]
"""
