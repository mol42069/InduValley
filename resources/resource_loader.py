import pygame as pg
import os

entity_sprites = {}
environment_sprites = {}
item_sprites = {}
bg_sprites = {}
maps = {}

def init(scale, entity_scale, item_scale, bg_scale):
    load_entity(entity_scale)
    load_items(item_scale)
    load_environment(scale)
    load_background(bg_scale)

def get_entity_sprite(entity_name = ""):
    global entity_sprites
    return entity_sprites[entity_name]

def get_item_sprite(item_name = ""):
    global item_sprites
    return item_sprites[item_name]

def get_environment_sprite(env_name = ""):
    global environment_sprites
    return environment_sprites[env_name]

def get_bg_sprite(bg_name = ""):
    global bg_sprites
    return bg_sprites[bg_name]

def get_map(map_name = ""):
    global maps
    return maps[map_name]

def load_entity(scale):                     # scale is entity-scale
    global entity_sprites
    directory = os.listdir('./Entity')

    for filename in directory:
        if '.' in filename:
            cur_sprite = pg.image.load('./Entity/' + filename)
            cur_sprite = pg.transform.scale(cur_sprite, (scale, scale))
            filename = filename[:-4]
            entity_sprites.update({filename : cur_sprite})

        else:
            print("ERROR: Entity Filesystem is broken")
            exit()

def load_environment(scale):                # scale is environment-scale
    global environment_sprites
    directory = os.listdir('./Environment')

    for filename in directory:
        if '.' in filename:
            cur_sprite = pg.image.load('./Environment/' + filename)
            cur_sprite = pg.transform.scale(cur_sprite, (scale, scale))
            filename = filename[:-4]
            entity_sprites.update({filename : cur_sprite})

        else:
            print("ERROR: Environment Filesystem is broken")
            exit()

def load_items(scale):                      # scale is items-scale
    global item_sprites
    directory = os.listdir('./Items')

    for filename in directory:
        if '.' in filename:
            cur_sprite = pg.image.load('./Items/' + filename)
            cur_sprite = pg.transform.scale(cur_sprite, (scale, scale))
            filename = filename[:-4]
            entity_sprites.update({filename : cur_sprite})

        else:
            print("ERROR: Item Filesystem is broken")
            exit()

def load_background(scale):                     # scale is entity-scale
    global entity_sprites
    directory = os.listdir('./Background')

    for filename in directory:
        if '.' in filename:
            cur_sprite = pg.image.load('./Background/' + filename)
            cur_sprite = pg.transform.scale(cur_sprite, (scale, scale))
            filename = filename[:-4]
            entity_sprites.update({filename : cur_sprite})

        else:
            print("ERROR: Background Filesystem is broken")
            exit()

def load_maps(save_name):                            # we load map build
    path = "./Maps/" + save_name
                                                    # TODO: load a map after save map
    return

def create_save(save_name):                         # TODO: copy everything to the folder "save_name"
    path = "./Maps/" + save_name

    return

def save(save_name):                                # TODO: figure out how to save a map!!      <- First
    path = "./Maps/" + save_name
