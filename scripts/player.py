
class Player:
    def __init__(self, pos, screen_size, sprite_loader, mapx):

        self.pos = pos
        self.screen_size = screen_size
        self.map = mapx
        self.sprite = sprite_loader.get_entity_sprite("Player")

        return

    def teleport(self, pos):

        self.pos = pos

        return

    def animation(self):

        return

    def move(self, movement_x=0, movement_y=0):

        if self.check_collision(movement_x, movement_y):
            self.pos[0] += movement_x
            self.pos[1] += movement_y

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
