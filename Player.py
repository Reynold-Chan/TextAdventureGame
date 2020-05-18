import items
import random
import world


class Player():
    def __init__(self):
        self.inventory = [items.Lembas_Bread(), items.Rock()]
        self.hp = 75
        self.location_x, self.location_y = world.starting_position
        self.victory = False
        self.xp = 0
        self.level = 1
        self.base_damage = 5

    def is_alive(self):
        return self.hp > 0

    def level_up(self):
        if self.xp > 50*self.level:
            self.base_damage += 5
            self.xp -= 50*self.level
            print("You've gain enough knowledge of Middle Earth and understand the armies of Modor,"
                  "Your base damage is now {}".format(self.base_damage))

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def heal(self):
        if self.inventory[0].amount > 0:
            self.inventory[0].amount -= 1
            self.hp += self.inventory[0].heal
            print("Your HP is {}".format(self.hp))
        else:
            print("You have no more Lembas Bread, Go find some more")

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i

        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= (best_weapon.damage + self.base_damage)
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
            print("You gained {}XP".format(enemy.xp))
            self.xp += enemy.xp
            self.level_up()
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])
