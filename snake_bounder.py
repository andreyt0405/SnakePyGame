import pygame

from snakepy import snakepy
class snake_bounder(snakepy):
    def __init__(self,dis,level,mode):
        super(snake_bounder, self).__init__(dis,level,mode)
        self.__parms={'1':[(30,575,390,30),5],
                      '2':[(60,540,360,60),10],
                      '3':[(105,480,285,105),15]}
        self.__x1 = self.__parms.get(level)[0][0]
        self.__y1 = self.__parms.get(level)[0][0]
        self.__list_bounder = self.get_params_list(level)
        self.__snake_len = self.__parms.get(level)[1]
        self.__x1_change = 0
        self.__y1_change = 0
        self.__snake_List = []
        self.__snake_Head = []
        self.__color=(113,46,181)

    def draw_object(self):
        [(pygame.draw.circle(self._display, self.__color, [x[0], x[1]], 10, 10),
          pygame.draw.circle(self._display, (0, 0, 0), [x[0], x[1]], 10, 2),
          pygame.draw.circle(self._display, (16,116,154), [x[0], x[1]], 5, 5)) for x in self.__snake_List]

    def move_up(self):
        self.__y1_change = -15
        self.__x1_change = 0

    def move_down(self):
        self.__y1_change = 15
        self.__x1_change = 0

    def move_left(self):
        self.__x1_change = -15
        self.__y1_change = 0

    def move_right(self):
        self.__x1_change = 15
        self.__y1_change = 0

    def update_points(self):
        self.__x1 += self.__x1_change
        self.__y1 += self.__y1_change


    def get_x(self):
        return self.__x1

    def get_y(self):
        return self.__y1

    def snake_tail(self):
        self.__snake_Head = []
        self.__snake_Head.append(self.__x1)
        self.__snake_Head.append(self.__y1)
        self.__snake_List.append(self.__snake_Head)
        if len(self.__snake_List) > self.__snake_len:
            del self.__snake_List[0]

    def get_params_list(self,dif):
        return self.__parms.get(dif)[0]

    def check_collusion(self,plist):
        return next((x for x in plist for y in
                self.__snake_List if x[0] == y[0] and x[1] == y[1]), None)








