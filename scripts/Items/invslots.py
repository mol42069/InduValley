import pygame as pg
from copy import copy

class InvSlot:

    def __init__(self, sprite_loader, scale, amount, t_type, pos=(0,0)):
        self.sprite_loader = sprite_loader
        self.sprite = sprite_loader.get_item_sprite("EmptyInv")
        self.scale = scale
        self.surf = pg.Surface((scale, scale))
        self.pos = pos
        self.surf.blit(self.sprite, (0, 0))
        self.amount = amount
        self.type = t_type

        self.font = pg.font.SysFont("arial", 15)
        self.font.bold = True

    def change(self, t_type, amount):           # we change what is in what inventory slot
        self.type = t_type
        self.amount = amount
        self.sprite = self.sprite_loader.get_item_sprite(self.type)
        self.surf.blit(self.sprite, (0, 0))


    def draw(self, surface):
        surface.blit(self.surf, self.pos)

    def update(self, surface):                                          # we update the contends and draw the corresponding sprites to the hot-bar surface

        if self.type is None:
            self.sprite = self.sprite_loader.get_item_sprite("EmptyInv")

        else:
            self.sprite = self.sprite_loader.get_item_sprite(self.type)

        self.surf.blit(self.sprite,(0, 0))

        if self.amount != 0:
            label = self.font.render(str(self.amount), 1, (255, 255, 255))
            self.surf.blit(label, ((self.scale / 10), (self.scale - (self.scale / 2) + 5)))


class HotBarSlot(InvSlot):

    def __init__(self, sprite_loader, scale, amount, t_type, hot_pos):
        super().__init__(sprite_loader, scale, amount, t_type)
        self.hot_pos = hot_pos
        self.select = False

    def draw_hot(self, surface):
        surface.blit(self.surf, self.hot_pos)

    def unselect(self):                 # we make sure the red square isn't there anymore
        self.select = False
        self.surf.blit(self.sprite, (0, 0))

    def selected(self):                                                 # we call this if this hot-bar-slot is selected and draw a red square around the sprite
        self.select = True
        temp_sprite = copy(self.sprite_loader.get_item_sprite("HotHover"))
        temp_sprite = pg.transform.scale(temp_sprite, (self.scale, self.scale))
        self.surf.blit(temp_sprite, (0, 0))

    def update(self, surface):                                          # we update the contends and draw the corresponding sprites to the hot-bar surface
        if self.type is None:
            self.sprite = self.sprite_loader.get_item_sprite("EmptyInv")

        else:
            self.sprite = self.sprite_loader.get_item_sprite(self.type)

        self.surf.blit(self.sprite,(0, 0))

        label = self.font.render(str(self.amount), 1, (255, 255, 255))

        # we check if this is selected and then go to the right method (unselect()/selected())

        if self.select:
            self.selected()
            if self.amount != 0:
                self.surf.blit(label,( (self.scale / 10), (self.scale - (self.scale / 3))))
            self.draw_hot(surface)

        else:
            self.unselect()
            if self.amount != 0:
                self.surf.blit(label, ((self.scale / 9), (self.scale - (self.scale / 3))))
            self.draw_hot(surface)
