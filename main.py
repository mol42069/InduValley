import pygame as pg
from win32api import GetSystemMetrics
from resources.resource_loader import SaveMng
from scripts.map import Map
from scripts.player import Player

grey = (50, 50, 50)

def key_pressed(input_key):
    keys_pressed = pg.key.get_pressed()
    if keys_pressed[input_key]:
        return True
    else:
        return False

def main():
    starting_map = "Farm"
    scale = 30
    save_name = "save1"
    pg.init()
    screen_size = (GetSystemMetrics(0), GetSystemMetrics(1))
    root = pg.display.set_mode(screen_size, pg.FULLSCREEN)
    pg.display.toggle_fullscreen()
    sprite_loader = SaveMng(scale=scale, entity_scale=40, item_scale=10)
    cur_map = Map(sprite_loader, starting_map, save_name, scale)
    player = Player(cur_map.player_start_pos)

    while True:

        root.fill(grey)
        cur_map.draw(root, player, screen_size)



        for event in pg.event.get():
            print(event.type)
            match event.type:
                case pg.QUIT:
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
            player.move(-0.2, 0)
        elif right:
            player.move(0.2, 0)
        if up:
            player.move(0, -0.2)
        elif down:
            player.move(0, 0.2)


        pg.display.update()



def esc_menu():
    exit()                      # TODO: here we need to make an escape menu !


if __name__ == "__main__":
    main()
