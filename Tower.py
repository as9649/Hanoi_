from Disk import *


class Tower:

    disks: list[Disk]

    def __init__(self, disks, x_pos):
        self.disks = disks
        self.x_pos = x_pos

    def add_disk(self, disk: Disk):
        self.disks.append(disk)

    def remove_disk(self):
        return self.disks.pop()

    def get_num_of_disks(self):
        return len(self.disks)

    def add_tower(self):
        for i, disk in enumerate(self.disks):
            disk.draw_disk(self.x_pos, i)
