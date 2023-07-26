import pygame as pg
from scripts import enums
class Map:

    def __init__(self, sprite_loader, map_name, save_name, scale):
        map_lst = sprite_loader.get_map(map_name)
        self.map = pg.Surface((map_lst.length() * scale, map_lst[0].length * scale))
        self.save_name = save_name
        self.scale = scale
        self.pos = [0, 0]



    def draw(self, root, player, screen_size):

        # we draw the player on the Surface "map"

        self.map.blit(player.sprite, (player.pos[enums.Cor.X.value] - (self.scale / 2), player.pos[enums.Cor.Y.value] - self.scale))


        # we define where top_left of the Surface "map" should be

        if player.pos[enums.Cor.X.value] < screen_size[enums.Cor.X.value] / 2:
            self.pos[enums.Cor.X.value] = 0

        elif self.map.get_width() - player.pos[enums.Cor.X.value] < screen_size[enums.Cor.X.value] / 2:
            self.pos[enums.Cor.X.value] = -(self.map.get_width() - screen_size[enums.Cor.X.value])

        else:
            self.pos[enums.Cor.X.value] = player[enums.Cor.X.value] - screen_size[enums.Cor.X.value] / 2


        if player.pos[enums.Cor.Y.value] < screen_size[enums.Cor.Y.value] / 2:
            self.pos[enums.Cor.Y.value] = 0

        elif self.map.get_height() - player.pos[enums.Cor.Y.value] < screen_size[enums.Cor.Y.value] / 2:
            self.pos[enums.Cor.Y.value] = -(self.map.get_height() - screen_size[enums.Cor.Y.value])

        else:
            self.pos[enums.Cor.Y.value] = player[enums.Cor.Y.value] - screen_size[enums.Cor.Y.value] / 2


        root.blit(self.map, self.pos)

        return root
