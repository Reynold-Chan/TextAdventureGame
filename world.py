import numpy as np
import random

_world = {}
starting_position = (0, 0)


def generate_tiles():
    itemsRoom = ["FindDaggerRoom","FindSwordRoom","FindStaffRoom","FindRingRoom"]
    """Automatically Generate map.txt file  6x8 grid with various map rooms"""
    x = 6
    y = 8
    itemsAdded = 0
    world = np.random.random((x, y))
    World = []
    for i in range(world.shape[0]):
        row = []
        for j in range(world.shape[1]):
            if world[i][j] <= 0.3:
                row.append("LeambasBreadRoom")
            elif world[i][j] <= 0.7:
                row.append("EmptyTilePath")
            elif world[i][j] <= 0.8:
                row.append("GiantSpiderRoom")
            elif world[i][j] <= 0.9:
                row.append("Goblin")
            elif world[i][j] <= 1:
                row.append("OgreRoom")
        World.append(row)
    #Always start at the corners of the map
    np.array(World)
    World[0][0] = "StartingRoom"
    World[x-1][y-1] = "Sauron"
    World[x-1][0] = "Sauramon"
    World[0][y-1] = "Balrog"
    while itemsAdded != (len(itemsRoom)-1):
        if World[random.randint(1, x - 2)][random.randint(1, y - 2)] in itemsRoom:
            continue
        else:
            World[random.randint(1, x - 2)][random.randint(1, y - 2)] = itemsRoom[itemsAdded]
            itemsAdded +=1
    np.savetxt('resources/map.txt', World, delimiter='\t', fmt="%s")


def load_tiles():
    """Parses a file that describes the world space into the _world object"""
    with open('resources/map.txt', 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('\t'))  # Assumes all rows contain the same number of tabs
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '')  # Windows users may need to replace '\r\n'
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y)
            _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)


def tile_exists(x, y):
    return _world.get((x, y))
