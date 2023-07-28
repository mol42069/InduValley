import time
from scripts import enums

class Player:
    def __init__(self, pos, screen_size, sprite_loader, mapx):

        self.ani_counter = 0
        self.pos = pos
        self.screen_size = screen_size
        self.map = mapx
        self.ani_sprites = sprite_loader.get_ani("Player")
        self.sprite = sprite_loader.get_entity_sprite("Player")
        self.s_time = time.time()
        self.direction = enums.Direction.RIGHT.value

        return

    def teleport(self, pos):

        self.pos = pos

        return

    def animation(self):

        if self.s_time + 0.1 < time.time():
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

        elif self.pos[1] + movement_y > self.map.map.get_height() - 29 or self.pos[1] + movement_y < 80:
            return False

        else:
            return True
    def draw(self):

        return

    def update_inv(self):

        return

    def build(self):

        return
