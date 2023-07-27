import pygame as pg
import os
class SaveMng:
    entity_sprites = {}
    environment_sprites = {}
    item_sprites = {}
    bg_sprites = {}
    maps = {}

    def __init__(self, scale, entity_scale, item_scale, bg_scale):
        self.entity_sprites = {}
        self.environment_sprites = {}
        self.item_sprites = {}
        self.bg_sprites = {}
        self.maps = {}

        self.load_entity(entity_scale)
        self.load_items(item_scale)
        self.load_environment(scale)
        self.load_background(bg_scale)


    def get_entity_sprite(self, entity_name = ""):
        return self.entity_sprites[entity_name]

    def get_item_sprite(self, item_name = ""):
        return self.item_sprites[item_name]

    def get_env_sprite(self, env_name = ""):
        return self.environment_sprites[env_name]

    def get_bg_sprite(self, bg_name = ""):
        return self.bg_sprites[bg_name]

    def get_map(self, map_name = ""):
        return self.maps[map_name]

    def load_entity(self, scale):                     # scale is entity-scale

        directory = os.listdir('./Entity')

        for filename in directory:
            if '.' in filename:
                cur_sprite = pg.image.load('./Entity/' + filename)
                cur_sprite = pg.transform.scale(cur_sprite, (scale, scale))
                filename = filename[:-4]
                self.entity_sprites.update({filename : cur_sprite})

            else:
                print("ERROR: Entity Filesystem is broken")
                exit()

    def load_environment(self, scale):                # scale is environment-scale

        directory = os.listdir('./Environment')

        for filename in directory:
            if '.' in filename:
                cur_sprite = pg.image.load('./Environment/' + filename)
                cur_sprite = pg.transform.scale(cur_sprite, (scale, scale))
                filename = filename[:-4]
                self.environment_sprites.update({filename : cur_sprite})

            else:
                print("ERROR: Environment Filesystem is broken")
                exit()

    def load_items(self, scale):                      # scale is items-scale

        directory = os.listdir('./Items')

        for filename in directory:
            if '.' in filename:
                cur_sprite = pg.image.load('./Items/' + filename)
                cur_sprite = pg.transform.scale(cur_sprite, (scale, scale))
                filename = filename[:-4]
                self.item_sprites.update({filename : cur_sprite})

            else:
                print("ERROR: Item Filesystem is broken")
                exit()

    def load_background(self, scale):                     # scale is entity-scale

        directory = os.listdir('./Background')

        for filename in directory:
            if '.' in filename:
                cur_sprite = pg.image.load('./Background/' + filename)
                cur_sprite = pg.transform.scale(cur_sprite, (scale, scale))
                filename = filename[:-4]
                self.bg_sprites.update({filename : cur_sprite})

            else:
                print("ERROR: Background Filesystem is broken")
                exit()

    def load_maps(self, save_name):                            # we load map build
        path = "./Maps/" + save_name
                                                            # TODO: load a map after save map
        return

    def create_save(self, save_name):                       # TODO: copy everything to the folder "save_name"
        path = "./Maps/" + save_name

        return

    def save(self, save_name):                              # TODO: figure out how to save a map!!      <- First
        path = "./Maps/" + save_name
