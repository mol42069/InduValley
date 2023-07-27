import pygame as pg
from scripts import enums
class Map:

    def __init__(self, sprite_loader, map_name, save_name, scale=50):
        self.map_lst = [[]]
        self.sprite_loader = sprite_loader
        self.map = None
        self.load_map(map_name, scale)
        self.build_map()
        self.save_name = save_name
        self.scale = scale
        self.player_start_pos = [500, 500]
        self.pos = [0, 0]
        self.prev_pos = self.pos

    def load_map(self, map_name, scale=50):
        self.map_lst = self.sprite_loader.get_map(map_name)
        self.map = pg.Surface(((len(self.map_lst) - 1) * scale, len(self.map_lst[enums.Cor.X.value]) * scale))
        self.build_map()
        return

    def build_map(self, scale=80):
        # init = self.map_lst[-1].pop()
        # bg = init[1]
        # self.player_start_pos = init[2]
        # self.map.blit(self.sprite_loader.get_bg_sprite(bg, (self.map.get_width(), self.map.get_height())), (0, 0))
        self.map.fill((0, 0, 0))
        for x, col in enumerate(self.map_lst):
            for y, row in enumerate(col):
                self.map.blit(self.sprite_loader.get_env_sprite(row), (x * scale, y * scale))

        return





    def draw(self, root, player, screen_size, scale=50):

        # we draw the player on the Surface "map"

        self.map.blit(player.sprite, (player.pos[enums.Cor.X.value] - (scale / 2), player.pos[enums.Cor.Y.value] - scale))


        # we define where top_left of the Surface "map" should be

        if player.pos[enums.Cor.X.value] < screen_size[enums.Cor.X.value] / 2:
            self.pos[enums.Cor.X.value] = 0

        elif self.map.get_width() - player.pos[enums.Cor.X.value] < screen_size[enums.Cor.X.value] / 2:
            self.pos[enums.Cor.X.value] = -(self.map.get_width() - screen_size[enums.Cor.X.value])

        else:
            self.pos[enums.Cor.X.value] = -(player.pos[enums.Cor.X.value] - screen_size[enums.Cor.X.value] / 2)


        if player.pos[enums.Cor.Y.value] < screen_size[enums.Cor.Y.value] / 2:
            self.pos[enums.Cor.Y.value] = 0

        elif self.map.get_height() - player.pos[enums.Cor.Y.value] < screen_size[enums.Cor.Y.value] / 2:
            self.pos[enums.Cor.Y.value] = -(self.map.get_height() - screen_size[enums.Cor.Y.value])

        else:
            self.pos[enums.Cor.Y.value] = -(player.pos[enums.Cor.Y.value] - screen_size[enums.Cor.Y.value] / 2)

        root.blit(self.map, self.pos)

        return root


    def update(self, root, player, screen_size, scale=50):
           self.build_map(scale)
           root = self.draw(root, player, screen_size, scale)
           return root