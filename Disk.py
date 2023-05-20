from constants import *


class Disk:
    def __init__(self, size: int, color: tuple):
        self.size = size
        self.color = color

    def draw_disk(self, x_pos: int, y_pos: int):
        square = pygame.Rect(0, 0, self.size*35, DISK_HEIGHT)
        square.center = (SPACE_HEIGHT + (x_pos - 1) * 353, SPACE_WIDTH - y_pos * 25)
        pygame.draw.rect(screen, self.color, square)
