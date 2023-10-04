from scripts.Items.invslots import *
import pygame as pg


class Inventory:

    def __init__(self, sprite_loader, scale, pos, inv_size):
        self.sprite_loader = sprite_loader
        self.scale = scale
        self.surf = pg.Surface(inv_size)
        self.rect = self.surf.get_rect()
        self.rect.topleft = pos
        self.pos = pos
        self.items = [["Dirt:099", "Stone:001", "Grass:005", "None:000", "None:000", "None:000", "None:000", "None:000", "None:000", "None:000"]]
        self.inv_tiles = []
        if inv_size != (0, 0):
            self.bg = sprite_loader.get_bg_sprite("Inventory", inv_size)
        for i in range(1,4):
            temp_row = []
            for j in range(0, 10):
                temp_row.append("None:000")
            self.items.append(temp_row)

        for y, row in enumerate(self.items):
            temp_row = []

            for x, tile in enumerate(row):

                if y == 0:

                    amount = tile[-3:]
                    t_type = tile[:-4]

                    if t_type == "None":
                        t_type = None

                    pos = ((10 + x * self.scale), (20 + 3 * self.scale))

                    temp_tile = InvSlot(self.sprite_loader, self.scale, amount, t_type, pos)
                    temp_row.append(temp_tile)

                else:

                    amount = tile[-3:]
                    t_type = tile[:-4]

                    if t_type == "None":
                        t_type = None

                    pos = ((10 + x * self.scale), (10 + (y - 1) * self.scale))

                    temp_tile = InvSlot(self.sprite_loader, self.scale, amount, t_type, pos)
                    temp_row.append(temp_tile)

            self.inv_tiles.append(temp_row)


    def i_update(self, items):

        self.items = items
        self.surf.blit(self.bg, (0, 0))

        for x, row in enumerate(self.inv_tiles):
            for y, inv_tile in enumerate(row):
                inv_tile.amount = int(self.items[x][y][-3:])

                if inv_tile.amount == 0:
                    self.items[x][y] = "None:000"

                t_type = self.items[x][y][:-4]

                if t_type == "None":
                    t_type = None

                inv_tile.type = t_type

                inv_tile.update(self.surf)

        return self.items

    def draw(self):

        for row in self.inv_tiles:
            for tile in row:
                tile.draw(self.surf)


class HotBar(Inventory):

    def __init__(self, sprite_loader, scale, pos, hot_size, items):
        super().__init__(sprite_loader, scale, pos, inv_size=(0, 0))

        self.hot_size = hot_size
        self.hot_bar = [None, None, None, None, None, None, None, None, None, None]
        self.sprite = sprite_loader.get_bg_sprite("HotBar", self.hot_size)
        self.surf = pg.Surface((self.sprite.get_width(), self.sprite.get_height()))
        self.items = items

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

        # we just count which way and how much your scrolling and adding it to the selected variable. Then check that
        # we are still in the range we need to be.

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

    def key_scroll(self, index):
        self.selected = index

        for x, hot_tile in enumerate(self.hot_bar):
            if self.selected == x:
                hot_tile.selected()

            else:
                hot_tile.unselect()


    def update(self, items):

        # we check that the items in the current hot-bar are the ones that should be there. And it hasn't been changed to
        # another item in the inventory. Then we check that the amount isn't 0 because if it is there is no item in the
        # slot so we "remove" it aka write "None:000" into the item slot.

        self.items = items

        for x, hot_tile in enumerate(self.hot_bar):
            hot_tile.amount = int(self.items[0][x][-3:])
            hot_tile.type = str(self.items[0][x][:-4])

            if hot_tile.amount == 0:
                hot_tile.type = None
                self.items[0][x] = "None:000"

            hot_tile.update(self.surf)

        return self.items
    def draw(self, surface):
        surface.blit(self.surf, self.pos)

    def get_item(self):

        # we return the type of the item which is currently selected in the hot-bar

        return self.hot_bar[self.selected].type

    def item_used(self):

        # we need to subtract the amount by 1 after we use an item. And add 0's so the slicing of the strings will work.

        self.hot_bar[self.selected].amount -= 1
        if int(self.hot_bar[self.selected].amount) > 99:
            self.items[0][self.selected] = self.items[0][self.selected][:-3] + str(self.hot_bar[self.selected].amount)

        elif int(self.hot_bar[self.selected].amount) > 9:
            self.items[0][self.selected] = self.items[0][self.selected][:-3] + "0" + str(self.hot_bar[self.selected].amount)

        else:
            self.items[0][self.selected] = self.items[0][self.selected][:-3] + "00" + str(self.hot_bar[self.selected].amount)

