import pygame as pg

class Map:

    def __init__(self, sprite_loader, map_name, save_name):
        sprite_loader.get_map(map_name)
        self.save_name = save_name


