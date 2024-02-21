from constants import *


class RotatedMenu:
    def __init__(self, radius=80, center=glm.vec2(WIN_SIZE.x / 2, WIN_SIZE.y-80)):
        self.center = center
        self.radius = radius
        self.labels = ['d4', 'd6', 'd8', 'd10', 'd12', 'd20']
        self.font = pg.font.Font(None, 24)
        self.extend = False

    def update(self):
        pass

    def draw(self, surface):
        if self.extend:
            pg.draw.circle(surface, MENU_COLOR, self.center, self.radius, width=40)
            angle = 2 * math.pi / len(self.labels)

            for i, label in enumerate(self.labels):
                x = self.center.x + (self.radius-20)*math.cos(i * angle)
                y = self.center.y + (self.radius-20)*math.sin(i * angle)
                text = self.font.render(label, True, self.text_color(i))
                surface.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))
        else:
            pg.draw.circle(surface, MENU_COLOR, self.center, self.radius - 40)

    def inside_button(self, mouse_xy):
        return glm.length(self.center - mouse_xy) <= self.radius - 40

    def index_of_sector(self):
        dx, dy = glm.vec2(self.center - pg.mouse.get_pos())
        sector_size = int(360 / len(self.labels))
        if self.radius - 40 <= glm.length((dx, dy)) <= self.radius:
            sector = (math.degrees(math.atan2(-dy, dx) + glm.pi()) - sector_size / 2) // sector_size
            sector = len(self.labels) - 1 - sector
            sector %= len(self.labels)
            return int(sector)
        return None

    def text_color(self, index):
        if index == self.index_of_sector():
            return 255, 255, 255
        return 0, 0, 0


