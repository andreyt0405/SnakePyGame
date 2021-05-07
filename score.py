import pygame

class score:
    def __init__(self,dis, point):
        self.__prevScore=0
        self.__dis = dis
        self.__color = (255,255,255)
        self.__score_font_init = pygame.font.SysFont("impact.ttf", 25)
        self.__score_font_over = pygame.font.SysFont("arial.ttf", 40)
        self.__score_font_message = pygame.font.SysFont("arial.ttf", 25)
        self.__score = point

    def revoke_score(self,section,level,mode):
        if section != "game_over":
         pygame.draw.rect(self.__dis,(255,178,102),[0,0,600,20])
         self.__dis.blit(self.__score_font_init .render("Score {}".format(str(self.__score)), True,(0,0,0)), (5, 2))
         self.__dis.blit(self.__score_font_init.render("Level {}".format(str(level)), True, self.__color), (95, 2))
         self.__dis.blit(self.__score_font_init .render("Mode {}".format(str(mode)), True, self.__color), (185, 2))
        else:
         self.__dis.blit(self.__score_font_over.render("Score : {}".format(str(self.__score)), True, self.__color),(0, 250))

    def score_inc(self):
        self.__score+=1

    def get_prevScore(self):
        return self.__prevScore

    def get_score(self):
        return self.__score

    def update_prevScore(self):
        self.__prevScore = self.__score




