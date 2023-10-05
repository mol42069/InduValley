import math
from scripts.Items.inventory import *
from scripts.block import *


class Map:

    def __init__(self, sprite_loader, map_name, save_name, scale=50):

        self.map_lst = [[]]
        self.map_tiles = [[]]
        self.sprite_loader = sprite_loader
        self.map = None

        self.load_map(map_name, scale)
        self.map_name = map_name
        self.save_name = save_name
        self.scale = scale
        self.player_start_pos = [500, 500]
        self.pos = [0, 0]
        self.prev_pos = self.pos

        self.inventory = []
        self.last_hover = None
        self.hover_pos = [0, 0]

        self.reachable = None



    def load_map(self, map_name, scale=50):

        # we load the current map from the resource loader which already loaded it from the files than we call the next function

        self.map_lst = self.sprite_loader.get_map(map_name)
        self.map = pg.Surface(((len(self.map_lst) - 1) * scale, len(self.map_lst[enums.Cor.X.value]) * scale))
        self.map_name = map_name
        self.build_map(scale)

        return

    def save_map(self):

        data = []

        for x, col in enumerate(self.map_tiles):
            temp = []
            for tile in col:
                if tile.tillable:
                    temp_str = tile.type + ':Ta'
                else:
                    temp_str = tile.type + ':nT'

                temp.append(temp_str)

            if x == 1:
                data[0] = temp

            else:
                data.append(temp)

        save.save(data, self.save_name, self.map_name)

        return

    def build_map(self, scale=50):

        # we build the map out of the self.map_lst which is where all the tiles are stored for easier saving into a file
        # but those entries are in string format. So we have to slice the information up and then convert them into the
        # format we want to create tiles

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

    def draw(self, root, player, screen_size):
        # we say where the map surface should be in correlation to the screen
        # in accordance with the player position. (player should always be in the middle)

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

        # self.update(root, player, screen_size)
        # root.blit(self.map, self.pos)
        # root.blit(self.hot_surf, self.hot_pos)
        #pg.display.update()
        self.replace_player(player)

        return root

    def replace_player(self, player):

        for x in range(3):
            for y in range(3):
                self.map = self.map_tiles[math.floor(player.pos[0]/self.scale) + x][math.floor(player.pos[1]/self.scale) + (y-1)].draw_t(self.map)


    def update(self, root, player, screen_size, scale=50):

        # here we update the map surface and give the tile which is currently under our mouse a black outline.

        m_pos = pg.mouse.get_pos()

        self.hover_pos = [math.ceil((m_pos[0] - self.pos[0]) / scale), math.floor((m_pos[1] - self.pos[1]) / scale)]
        #print(self.hover_pos)

        try:
            if self.last_hover is not None:
                self.map_tiles[self.last_hover[0]][self.last_hover[1]].surf.blit(self.sprite_loader.get_env_sprite(self.map_tiles[self.last_hover[0]][self.last_hover[1]].type), (0, 0))
                self.last_hover = None

            self.map_tiles[self.hover_pos[0]][self.hover_pos[1]].surf.blit(self.sprite_loader.get_env_sprite("Hover"), (0, 0))

            self.last_hover = self.hover_pos

        except IndexError:
            pass

        if self.map is not None:
            for x, col in enumerate(self.map_tiles):
                for y, row in enumerate(col):
                    row.draw_t(self.map)

            #root = self.draw(root, player, screen_size)

        return root

    def inv_manager(self, scale):


        return
