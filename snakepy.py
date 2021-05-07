import threading
import pygame

class snakepy(object):
    def __init__(self,dis,level,mode):
        self.__snake_Head = []
        self.__snake_List = []
        self.__length_of_snake = 1
        self.__snake_speed = self.__set_snake_speed(level,mode)
        self.__x1 = 300
        self.__y1 = 300
        self.__x1_change = 0
        self.__y1_change = 0
        self.__snake_block = 15
        self._display=dis
        self.__color=(95,158,160)

    def move_up(self):
        self.__y1_change = -self.__snake_block
        self.__x1_change = 0


    def move_down(self):
        self.__y1_change = self.__snake_block
        self.__x1_change = 0


    def move_left(self):
        self.__x1_change = -self.__snake_block
        self.__y1_change = 0


    def move_right(self):
        self.__x1_change = self.__snake_block
        self.__y1_change = 0

    def snake_tail(self):
        self.__snake_Head = []
        self.__snake_Head.append(self.__x1)
        self.__snake_Head.append(self.__y1)
        self.__snake_List.append(self.__snake_Head)
        if len(self.__snake_List) > self.__length_of_snake:
            del self.__snake_List[0]
            return next((x for x in self.__snake_List[:-1] if x == self.__snake_Head), None)

    def update_points(self):
        self.__x1 += self.__x1_change
        self.__y1 += self.__y1_change

    def check_bounders(self):
        if self.__x1 >= 600 \
                or self.__x1 < 15 or self.__y1 >= 405 or self.__y1 <= 15:
            return True

    def get_x(self):
        return self.__x1

    def get_y(self):
        return  self.__y1

    def snake_speed(self):
        return self.__snake_speed

    def draw_object(self):
        [(pygame.draw.circle(self._display, self.__color, [x[0], x[1]], 10, 10),
          pygame.draw.circle(self._display, (0, 0, 0), [x[0], x[1]], 10, 2),
          pygame.draw.circle(self._display, (255, 255, 255), [x[0], x[1]], 5, 5)) for x in self.__snake_List]

    def snake_len(self):
         if len(self.__snake_List) < 40:
          self.__length_of_snake+=1

    def speed_inc(self):
         self.__snake_speed += 5

    def __set_snake_speed(self,level,mode):
         if mode[0] == "Easy":
             if level == '1':
                 return 15
             elif level == '2':
                 return 20
             else: return 30

         elif mode[0] == "Hard":
             if level == '1': return 20
             elif level == '2': return 25
             else:return 30
         else:
             return 30

    def get_snake_pos(self):
        return self.__snake_List
