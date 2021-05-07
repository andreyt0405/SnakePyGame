import threading
from snake_bounder import snake_bounder
from count_down import count_down
from snakepy import snakepy
from coins import coins
from score import score
from intro_menu import  intro_menu
import pygame
import logging

class init_game:
  def __init__(self,mode,name,level='1',point=0,sound=None):
      self.__stop = False
      self.__name = name
      self.__sound=sound
      self.__level = level
      self.__mode = mode
      self.__game_over = False
      self.__state = True
      pygame.display.set_caption('SnakePy By AndreyT')
      self.__sb_image = ['arrows.png','pause.png']
      self.__soundList = ['snake_eat2.mp3','victory.mp3','lose.mp3']
      self.__backgroud = {'1':'grass.png','2':'grass2.png','3':'grass3.png'}
      self.__dis = pygame.display.set_mode((600, 405))
      self.__score = score(self.__dis, point)
      self.__coin = coins(self.__dis)
      self.__snake = snakepy(self.__dis,self.__level,self.__mode)
      self.__snake_bondrs = snake_bounder(self.__dis,self.__level,self.__mode)
      self.__clock = pygame.time.Clock()
      self.__count_down = count_down(self.__dis, self.__backgroud.get(self.__level))
      self. __start_game()

  def __start_game(self):
    game_close = False
    f_count = 1
    threading.Thread(target=self.__snake_in_bounder).start()
    gamebackground = pygame.image.load(self.__backgroud.get(self.__level))
    sub_icon = pygame.image.load((self.__sb_image[0]))
    sub_icon1 = pygame.image.load((self.__sb_image[1]))
    threading.Thread(target=self.__check_coin).start()
    while not game_close:
        while self.__game_over:
            self.__sound_play("lose")
            intro_menu('GameOver',self.__name,self.__mode[0],self.__score.get_score())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:game_close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.__state == True:
                        self.__state = False
                    else:self.__state = True
                if self.__state != False:
                 if event.key == pygame.K_LEFT:self.__snake.move_left()
                 elif event.key == pygame.K_RIGHT:self.__snake.move_right()
                 elif event.key == pygame.K_UP:self.__snake.move_up()
                 elif event.key == pygame.K_DOWN:self.__snake.move_down()
                 if f_count == 1:self.__count_down.start_count_down()
                 f_count = 0
        if game_close != True: self.__game_over = self.__snake.check_bounders()
        if self.__state != False:self.__snake.update_points()
        if self.__state != False:
         self.__dis.blit(gamebackground, (0, 0))
         self.__dis.blit(sub_icon, (500, 300))
        else: self.__dis.blit(sub_icon1, (175, 75))
        if self.__game_over != True:
            if self.__state != False:self.__game_over = self.__snake.snake_tail()
        self.__snake.draw_object()
        self.__coin.draw_object()
        self.__snake_bondrs.draw_object()
        self.__score.revoke_score("update",self.__level,self.__mode[0])
        if self.__score.get_prevScore() + 10 == self.__score.get_score():
           self.__score.update_prevScore()
           self.__snake.speed_inc()
        if self.__score.get_score() == 15 and self.__level == '1':
           self.__sound_play("victory")
           self.__del__()
           init_game(self.__mode,self.__name,'2',self.__score.get_score(),sound=self.__sound)
        elif self.__score.get_score() == 35 and self.__level == '2':
             self.__sound_play("victory")
             self.__del__()
             init_game(self.__mode,self.__name,'3',self.__score.get_score(),sound=self.__sound)
        pygame.display.update()

        self.__clock.tick(self.__snake.snake_speed())
    pygame.quit()
    quit()

  def __check_coin(self):
      while not self.__game_over:
          if self.__snake.get_x() == self.__coin.get_objectx() and self.__snake.get_y() == self.__coin.get_objecty():
               self.__sound_play("crunch")
               self.__coin.rand_place()
               self.__snake.snake_len()
               self.__score.score_inc()


  def __sound_play(self,sound):
    if self.__sound == 1:
     if sound == "crunch": pygame.mixer.music.load(self.__soundList[0])
     elif sound == "victory":  pygame.mixer.music.load(self.__soundList[1])
     elif sound == "lose": pygame.mixer.music.load(self.__soundList[2])
     pygame.mixer.music.play()


  def __snake_in_bounder(self):
      x_right = self.__snake_bondrs.get_params_list(self.__level[0])[0]
      y_down =self.__snake_bondrs.get_params_list(self.__level[0])[1]
      x_left = self.__snake_bondrs.get_params_list(self.__level[0])[2]
      y_up = self.__snake_bondrs.get_params_list(self.__level[0])[3]
      while not self.__game_over:
          self.__clock.tick(self.__snake_bondrs.snake_speed()-5)
          if self.__snake_bondrs.get_y() <= x_right:
              self.__snake_bondrs.move_right()
          if self.__snake_bondrs.get_x()>=y_down:
            self.__snake_bondrs.move_down()
          if self.__snake_bondrs.get_y()>=x_left:
              self.__snake_bondrs.move_left()
          if self.__snake_bondrs.get_x()<y_up and self.__snake_bondrs.get_y() != y_up:
              self.__snake_bondrs.move_up()
          if self.__state != False: self.__snake_bondrs.update_points()
          if self.__state != False and not self.__game_over:self.__snake_bondrs.snake_tail()
          if not self.__game_over:
              self.__game_over=self.__snake_bondrs.check_collusion(self.__snake.get_snake_pos())

  def __del__(self):
      logging.info("class object deleted")
      del self