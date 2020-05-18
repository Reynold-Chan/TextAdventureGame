import items, enemies, actions, world


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.Heal())

        return moves


class StartingRoom(MapTile):
    def intro_text(self):
        return """
        Middle Earth is in great peril, the Dark Lord Sauron threatens to destroy us all
        Defeat Sauron by finding items and gaining experience and knowledge of the dark ways
        Middle Earth is in your hands
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class LootRoom(MapTile):
    Visited: bool = False
    def intro_text(self):
        pass

    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        if not self.Visited:
            self.add_loot(player)
            self.Visited = True
        else:
            pass


class EnemyRoom(MapTile):
    def intro_text(self):
        pass

    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()


class EmptyTilePath(MapTile):
    def intro_text(self):
        return """
        You stop to admire the beauty of Middle Earth. Alas, You must forge onwards.
        """

    def modify_player(self, player):
        # Room has no action on player
        pass


class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant spider jumps down from its web in front of you!
            """
        else:
            return """
            The corpse of a dead spider rots on the ground.
            """


class OgreRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ogre())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            An Ogre roars
            """
        else:
            return """
            The corpse of the giant ogre lays
            """


class Sauramon(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Sauramon())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Sauramon ~ the corrputed ~ laughs at your attempt to destroy Sauron
            """
        else:
            return """
            Sauramon sits lifeless in his chair
            """


class Balrog(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Balrog())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            The Demon roars, his voice is heard all throughout Moria, Balrog appears 
            """
        else:
            return """
            The embers of the Demon Balrog is fading
            """


class Goblin(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Goblin())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            The dark forces of Modor is near, you see a goblin camp
            """
        else:
            return """
            The corpses of the goblin lays in shock
            """


class Sauron(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Sauron())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Sauron lies in front, His eyes piercing through all goodness in Middle Earth
            """
        else:
            return """
            The Dark Lord Sauron is slain for now, He shall return again but for now Middle Earth is free 
            """
            Player.victory = True


class LembasBreadRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Lembas_Bread())

    def add_loot(self, player):
        player.inventory[0].amount += 1

    def intro_text(self):
        if not self.Visited:
            return """
            You Found some Lembas Bread, You go to pick it up
            """
        else:
            return """
            You find solace in this Middle's Earth Beauty
            """


class FindRingRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Ring())

    def intro_text(self):
        if not self.Visited:
            return """
            You hear a voice calling to you in this Cave
            The Ring calls to you, You pick it up.
            """
        else:
            return """
            Golum's Cave reeks of death"""


class FindStaffRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Staff())

    def intro_text(self):
        if not self.Visited:
            return """
            You notice a staff in the City of Rivendell,
            bursting with elven magic
            you pick it up.
            """
        else:
            return"""
            You feel powerful magic emulating here,
            The City of Rivendell  bursting with its streams of life
            """


class FindSwordRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Sword())

    def intro_text(self):
        if not self.Visited:
            return """
            The sword of the kings in Minas Tirith, 
            Man has used it to slay the enemies of Middle earth,
            You pick it up.
            """
        else:
            return"""
            The great city of Minas Tirith , Home of Man,
            City of Gondor
            """



class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        if not self.Visited:
            return """
            You notice something shiny in the of bilbo's house.
            It's a dagger! You pick it up.
            You wonder if Bilbo Baggins will notice it's missing
            """
        else:
            return """
            The shire, where the simple hobbits live"""
