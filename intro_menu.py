import pygame
from leadboard import leadboard
from pygame_menu import *

class intro_menu:
    def __init__(self,section,name,mode='Easy',score=None,callback=False):
        pygame.init()
        self.__sound = 1
        self.__name=name
        self.__mode=mode
        self.__score=score
        surface = pygame.display.set_mode((550, 550))
        self.__menu = pygame_menu.Menu(550, 550, self.__set_title(section), theme=pygame_menu.themes.THEME_GREEN)
        pygame.display.set_caption('SnakePy By AndreyT')
        if section != 'Main':  self.__menu.add_label("Score: {}".format(str(score)))
        self.__return_section(section)
        if section == 'Main':self.__menu.add_text_input("Name: ",onchange=self.__set_name)
        self.leadnb = leadboard(section,self.__name,self.__mode,score,callback)
        if section == 'GameOver' or section == 'Main': self.leadnb.check_rows_db()
        self.__mode = self.__menu.add_selector('Difficulty :', [('Easy', 1), ('Hard', 2), ('Insane', 3)])
        self.__menu.add_selector('Sound :', [('On', 1), ('Off', 0)],onchange=self.__get_sound)
        self.__menu.add_button('Score Board', lambda:self.leadnb.leadBoard_load())
        if section == 'Main':self.__menu.add_image('snake_main.png', 0, 'main',).set_margin(170, 0)
        self.__menu.mainloop(surface)


    # def start_menu(self):
    #     from init_game import init_game
    #     surface = pygame.display.set_mode((550, 550))
    #     self.__menu = pygame_menu.Menu(550, 550, 'SnakePy By AndreyT', theme=pygame_menu.themes.THEME_GREEN)
    #     pygame.display.set_caption('SnakePy By AndreyT')
    #     self.__menu.add_button('Play', lambda:init_game(self.__mode.get_value(), self.__name, sound=self.__sound))
    #     self.__menu.add_text_input("Name: ", onchange=self.__set_name)
    #     self.__mode = self.__menu.add_selector('Difficulty :', [('Easy', 1), ('Hard', 2), ('Insane', 3)])
    #     self.__menu.add_selector('Sound :', [('On', 1), ('Off', 0)],onchange=self.__get_sound)
    #     self.__menu.add_image('snake_main.png', 0, 'main', ).set_margin(170, 0)
    #
    # def game_over_menu(self):
    #     from init_game import init_game
    #     surface = pygame.display.set_mode((550, 550))
    #     self.__menu = pygame_menu.Menu(550, 550, 'SnakePy By AndreyT',theme=pygame_menu.themes.THEME_GREEN)
    #     pygame.display.set_caption('GAME OVER LOSSSER')
    #     self.__menu.add_label("Score: {}".format(str(self.__score)))
    #     self.__menu.add_button('Play Again',lambda: init_game(self.__mode.get_value(), self.__name, sound=self.__sound))
    #     self.__mode = self.__menu.add_selector('Difficulty :', [('Easy', 1), ('Hard', 2), ('Insane', 3)])
    #     self.__menu.add_selector('Sound :', [('On', 1), ('Off', 0)], onchange=self.__get_sound)

    def __return_section(self,section):
        from init_game import init_game
        if section == 'Main':
            self.__menu.add_button('Play', lambda:init_game(self.__mode.get_value(),self.__name,sound=self.__sound))
        else:
            self.__menu.add_button('Play Again', lambda:init_game(self.__mode.get_value(),self.__name,sound=self.__sound))

    def __set_title(self,section):
        return 'SnakePy By AndreyT' if section =='Main' else 'GAME OVER LOSSSER'

    def __get_sound(self,selector,value):
        self.__sound = value

    def __set_name(self,value):
        self.__name = value