import math
import threading
import pygame as pg
from win32api import GetSystemMetrics
from resources.resource_loader import SaveMng
from scripts.map import Map
from scripts.player import Player
from scripts import enums
from scripts.Items.inventory import *
# from resources.Maps.map_generator import MapGen
import time

grey = (50, 50, 50)
running = True
items =  None

def key_pressed(input_key):
    keys_pressed = pg.key.get_pressed()
    if keys_pressed[input_key]:
        return True
    else:
        return False

def main():
    global running, items

    starting_map = "Farm"
    scale = 80
    entity_scale = 80
    item_scale = 50
    save_name = "save1"
    pg.init()
    pg.font.init()

    inv_o = False

    #MapGen() # <---- generate the temporary "Farm" Layout

    screen_size = (GetSystemMetrics(0), GetSystemMetrics(1))
    root = pg.display.set_mode(screen_size, pg.FULLSCREEN)

    sprite_loader = SaveMng(scale=scale, entity_scale = entity_scale, item_scale=item_scale)

    cur_map = Map(sprite_loader, starting_map, save_name, scale)

    inv_size = (520, 230)
    inv_pos = ((screen_size[0] - inv_size[0]) / 2, (screen_size[1] - inv_size[1]) / 2)
    inventory = Inventory(sprite_loader, item_scale, inv_pos, inv_size)
    items = inventory.items

    hot_size = (505, 56)
    hot_pos = ((screen_size[0] - hot_size[0]) / 2, screen_size[1] - hot_size[1])
    hot_bar = HotBar(sprite_loader, item_scale, hot_pos, hot_size, items)

    player = Player(cur_map.player_start_pos, screen_size, sprite_loader, cur_map, hot_bar)

    screen_thread = threading.Thread(target=screen_threading, args=(root,player, screen_size, scale, cur_map, hot_bar,))
    screen_thread.start()


    while running:

        # we draw the player on the map surface then draw that surface on the root surface and at last we draw the hot-bar
        # to the root surface.
        cur_map.map.blit(player.sprite, (player.pos[enums.Cor.X.value], player.pos[enums.Cor.Y.value] - entity_scale))
        root.blit(cur_map.map, cur_map.pos)
        hot_bar.draw(root)
        if inv_o:
            inventory.i_update(items)
            inventory.draw()
            root.blit(inventory.surf, inventory.pos)


        pg.display.update()

        # we check for events and call r_click and l_click for the clicked mouse buttons.

        for event in pg.event.get():

            match event.type:
                case pg.QUIT:
                    running = False
                    exit()

                case pg.KEYDOWN:
                    match event.key:
                        case pg.K_ESCAPE:
                            esc_menu()

                        case pg.K_TAB:
                            inv_o = not inv_o

                        case pg.K_1:
                            hot_bar.key_scroll(0)

                        case pg.K_2:
                            hot_bar.key_scroll(1)

                        case pg.K_3:
                            hot_bar.key_scroll(2)

                        case pg.K_4:
                            hot_bar.key_scroll(3)

                        case pg.K_5:
                            hot_bar.key_scroll(4)

                        case pg.K_6:
                            hot_bar.key_scroll(5)

                        case pg.K_7:
                            hot_bar.key_scroll(6)

                        case pg.K_8:
                            hot_bar.key_scroll(7)

                        case pg.K_9:
                            hot_bar.key_scroll(8)

                        case pg.K_0:
                            hot_bar.key_scroll(9)

                case pg.MOUSEBUTTONDOWN:
                    if pg.mouse.get_pressed()[2]:           # <- Right-click

                        mouse_pos = pg.mouse.get_pos()
                        m_pos = [mouse_pos[0], mouse_pos[1]]

                        if inv_o:
                            if not inventory.rect.collidepoint(m_pos):
                                player.r_click(m_pos, scale)

                            else:

                                Inventory.inv_l_click(m_pos=mouse_pos)


                        else:
                            player.r_click(m_pos, scale)

                    elif pg.mouse.get_pressed()[0]:       # <- Left-click

                        mouse_pos = pg.mouse.get_pos()
                        m_pos = [mouse_pos[0], mouse_pos[1]]

                        if inv_o:
                            if not inventory.rect.collidepoint(m_pos):
                                player.l_click(m_pos, scale)

                            else:
                                pass            # TODO: Mouse in Inventory function must be called

                        else:
                            player.l_click(m_pos, scale)

                case pg.MOUSEBUTTONUP:
                    if pg.mouse.get_pressed()[0]:
                        inventory.inv_l_click_release()

                case pg.MOUSEWHEEL:
                    hot_bar.scroll(event.y)     # we scroll through the hot-bar

        # we poll for all the keys we need then according to what's pressed we call the move function with the corresponding
        # variables.

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

        # we change the sprite to the standing sprite while the player isn't moving.

        if not right and not left and not up and not down:
            player.cur_ani = player.idle_sprites[player.direction]
            player.animation()




def screen_threading(root, player, screen_size, scale, cur_map, hot_bar):

    # we want to run the updates in a separate thread, so we can get more fps.

    global running

    while running:

        cur_map.update(root, player, screen_size, scale)
        hot_bar.update(items)


def esc_menu():
    global running

    # whatever we do when "esc" is pressed.

    running = False
    exit()                      # TODO: here we need to make an escape menu !

if __name__ == "__main__":
    main()
