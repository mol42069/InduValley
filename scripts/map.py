import math
from scripts.block import *
import pygame as pg
from scripts.Items.inventory import *

class Map:

    def __init__(self, sprite_loader, map_name, save_name, scale=50):

        self.map_lst = [[]]
        self.map_tiles = [[]]
        self.sprite_loader = sprite_loader
        self.map = None

        self.load_map(map_name, scale)
        self.save_name = save_name
        self.scale = scale
        self.player_start_pos = [500, 500]
        self.pos = [0, 0]
        self.prev_pos = self.pos
        self.hot_bar = [None, None, None, None, None, None, None, None, None, None]
        for i in range(0, 10):
            if i % 3 == 0:
                sprite = sprite_loader.get_env_sprite("Dirt")
            elif i % 3 == 1:
                sprite = sprite_loader.get_env_sprite("Stone")
            else:
                sprite = sprite_loader.get_env_sprite("Grass")

            self.hot_bar[i] = InvTiles(sprite_loader, sprite, "Ta", 99)

        self.inventory = []
        self.hot_surf = sprite_loader.get_bg_sprite("HotBar", (550, 50))
        self.hot_pos = (685, 1030)

    def load_map(self, map_name, scale=50):

        self.map_lst = self.sprite_loader.get_map(map_name)
        self.map = pg.Surface(((len(self.map_lst) - 1) * scale, len(self.map_lst[enums.Cor.X.value]) * scale))

        self.build_map(scale)

        return

    def build_map(self, scale=50):

        # init = self.map_lst[-1].pop()
        # bg = init[1]
        # self.player_start_pos = init[2]
        # self.map.blit(self.sprite_loader.get_bg_sprite(bg, (self.map.get_width(), self.map.get_height())), (0, 0))

        for x, col in enumerate(self.map_lst):

            col_tiles = []

            for y, row in enumerate(col):
                sprite = self.sprite_loader.get_env_sprite(row[:-3])
                t_or_nt = row[-2:]

                if t_or_nt == "Ta":
                    tile = TillAble(sprite, (x * scale,y * scale), row[:-3])

                elif t_or_nt == "nT":
                    tile = Tile(sprite, (x * scale,y * scale), row[:-3])

                else:
                    tile = Tile(sprite,(x * scale,y * scale), row[:-3])

                col_tiles.append(tile)

            self.map_tiles.append(col_tiles)

    def draw(self, root, player, screen_size, scale=50):

        # we draw the player on the Surface "map"

        self.map.blit(player.sprite, (player.pos[enums.Cor.X.value] - (scale / 2), player.pos[enums.Cor.Y.value] - scale))

        # we define where top_left of the Surface "map" should be

        if player.pos[enums.Cor.X.value] < screen_size[enums.Cor.X.value] / 2:
            self.pos[enums.Cor.X.value] = 0

        elif self.map.get_width() - player.pos[enums.Cor.X.value] < screen_size[enums.Cor.X.value] / 2:
            self.pos[enums.Cor.X.value] = -(self.map.get_width() - screen_size[enums.Cor.X.value])

        else:
            self.pos[enums.Cor.X.value] = math.floor(-(player.pos[enums.Cor.X.value] - screen_size[enums.Cor.X.value] / 2))


        if player.pos[enums.Cor.Y.value] < screen_size[enums.Cor.Y.value] / 2:
            self.pos[enums.Cor.Y.value] = 0

        elif self.map.get_height() - player.pos[enums.Cor.Y.value] < screen_size[enums.Cor.Y.value] / 2:
            self.pos[enums.Cor.Y.value] = -(self.map.get_height() - screen_size[enums.Cor.Y.value])

        else:
            self.pos[enums.Cor.Y.value] = math.floor(-(player.pos[enums.Cor.Y.value] - screen_size[enums.Cor.Y.value] / 2))

        self.hot_bar_mng()

        root.blit(self.map, self.pos)
        root.blit(self.hot_surf, self.hot_pos)
        #pg.display.update()


        return root


    def update(self, root, player, screen_size, scale=50):

        if self.map is not None:
            self.map.fill((0, 10, 0))

            for x, col in enumerate(self.map_tiles):
                for y, row in enumerate(col):
                    row.draw_t(self.map)

            root = self.draw(root, player, screen_size, scale)

        return root

    def inv_manager(self, scale):


        return

    def hot_bar_mng(self):

        self.hot_surf = self.sprite_loader.get_bg_sprite("HotBar", (550, 50))

        for i in range(0, 10):
            if self.hot_bar[i] is not None:
                self.hot_surf.blit(self.hot_bar[i].sprite, ((2 + (50 * i) + (5 * (i - 1))), 2))

        pass
