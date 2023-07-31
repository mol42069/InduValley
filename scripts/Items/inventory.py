from scripts.Items.invslots import *
import pygame as pg

class InvTiles:

    def __init__(self, sprite_loader, sprite, t_type, amount):
        self.sprite = sprite
        self.t_type = t_type
        self.amount = amount
        self.sprite_loader = sprite_loader
        self.exist = True

    def draw(self, surface, pos):
        surface.blit(self.sprite, pos)

    def use(self, tile):
        tile.sprite = self.sprite
        if self.amount == 0:
            self.exist = False


class Weapons(InvTiles):

    def __init__(self, sprite_loader, sprite, t_type, cooldown):
        super().__init__(sprite_loader, sprite, t_type, 1)
        self.cooldown = cooldown

    def use(self, tile):
        pass  # TODO: here we need to add attacking but first we need to add enemies

    def block(self):
        pass  # TODO: same as above but just with blocking


class Tools(InvTiles):

    def __init__(self, sprite_loader, sprite, t_type, speed):
        super().__init__(sprite_loader, sprite, t_type, 1)
        self.speed = speed


class Pickaxe(Tools):

    def __init__(self, sprite_loader, sprite, t_type, speed):
        super().__init__(sprite_loader, sprite, t_type, speed)

    def use(self, tile):

        if tile.type == "Stone":
            tile.sprite = self.sprite_loader.get_env_sprite("Dirt")

# TODO: we need add stuff for the other tools


class Inventory:

    def __init__(self, sprite_loader, scale):
        self.sprite_loader = sprite_loader
        self.scale = scale
        self.items = [["Dirt:099", "Stone:001", "Grass:005", "None:000", "None:000", "None:000", "None:000", "None:000", "None:000", "None:000"]]
        pass

class HotBar(Inventory):

    def __init__(self, sprite_loader, scale, hot_pos, hot_size):
        super().__init__(sprite_loader, scale)
        self.hot_size = hot_size
        self.hot_bar = [None, None, None, None, None, None, None, None, None, None]
        self.hot_pos = hot_pos
        self.sprite = sprite_loader.get_bg_sprite("HotBar", self.hot_size)
        self.surf = pg.Surface((self.sprite.get_width(), self.sprite.get_height()))

        for i in range(0, 10):
            if self.hot_bar[i] is None:
                t_type = self.items[0][i]
                amount = int(t_type[-3:])
                t_type = t_type[:-4]
                if t_type == "None":
                    t_type = None

                i_pos = [3 + (i * self.scale), 3]

                self.hot_bar[i] = HotBarSlot(self.sprite_loader, self.scale , amount, t_type, i_pos)

        self.selected = 0
        self.hot_bar[self.selected].selected()

    def scroll(self, amount):
        self.selected += amount
        if self.selected > 9:
            self.selected = 0

        elif self.selected < 0:
            self.selected = 9

        for x, hot_tile in enumerate(self.hot_bar):
            if self.selected == x:
                hot_tile.selected()

            else:
                hot_tile.unselect()


    def update(self):
        for x, hot_tile in enumerate(self.hot_bar):
            if hot_tile.amount == 0:
                hot_tile.type = None
                self.items[0][x] = "None:000"

            hot_tile.update(self.surf)

    def draw(self, surface):
        surface.blit(self.surf, self.hot_pos)

    def get_item(self):
        return self.hot_bar[self.selected].type

    def item_used(self):
        self.hot_bar[self.selected].amount -= 1
