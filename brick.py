import pygame

from GameObject import GameObject


#Дочерний класс (подкласс) суперкласса GameObject
class Brick(GameObject):
    def __init__(self, x, y, w, h, color, special_effect=None):
        GameObject.__init__(self, x, y, w, h)
        self.color = color
        self.special_effect = special_effect


    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)