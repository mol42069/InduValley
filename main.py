import pygame as pg
from win32api import GetSystemMetrics
grey = (50, 50, 50)
def main():
    pg.init()
    screen_size = (GetSystemMetrics(0), GetSystemMetrics(1))
    root = pg.display.set_mode(screen_size, pg.FULLSCREEN)
    pg.display.toggle_fullscreen()

    while True:

        root.fill(grey)

        for event in pg.event.get():
            print(event.type)
            match event.type:
                case pg.QUIT:
                    exit()

                case pg.KEYDOWN:
                    match event.key:
                        case pg.K_ESCAPE:
                            esc_menu()


        pg.display.update()

def esc_menu():
    exit()                      # TODO: here we need to make an escape menu !


if __name__ == "__main__":
    main()
