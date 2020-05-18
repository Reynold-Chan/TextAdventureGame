class Enemy:
    def __init__(self, name, hp, damage, xp):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.xp = xp

    def is_alive(self):
        return self.hp > 0


class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=10, damage=2, xp=20)


class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=30, damage=10, xp=50)


class Goblin(Enemy):
    def __init__(self):
        super().__init__(name="Goblin", hp=15, damage=4, xp=30)


class Balrog(Enemy):
    def __init__(self):
        super().__init__(name="Balrog - The Demon of Moria", hp=50, damage=15, xp=100)


class Sauramon(Enemy):
    def __init__(self):
        super().__init__(name="Sauramon ~ The White Wizard", hp=50, damage=15, xp=100)


class Sauron(Enemy):
    def __init__(self):
        super().__init__(name="Sauron ~ Dark Lord of Modor", hp=100, damage=20, xp=200)
