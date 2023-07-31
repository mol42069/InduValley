import math
import threading
import pygame as pg
from win32api import GetSystemMetrics
from resources.resource_loader import SaveMng
from scripts.map import Map
from scripts.player import Player
from scripts import enums
# from resources.Maps.map_generator import MapGen
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
    scale = 80
    entity_scale = 80
    item_scale = 50
    save_name = "save1"
    pg.init()

    #MapGen() # <---- generate the temporary "Farm" Layout

    screen_size = (GetSystemMetrics(0), GetSystemMetrics(1))
    root = pg.display.set_mode(screen_size, pg.FULLSCREEN)

    sprite_loader = SaveMng(scale=scale, entity_scale = entity_scale, item_scale=item_scale)

    cur_map = Map(sprite_loader, starting_map, save_name, scale)
    player = Player(cur_map.player_start_pos, screen_size, sprite_loader, cur_map)

    screen_thread = threading.Thread(target=screen_threading, args=(root,player, screen_size, scale, cur_map,))
    screen_thread.start()

    while running:

        cur_map.map.blit(player.sprite, (player.pos[enums.Cor.X.value], player.pos[enums.Cor.Y.value] - entity_scale))
        root.blit(cur_map.map, cur_map.pos)

        root.blit(cur_map.hot_surf, cur_map.hot_pos)

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

                case pg.MOUSEBUTTONDOWN:
                    if pg.mouse.get_pressed()[2]:

                        mouse_pos = pg.mouse.get_pos()
                        m_pos = [mouse_pos[0], mouse_pos[1]]
                        player.r_click(m_pos, scale)

                    elif pg.mouse.get_pressed()[0]:

                        mouse_pos = pg.mouse.get_pos()
                        m_pos = [mouse_pos[0], mouse_pos[1]]
                        player.l_click(m_pos, scale)

                case pg.MOUSEBUTTONUP:
                    pass

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
            player.move(left, right, up, down, -3, 0)
        elif right:
            player.move(left, right, up, down, 3, 0)
        if up:
            player.move(left, right, up, down, 0, -3)
        elif down:
            player.move(left, right, up, down, 0, 3)

        if not right and not left and not up and not down:
            player.sprite = player.ani_sprites[player.direction][3]
            player.ani_counter = 3




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
            pass



def esc_menu():
    global running

    running = False
    exit()                      # TODO: here we need to make an escape menu !

if __name__ == "__main__":
    main()
