import math
import threading
import pygame as pg
from win32api import GetSystemMetrics
from resources.resource_loader import SaveMng
from scripts.map import Map
from scripts.player import Player
from resources.Maps.map_generator import MapGen
import time

grey = (50, 50, 50)
running = True

def key_pressed(input_key):
    keys_pressed = pg.key.get_pressed()
    if keys_pressed[input_key]:
        return True
    else:
        return False

def main():
    global running
    starting_map = "Farm"
    scale = 50
    target_fps = 144
    frame_t_time = 1000000000 / target_fps
    save_name = "save1"
    pg.init()
    ############################################################MapGen() # <---- generate the temporary "Farm" Layout
    screen_size = (GetSystemMetrics(0), GetSystemMetrics(1))
    root = pg.display.set_mode(screen_size, pg.FULLSCREEN)
    pg.display.toggle_fullscreen()
    sprite_loader = SaveMng(scale=scale, entity_scale=50, item_scale=10)
    cur_map = Map(sprite_loader, starting_map, save_name, scale)
    player = Player(cur_map.player_start_pos, screen_size, sprite_loader, cur_map)
    screen_thread = threading.Thread(target=screen_threading, args=(root,player, screen_size, scale, cur_map,))
    screen_thread.start()

    while running:

        pg.display.update()

        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    running = False
                    exit()

                case pg.KEYDOWN:
                    match event.key:
                        case pg.K_ESCAPE:
                            esc_menu()



        if key_pressed(pg.K_d):
            right = True
        else:
            right = False
        if key_pressed(pg.K_a):
            left = True
        else:
            left = False
        if key_pressed(pg.K_w):
            up = True
        else:
            up = False
        if key_pressed(pg.K_s):
            down = True
        else:
            down = False

        if left:
            player.move(-3, 0)
        elif right:
            player.move(3, 0)
        if up:
            player.move(0, -3)
        elif down:
            player.move(0, 3)




def screen_threading(root, player, screen_size, scale, cur_map):
    global running
    target_fps = 144
    frame_t_time = 1000000000 / target_fps
    s_time = time.time_ns()
    while running:
        frame_time = time.time_ns() - s_time
        if frame_time > frame_t_time:
            s_time = time.time_ns()
            cur_map.update(root, player, screen_size, scale)

        if frame_time != 0:
            print(math.floor(1000000000 / frame_time))



def esc_menu():
    global running
    running = False
    exit()                      # TODO: here we need to make an escape menu !

if __name__ == "__main__":
    main()
