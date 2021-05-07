
import pygame
import random

class coins:
    def __init__(self,dis):
        self.__display = dis
        self.__color=(229,0,0)
        self.rand_place()
        self.__furitImage = pygame.image.load("fruit.png")

    def draw_object(self):
        self.__display.blit(self.__furitImage, (self.__coinx-25, self.__coiny-25))

    def get_objectx(self):
        return self.__coinx

    def get_objecty(self):
        return self.__coiny

    def rand_place(self):
        self.__coinx = round(random.randrange(30, 600 - 30) / 15.0) * 15.0
        self.__coiny = round(random.randrange(45, 405 - 45) / 15.0) * 15.0
