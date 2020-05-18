class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Consumable(Item):
    def __init__(self, name, description, value, heal, amount):
        self.amount = amount
        self.heal = heal
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nHealing: {}\nAmount: {}".format(self.name, self.description, self.value,
                                                                          self.heal, self.amount)


class Lembas_Bread(Consumable):
    def __init__(self) -> object:
        super().__init__(name="Lembas Bread",
                         description="The bread of the elven people, it will nourish the soul",
                         value=15,
                         heal=25,
                         amount=1)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         damage=5)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=10,
                         damage=10)


class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                         description="A typical sword, good to defend yourself in battles against foe",
                         value=25,
                         damage=15)


class Staff(Weapon):
    def __init__(self):
        super().__init__(name="Staff",
                         description="A rare staff, cast magical spells with it with high damage",
                         value=50,
                         damage=25)


class Ring(Weapon):
    def __init__(self):
        super().__init__(name="The Ring",
                         description="One Ring to Rule them all",
                         value=100,
                         damage=50)
