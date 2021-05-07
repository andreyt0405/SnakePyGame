import time
import pygame
import random

class count_down:
  def __init__(self,screen,backgroud):
      self.__counter, self.__text = 3, '3'.rjust(3)
      self.__screen=screen
      self.__color = 0
      self.__backgroud = backgroud
      pygame.time.set_timer(pygame.USEREVENT, 1000)
      self.__font = pygame.font.SysFont('impact', 75)
      self.__font2 = pygame.font.SysFont('impact', 40)
      self.__clock = pygame.time.Clock()

  def start_count_down(self):
      while self.__counter != 0:
          for e in pygame.event.get():
              if e.type == pygame.USEREVENT:
                  self.__color = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
                  self.__counter -= 1
                  self.__text = str(self.__counter).rjust(3) if self.__counter > 0 else 'GO!!'
              if e.type == pygame.QUIT:pygame.quit(),quit()
          else:
              self.__screen.blit(pygame.image.load(self.__backgroud), (0, 0))
              self.__screen.blit(self.__font.render(self.__text, True, (self.__color)), (250,150))
              self.__screen.blit(self.__font2.render(self.__text, True, (255,255,255)), (265,165))
              pygame.display.update()
              self.__clock.tick(60)
              continue

      time.sleep(1)