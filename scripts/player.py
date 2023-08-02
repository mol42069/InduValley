import math
import time
from scripts import enums

class Player:
    def __init__(self, pos, screen_size, sprite_loader, map_x, hot_bar):

        self.ani_counter = 0
        self.pos = pos
        self.screen_size = screen_size
        self.map = map_x
        self.sprite_loader = sprite_loader

        self.direction = enums.Direction.RIGHT.value
        self.ani_sprites = sprite_loader.get_ani("Player")
        self.idle_sprites = sprite_loader.get_ani("IdlePlayer")
        self.cur_ani = self.idle_sprites[self.direction]
        self.sprite = self.cur_ani[0]

        self.s_time = time.time()
        self.hot_bar = hot_bar

        return

    def teleport(self, pos):

        self.pos = pos

        return

    def animation(self):

        # we change the sprite which is used by the player after an amount of time.

        if self.s_time + 0.07 < time.time():            # The float value here changes the animation speed
            self.s_time = time.time()
            self.ani_counter += 1

            if self.ani_counter < len(self.cur_ani):
                self.sprite = self.cur_ani[self.ani_counter]

            else:
                self.ani_counter = 0
                self.sprite = self.cur_ani[self.ani_counter]

        return

    def move(self, left, right, up, down, movement_x=0, movement_y=0):

        # we save in which direction we are currently looking and then check if we are allowed to move where we want to
        # go to. Call upon the animation() function. And we change the position(self.pos) so we fulfilled the movement if
        # we are allowed to.

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

            self.cur_ani = self.ani_sprites[self.direction]

            self.animation()

    def check_collision(self, movement_x, movement_y):         # TODO: add collision checks for stuff on the map

        # we check if the next movement is "legal" aka. we don't walk into anything solid.

        if self.pos[0] + movement_x > self.map.map.get_width() - 29 or self.pos[0] + movement_x < 50:
            return False

        elif self.pos[1] + movement_y > self.map.map.get_height() - 59 or self.pos[1] + movement_y < 30:
            return False

        else:
            return True
    def draw(self):

        return

    def r_click(self, pos, scale):

        # we get where we clicked on the screen and check if this is within a 3x3 area around the player if it is we
        # change the sprite of the clicked tile for whatever is in the hot-bar selected slot.

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

        # we get where we clicked on the screen and check if this is within a 3x3 area around the player if it is we
        # change the sprite of the clicked tile for whatever is in the hot-bar selected slot.

        pos[0] -= self.map.pos[0]
        pos[1] -= self.map.pos[1]

        p_pos = (self.pos[0] + (scale / 2), self.pos[1] + ((scale / 4) * 2))

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
                        sprite = self.hot_bar.get_item()
                        if sprite is not None:
                            if row.type != sprite:
                                row.surf.blit(self.sprite_loader.get_env_sprite(sprite), (0, 0))
                                row.type = sprite
                                self.hot_bar.item_used()

    def update_inv(self):

        return

    def build(self):

        return
