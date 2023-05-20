import pygame

# screen
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 1060
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

# pole
pole = pygame.image.load("images\\pole.png")
pole = pygame.transform.scale(pole, (32, 350))

# disk
DISKS = 3
DISK_WIDTH = 80
DISK_HEIGHT = 25
disk = pygame.image.load("images\\disk.png")
disk = pygame.transform.scale(disk, (156.25, 70))


SPACE_HEIGHT = 180
SPACE_WIDTH = 455
clock = pygame.time.Clock()
