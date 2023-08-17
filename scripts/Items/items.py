
class Item:

    def __init__(self, sprite, item_in_plain):
        self.sprite = sprite
        self.item_in_plain = item_in_plain
    def draw(self, surface, pos=(0,0)):
        surface.blit(self.sprite, pos)

    def left_click(self, tile, amount=1):
        return

class Tools(Item):

    def __init__(self, sprite, item_in_plain):
        super().__init__(sprite, item_in_plain)

#TODO: Here will be all the tools pickaxe etc.
# as classes.

class PlaceAbles(Item):

    def __init__(self, sprite, item_in_plain, amount=1, walkable=True, tillable=True):
        super().__init__(sprite, item_in_plain)
        self.amount = amount
        self.walkable = walkable
        self.tillable = tillable

    def left_click(self, tile, amount=1):          # return arg1, arg2 --> arg1 = if item is placed, arg2 = if the item is empty.

        if tile.buildable:
            if self.amount - amount < 0:
                return False, True

            elif self.amount - amount == 0:
                tile.build(self.walkable, self.sprite)
                return True, True

            else:
                tile.build(self.walkable, self.sprite)
                self.amount =- amount
                return True, False

        else:
            return False, False

class Seed(Item):

    def __init__(self, sprite, item_in_plain, crop_type):
        super().__init__(sprite, item_in_plain)
        self.crop_type = crop_type
