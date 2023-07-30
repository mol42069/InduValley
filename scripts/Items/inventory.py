class InvTiles:

    def __init__(self, sprite_loader, sprite, t_type, amount):
        self.sprite = sprite
        self.t_type = t_type
        self.amount = amount
        self.sprite_loader = sprite_loader
        self.exist = True

    def draw(self, surface, pos):
        surface.blit(self.sprite, pos)

    def use(self, tile):
        tile.sprite = self.sprite
        if self.amount == 0:
            self.exist = False


class Weapons(InvTiles):

    def __init__(self, sprite_loader, sprite, t_type, cooldown):
        super().__init__(sprite_loader, sprite, t_type, 1)
        self.cooldown = cooldown

    def use(self, tile):
        pass  # TODO: here we need to add attacking but first we need to add enemies

    def block(self):
        pass  # TODO: same as above but just with blocking


class Tools(InvTiles):

    def __init__(self, sprite_loader, sprite, t_type, speed):
        super().__init__(sprite_loader, sprite, t_type, 1)
        self.speed = speed


class Pickaxe(Tools):

    def __init__(self, sprite_loader, sprite, t_type, speed):
        super().__init__(sprite_loader, sprite, t_type, speed)

    def use(self, tile):

        if tile.type == "Stone":
            tile.sprite = self.sprite_loader.get_env_sprite("Dirt")

# TODO: we need add stuff for the other tools

