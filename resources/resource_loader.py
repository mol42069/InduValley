import pygame as pg
import os
from scripts import save
class SaveMng:
    entity_sprites = {}
    environment_sprites = {}
    item_sprites = {}
    bg_sprites = {}
    maps = {}

    # we load everything in our resources, so we can easily use them later without the need of loading them later

    def __init__(self, scale, entity_scale, item_scale, save_name = 'save1'):

        self.entity_sprites = {}
        self.entity_sprites_name =[]
        self.environment_sprites = {}
        self.env_sprites_name = []
        self.item_sprites = {}
        self.item_sprites_name = []
        self.bg_sprites = {}
        self.bg_sprites_name = []
        self.maps = {}
        self.ani = {}
        self.ani_name = []

        self.load_maps(save_name)
        self.load_entity(entity_scale)
        self.load_items(item_scale)
        self.load_environment(scale)
        self.load_ani(entity_scale)
        self.load_background()


    def get_entity_sprite(self, entity_name = ""):

        return self.entity_sprites[entity_name]

    def get_ani(self, name = ""):

        return self.ani[name]

    def get_item_sprite(self, item_name = ""):

        return self.item_sprites[item_name]

    def get_env_sprite(self, env_name = ""):

        return self.environment_sprites[env_name]

    def get_bg_sprite(self, bg_name = "", scale = (2000, 3000)):

        sprite = pg.transform.scale(self.bg_sprites[bg_name], (scale[0], scale[1]))

        return sprite

    def get_map(self, map_name = ""):

        return self.maps[map_name]

    def load_ani(self, scale):

        directory = os.listdir('./resources/Animations')

        for filename in directory:

            anim = []
            filename_dir = os.listdir('./resources/Animations/' + filename)
            for file in filename_dir:

                state_anim = []
                file_dir = os.listdir('./resources/Animations/' + filename + '/' + file)

                for state in file_dir:

                    try:

                        cur_sprite = pg.image.load('./resources/Animations/' + filename + '/' + file + '/' + state)
                        cur_sprite = pg.transform.scale(cur_sprite, (scale, scale * 2))
                        state_anim.append(cur_sprite)

                    except AttributeError:

                        print("ERROR: Entity Filesystem is broken")
                        exit()

                anim.append(state_anim)

            self.ani.update({filename : anim})

    def load_entity(self, scale):                     # scale is entity-scale

        directory = os.listdir('./resources/Entity')

        for filename in directory:
            if '.' in filename:
                cur_sprite = pg.image.load('./resources/Entity/' + filename)
                cur_sprite = pg.transform.scale(cur_sprite, (scale, scale * 2))
                filename = filename[:-4]
                self.entity_sprites_name.append(filename)
                self.entity_sprites.update({filename : cur_sprite})

            else:
                print("ERROR: Entity Filesystem is broken")
                exit()

    def load_environment(self, scale):                # scale is environment-scale

        directory = os.listdir('./resources/Environment')

        for filename in directory:
            if '.' in filename:
                cur_sprite = pg.image.load('./resources/Environment/' + filename)
                cur_sprite = pg.transform.scale(cur_sprite, (scale, scale))
                filename = filename[:-4]
                self.env_sprites_name.append(filename)
                self.environment_sprites.update({filename : cur_sprite})

            else:
                print("ERROR: Environment Filesystem is broken")
                exit()

    def load_items(self, scale):                      # scale is items-scale

        directory = os.listdir('./resources/Items')

        for filename in directory:
            if '.' in filename:
                cur_sprite = pg.image.load('./resources/Items/' + filename)
                cur_sprite = pg.transform.scale(cur_sprite, (scale, scale))
                filename = filename[:-4]
                self.item_sprites_name.append(filename)
                self.item_sprites.update({filename : cur_sprite})

            else:
                print("ERROR: Item Filesystem is broken")
                exit()

    def load_background(self):                     # scale is entity-scale

        directory = os.listdir('./resources/Background')

        for filename in directory:
            if '.' in filename:
                cur_sprite = pg.image.load('./resources/Background/' + filename)
                filename = filename[:-4]
                self.bg_sprites_name.append(filename)
                self.bg_sprites.update({filename : cur_sprite})

            else:
                print("ERROR: Background Filesystem is broken")
                exit()

    def load_maps(self, save_name):                            # we load map build


                                                            # TODO: load a map after save map
        #self.maps.update({'Farm' : save.load(save_name, "Farm")})

        for m in os.listdir('./resources/Maps/'+ str(save_name) + '/'):

            self.maps.update({str(m[:-4]) : save.load(save_name, str(m[:-4]))})

        return

    def create_save(self, save_name):                       # TODO: copy everything to the folder "save_name"

        path = "./Maps/" + save_name

        return

    def save(self, save_name):                              # TODO: figure out how to save a map!!      <- First

        path = "./Maps/" + save_name
