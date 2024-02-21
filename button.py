from constants import *


class Button:
    def __init__(self, app, position, size, color=BUTTON_COLOR):
        self.app = app
        self.rect = pg.Rect(position, size)
        self.color = color

    def update(self):
        pass

    def render(self):
        pg.draw.rect(self.app.screen, self.color, self.rect)

    def is_pressed(self, mouse_xy):
        return self.rect.collidepoint(mouse_xy)
