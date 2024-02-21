import sys
from constants import *
from rotated_menu import RotatedMenu
from dice import Dice


class App:
    def __init__(self):
        pg.init()

        self. screen = pg.display.set_mode(WIN_SIZE)
        self.menu = RotatedMenu()
        self.dice = None
        self.is_running = True

        pg.display.set_caption('dice roll')

    def update(self):
        pass

    def render(self):
        self.screen.fill(BG_COLOR)
        self.menu.draw(self.screen)
        if self.dice is not None:
            self.dice.render(self.screen)
        pg.display.flip()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.dice is not None:
                        self.dice.roll()
                    if self.menu.inside_button(event.pos):
                        self.menu.extend = True
            elif event.type == pg.MOUSEBUTTONUP:
                if event.button == 1 and self.menu.extend:
                    index = self.menu.index_of_sector()
                    if index is not None:
                        _sides = int(self.menu.labels[index][1:])
                        self.dice = Dice(_sides)
                    self.menu.extend = False

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
        pg.quit()
        sys.exit()


if __name__ == '__main__':
    app = App()
    app.run()
