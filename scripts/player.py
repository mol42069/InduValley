import math
import time
from scripts import enums

class Player:
    def __init__(self, pos, screen_size, sprite_loader, map_x):

        self.ani_counter = 0
        self.pos = pos
        self.screen_size = screen_size
        self.map = map_x
        self.sprite_loader = sprite_loader
        self.ani_sprites = sprite_loader.get_ani("Player")
        self.sprite = sprite_loader.get_entity_sprite("Player")
        self.s_time = time.time()
        self.direction = enums.Direction.RIGHT.value

        return

    def teleport(self, pos):

        self.pos = pos

        return

    def animation(self):

        if self.s_time + 0.06 < time.time():            # The float value here changes the animation speed
            self.s_time = time.time()
            self.ani_counter += 1

            if self.ani_counter < len(self.ani_sprites[self.direction]):
                self.sprite = self.ani_sprites[self.direction][self.ani_counter]

            else:
                self.ani_counter = 0
                self.sprite = self.ani_sprites[self.direction][self.ani_counter]

        return

    def move(self, left, right, up, down, movement_x=0, movement_y=0):

        if left:
            self.direction = enums.Direction.LEFT.value

        elif right:
            self.direction = enums.Direction.RIGHT.value

        elif up:
            self.direction = enums.Direction.UP.value

        elif down:
            self.direction = enums.Direction.DOWN.value


        if self.check_collision(movement_x, movement_y):
            self.pos[0] += movement_x
            self.pos[1] += movement_y

            self.animation()

    def check_collision(self, movement_x, movement_y):         # add collision checks for stuff on the map

        if self.pos[0] + movement_x > self.map.map.get_width() - 29 or self.pos[0] + movement_x < 50:
            return False

        elif self.pos[1] + movement_y > self.map.map.get_height() - 59 or self.pos[1] + movement_y < 30:
            return False

        else:
            return True
    def draw(self):

        return

    def r_click(self, pos, scale):

        pos[0] -= self.map.pos[0]
        pos[1] -= self.map.pos[1]

        p_pos = (self.pos[0] + 25, self.pos[1] + 35)

        p_on_t = [math.floor(p_pos[0] / scale), math.floor(p_pos[1] / scale)]

        temp_col = self.map.map_tiles[ :(p_on_t[0] + 3)]
        temp_col = temp_col[(p_on_t[0]): ]
        temp_tiles = []

        for col in temp_col:

            temp_row = col[ :(p_on_t[1] + 2)]
            temp_row = temp_row[(p_on_t[1] - 1):]
            temp_tiles.append(temp_row)


        for col in temp_tiles:
            for row in col:
                if row.rect.collidepoint((pos[0], pos[1])):
                    if row.tillable:
                        row.surf.blit(self.sprite_loader.get_env_sprite("Stone"), (0, 0))
                        row.type = "Stone"

    def l_click(self, pos, scale):

        pos[0] -= self.map.pos[0]
        pos[1] -= self.map.pos[1]

        p_pos = (self.pos[0] + 25, self.pos[1] + 35)

        p_on_t = [math.floor(p_pos[0] / scale), math.floor(p_pos[1] / scale)]

        temp_col = self.map.map_tiles[ :(p_on_t[0] + 3)]
        temp_col = temp_col[(p_on_t[0]): ]
        temp_tiles = []

        for col in temp_col:

            temp_row = col[ :(p_on_t[1] + 2)]
            temp_row = temp_row[(p_on_t[1] - 1):]
            temp_tiles.append(temp_row)


        for col in temp_tiles:
            for row in col:
                if row.rect.collidepoint((pos[0], pos[1])):
                    if row.tillable:

                        row.surf.blit(self.sprite_loader.get_env_sprite("Dirt"), (0,0))
                        row.type = "Dirt"

    def update_inv(self):

        return

    def build(self):

        return
