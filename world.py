import numpy as np
import random

_world = {}
starting_position = (0, 0)


def generate_tiles():
    # Define special one off rooms
    SpecialRoom = ['StartingRoom', 'Sauron', 'Sauramon', 'Balrog', 'FindDaggerRoom', 'FindSwordRoom', 'FindStaffRoom',
                   'FindRingRoom']
    """Automatically Generate map 6x8 grid with various map rooms"""
    x = 6
    y = 8
    itemsAdded = 0
    #Generate the map
    world = np.random.random((x, y))
    World = []
    for i in range(world.shape[0]):
        row = []
        for j in range(world.shape[1]):
            if world[i][j] <= 0.1:
                row.append('')
            elif world[i][j] <= 0.3:
                row.append('LembasBreadRoom')
            elif world[i][j] <= 0.7:
                row.append('EmptyTilePath')
            elif world[i][j] <= 0.8:
                row.append('GiantSpiderRoom')
            elif world[i][j] <= 0.9:
                row.append('Goblin')
            elif world[i][j] <= 1:
                row.append('OgreRoom')
        World.append(row)
    np.array(World)
    #Add in special one off rooms
    while itemsAdded != len(SpecialRoom):
        if World[random.randint(0, x - 1)][random.randint(0, y - 1)] in SpecialRoom:
            continue
        else:
            World[random.randint(0, x - 1)][random.randint(0, y - 1)] = SpecialRoom[itemsAdded]
            itemsAdded += 1

    #Generate dictionary to map name and location
    for i in range(world.shape[0]):
        cols = World[i]
        for j in range(world.shape[1]):
            tile_name = cols[j]
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (j, i)
            _world[(j, i)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(j, i)


def tile_exists(x, y):
    return _world.get((x, y))
