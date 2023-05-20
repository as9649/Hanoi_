from constants import *
from Disk import Disk
from Tower import Tower
import random


def init(disk_list):
    return [Tower(disk_list, 1), Tower([], 2), Tower([], 3)]


def hanoi_rec(num_disks, source, target, helper, steps):
    if num_disks == 1:
        steps.append((source, target))
        return

    hanoi_rec(num_disks - 1, source, helper, target, steps)
    steps.append((source, target))
    hanoi_rec(num_disks - 1, helper, target, source, steps)


def get_disks_list():
    disks_list = []
    for i in reversed(range(1, disks + 1)):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        disks_list.append(Disk(i, (r, g, b)))
    return init(disks_list)


def solve(tower_list, steps, count):
    source = tower_list[steps[count][0] - 1]
    target = tower_list[steps[count][1] - 1]
    disk = source.remove_disk()
    target.add_disk(disk)
    set_screen(tower_list, count)


def set_screen(tower_list: list[Tower], count):
    screen.fill((255, 255, 255))
    rect = pygame.Rect(0, 468, SCREEN_WIDTH, 50)
    pygame.draw.rect(screen, (185, 122, 87), rect)

    for i in range(3):
        screen.blit(pole, (SPACE_HEIGHT + 338 + (i - 1) * 353, 118))

    for tower in tower_list:
        tower.add_tower()

    font = pygame.font.SysFont("Arial", 25)
    str1 = font.render(f"Steps:", True, (0, 0, 0))
    str2 = font.render(f"{count + 1}", True, (0, 0, 0))
    str3 = font.render(f"{disks}", True, (0, 0, 0))

    screen.blit(str1, (10, 20))
    screen.blit(str2, (70, 20))
    screen.blit(str3, (10, 40))


def main():
    pygame.init()
    pygame.display.set_caption("Hanoi Towers")

    running = True
    step_list = []
    count = 0
    global disks
    disks = 3
    global start
    start = False

    hanoi_rec(disks, 1, 3, 2, step_list)
    tower_list = get_disks_list()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                start = True

        if start:
            solve(tower_list, step_list, count)
            count += 1
            clock.tick(1)

            if count == len(step_list):
                if disks < 20:
                    count = 0
                    disks += 1
                    step_list = []
                    hanoi_rec(disks, 1, 3, 2, step_list)
                    tower_list = get_disks_list()

                    start = False
        else:
            set_screen(tower_list, -1)

        pygame.display.flip()


main()
