
import pygame
import pyodbc

class leadboard:
  def __init__(self,section,name,mode,score=None,callback=None):
      pygame.init()
      self.__name = name
      self.__mode = mode
      self.__callback = callback
      self.__conn_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Andrey\PycharmProjects\SnakePy\leadscore.accdb;'
      self.__connection = pyodbc.connect(self.__conn_string)
      self.__section = section
      self.__score = score
      self.__score_dict = []
      self.__name_dict = []
      self.__mode_dict = []
      self.__surface = pygame.display.set_mode((550, 550))
      self.__white = (255, 255, 255)
      self.__green = (188, 210, 159)
      self.__back_image = pygame.image.load('back.png','PNG')
      self.__caption_image = pygame.image.load('start_play.png','PNG')
      self.__font = pygame.font.Font(None, 40)


  def __insert(self):
      cursor =  self.__connection.cursor()
      cursor.execute('''INSERT INTO Score (Name,Score,Mode)VALUES('{}','{}','{}')'''.format(self.__name,self.__score,self.__mode))
      self.__connection.commit()

  def __select(self):
          cursor = self.__connection.cursor()
          cursor.execute('SELECT DISTINCT Name,Score,Mode FROM Score ORDER BY Score DESC')
          [(self.__score_dict.append(row[1]),self.__name_dict.append(row[0]),self.__mode_dict.append(row[2])) for row in cursor.fetchall()]

  def __blit_text(self, pos):
      unistr = "[<-- BackSpace ]"
      word_surface = self.__font.render('** Score Board **', 1, (206, 45, 61))
      word_surface1 = self.__font.render('____________', 1, (206, 45, 61))
      self.__surface.blit(word_surface,(150,50))
      self.__surface.blit(word_surface1, (170,55))
      unistr = self.__font.render(unistr, True, self.__white)
      self.__surface.blit(unistr, [150, 450])
      x, y = pos
      if not self.__score_dict:
          self.__surface.blit(self.__caption_image, (75, 30))
      else:
       for score,name,mode,in zip(self.__score_dict,self.__name_dict,self.__mode_dict):
              word_surface = self.__font.render('[Score:{}] | [Player:{}] | {}'.format(score,name,mode),1,(27,159,199))
              self.__surface.blit(word_surface, (x, y))
              x = pos[0]
              y += 50


  def leadBoard_load(self):
      self.__surface = pygame.display.set_mode((550, 550))
      while True:
          self.__surface.fill(self.__green)
          self.__surface.blit(self.__back_image, (30, 30))
          self.__blit_text((30, 100))
          for event in pygame.event.get():
              if event.type == pygame.QUIT:pygame.quit(),quit()
              if event.type == pygame.MOUSEBUTTONUP:
                  pos = pygame.mouse.get_pos()
                  self.__back_to_menu(pos,'Mouse')
              if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_BACKSPACE:
                     self.__back_to_menu(key='K_BACKSPACE')
              pygame.display.update()

  def __back_to_menu(self,pos=None, key=None):
    from intro_menu import intro_menu
    if (key == 'Mouse' and pos[0] >= 30 and pos[0] <= 70 and pos[1]>= 40 and pos[1]<=60) or key == 'K_BACKSPACE':
          if  self.__section == 'Main':intro_menu('Main',self.__name)
          else:intro_menu("GameOver",self.__name,self.__mode,self.__score,callback=True)

  def check_rows_db(self):
      cursor = self.__connection.cursor()
      cursor.execute('SELECT DISTINCT Name,Score FROM Score')
      [self.__score_dict.append(row[1]) for row in cursor.fetchall()]
      if len(self.__score_dict)>5:
         cursor.execute('DELETE FROM Score WHERE Score = ( SELECT Min( Score ) FROM Score )')
         self.__connection.commit()
      if self.__section != 'Main' and self.__callback != True:
          self.__insert()
      self.__select()
