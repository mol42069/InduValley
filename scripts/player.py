import pygame as pg

class Player:
    def __init__(self, pos, screen_size):
        self.pos = pos
        self.screen_size = screen_size
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
        if self.pos[0] + movement_x > self.screen_size[0] or self.pos[0] + movement_x < 0:
            return False

        elif self.pos[1] + movement_y > self.screen_size[1] or self.pos[1] + movement_y < 0:
            return False

        else:
            return True
    def draw(self):

        return

    def update_inv(self):

        return

    def build(self):

        return
