from random import randrange

from constants import *


class Dice:
    def __init__(self, sides):
        self.sides = sides
        self.font = pg.font.Font(None, 30)
        self.image = self.load_image(f"assets/dices/d{sides}.png")
        self.position = self.get_position()
        self.result = sides

    def get_position(self):
        return WIN_SIZE.x / 2 - self.image.get_width() / 2, WIN_SIZE.y / 3 - self.image.get_height() / 2

    def roll(self):
        width, height = self.image.get_size()
        x, y = self.position
        mouse_pos = pg.mouse.get_pos()
        if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
            self.result = randrange(self.sides) + 1

    def update(self):
        pass

    def render(self, surface):
        surface.blit(self.image, self.position)

        _text = self.font.render(f'{self.result}', True, (255, 255, 255))
        _position = WIN_SIZE.x / 2 - _text.get_width() / 2, \
            WIN_SIZE.y / 3 - _text.get_height() / 2 + self.offset(self.sides)
        surface.blit(_text, _position)

    def load_image(self, path):
        return pg.transform.scale(pg.image.load(path), DICE_SIZE)

    def offset(self, sides):
        return 12 if sides == 4 or sides == 20 else 0
