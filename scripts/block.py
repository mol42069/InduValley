from scripts import enums
import pygame as pg
class Tile:

    def __init__(self, sprite, pos):
        self.sprite = sprite
        self.pos = pos
        self.rect = self.sprite.get_rect()
        self.rect.topleft = self.pos


    def draw(self, root):
        root.blit(self.sprite, self.pos)
        return root

    def collision(self, player):
        player_rect = player.get_rect()
        if player_rect.collidepoint(self.rect):
            return True
        return False

    def draw_t(self, surf, scale):
        surf.blit(self.sprite, (self.pos[0] * scale, self.pos[1] * scale))

        return



class TillAble(Tile):

    def __init__(self, sprite, pos):
        super().__init__(sprite, pos)
        self.tilled = False
        self.crop_type = None
        self.grow_time = 0
        self.harvestable = False

    def till(self):
        self.tilled = True

        return

    def draw_t(self, surf, scale):
        surf = super().draw_t(surf, scale)
        return surf

    def plant(self, crop_type):
        if self.crop_type is None:
            self.crop_type = crop_type
            # player needs to lose a seed

        return

    def update(self):
        if self.crop_type is None and self.tilled:

            pass
        elif self.tilled:
            self.grow_time += 1
            match self.crop_type:
                case 'Blueberry':
                    if self.grow_time == enums.CropTimer.Blueberry.value:
                        self.harvestable = True

                case 'Wheat':
                    if self.grow_time == enums.CropTimer.Wheat.value:
                        self.harvestable = True

        else:

            return




