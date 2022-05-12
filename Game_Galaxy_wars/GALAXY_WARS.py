import pygame,sys,math,random
from pygame.locals import *

Earth = pygame.image.load("resources/images/earth-icon.png")
Space = pygame.image.load("resources/images/Space2.jpg")
Alien = pygame.image.load("resources/images/Alien1.png")
gameover = pygame.image.load("resources/images/gameover.png")
intro = pygame.image.load("resources/images/utron.png")
menu = pygame.image.load("resources/images/scr1.png")

# Nhạc
pygame.mixer.init()
hit = pygame.mixer.Sound("resources/audio/explode.wav")
enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
shoot = pygame.mixer.Sound("resources/audio/shoot.wav")
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)
pygame.mixer.music.load('resources/audio/musictheme.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)

class Game():
    highscore = 0
    def __init__(self):
        pygame.init()  # Init pygame
        pygame.display.set_caption("GALAXY WARS")
        self.width = 1100
        self.height = 600
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.keys = [False,False,False,False]
        self.x = 50
        self.y = 50
        self.acc = [0, 0]
        self.arrows = []
        self.arrow = pygame.image.load("resources/images/bullet.png")
        self.plane = pygame.image.load("resources/images/Plane5.png")
        self.badtimer = 100
        self.badtimer1 = 0
        self.badguys = [[640, 100]]
        self.healthvalue = 200
        self.badguyimg1 = pygame.image.load("resources/images/ufo2.png")
        self.badguyimg = self.badguyimg1
        self.gamerunning = True
        self.scores = 0
        # self.highscore = 0
        self.font = pygame.font.SysFont("comicsansms", 40)
        self.healthbar = pygame.image.load("resources/images/healthbar.png")
        self.health = pygame.image.load("resources/images/health.png")
        self.mx=0
        self.my=0
        self.start = pygame.image.load("resources/images/start.png")
        self.quit = pygame.image.load("resources/images/quit.png")
        self.p1 = pygame.image.load("resources/images/plane3.png")
        self.p2 = pygame.image.load("resources/images/plane5.png")
        self.p3 = pygame.image.load("resources/images/plane0.png")
        self.p11 = pygame.image.load("resources/images/plane3 - Copy.png")
        self.p21 = pygame.image.load("resources/images/plane5 - Copy.png")
        self.p31 = pygame.image.load("resources/images/plane0 - Copy.png")

    def bullet(self): # tạo ra chuyển động của đạn
        for bullet in self.arrows:
            index = 0
            velx = math.cos(bullet[0]) * 10
            vely = math.sin(bullet[0]) * 10
            bullet[1] += velx
            bullet[2] += vely
            if bullet[1] < -64 or bullet[1] > 1100 or bullet[2] < -64 or bullet[2] > 600:
                self.arrows.pop(index)
            index += 1
            for projectile in self.arrows:
                arrow1 = pygame.transform.rotate(self.arrow, 360 - projectile[0] * 57.29)
                self.screen.blit(arrow1, (projectile[1], projectile[2]))
    def check_colisson(self): # kiểm tra va chạm
        score = self.font.render('Score: {}'.format(self.scores), True, (255, 255, 255))
        self.screen.blit(score, (500, 5))
        self.badtimer -= 1
        if self.badtimer == 0:
            self.badguys.append([900, random.randint(50, 550)])
            self.badtimer = 100 - (self.badtimer1 * 2)
            if self.badtimer1 >= 10:
                self.badtimer1 = 10
            else:
                self.badtimer1 += 1
        index = 0
        for badguy in self.badguys:
            if badguy[0] < -64:
                self.badguys.pop(index)
            badguy[0] -= (1 + self.scores // 8)
            badrect = pygame.Rect(self.badguyimg.get_rect())
            badrect.top = badguy[1]
            badrect.left = badguy[0]
            if badrect.left < 64:
                hit.play()
                self.healthvalue -= 30
                self.badguys.pop(index)

            # kiểm tra va chạm giữa tàu và đạn
            index1 = 0
            # score = self.font.render(format(self.scores), True, (255, 255, 255))
            # self.screen.blit(score, (650, 5))
            for bullet in self.arrows:
                bullrect = pygame.Rect(self.arrow.get_rect())
                bullrect.left = bullet[1]
                bullrect.top = bullet[2]
                if badrect.colliderect(bullrect):
                    enemy.play()
                    self.acc[0] += 1
                    self.badguys.pop(index)
                    self.arrows.pop(index1)
                    self.scores += 1
                    # score = self.font.render(format(self.scores), True, (255, 255, 255))
                    # self.screen.blit(score, (650, 5))
                    #score_surface = self.font.render(str(int(score)), True, (255, 255, 255))
                    #score = self.font.render(str(self.scores), True, (255, 255, 255))
                    pygame.display.flip()
                index1 += 1
            index += 1
        for badguy in self.badguys:
            self.screen.blit(self.badguyimg, badguy)

    def draw(self):
        # Vẽ ảnh nền
        for x in range(int(self.width / Space.get_width()) + 1):
            for y in range(int(self.height / Space.get_height()) + 1):
                self.screen.blit(Space, (x * 550, y * 240))
        self.screen.blit(Earth, (0, 0)) # Vẽ ảnh trái đất
        self.screen.blit(Alien, (820, 10)) # Vẽ ảnh con quái to
        #Vẽ đạn
        position = pygame.mouse.get_pos()
        angle = math.atan2(position[1] - (self.y + 32), position[0] - (self.x + 26))
        playerrot = pygame.transform.rotate(self.   plane, 360 - angle * 57.29)
        playerpos1 = (self.x - playerrot.get_rect().width / 2, self.y - playerrot.get_rect().height / 2)
        self.screen.blit(playerrot, playerpos1)
        #Vẽ thanh máu
        self.screen.blit(self.healthbar, (5, 5))
        for health1 in range(self.healthvalue):
            self.screen.blit(self.health, (health1 + 8, 8))

    def menu(self):
        ok = True
        while ok:
            self.screen.blit(intro, (0, 0));
            if self.mx in range(27, 226) and self.my in range(353, 442):
                self.screen.blit(self.start,(26,351))
            if self.mx in range(27, 226) and self.my in range(465, 555):
                self.screen.blit(self.quit, (26, 463))
            pygame.display.update()
            self.mx,self.my = 0,0
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type ==pygame.MOUSEBUTTONDOWN:
                    self.mx,self.my = pygame.mouse.get_pos()
                if self.mx in range(27,226) and self.my in range(353,442):
                    ok=False
                elif self.mx in range(27, 226) and self.my in range(465, 555):
                    pygame.quit()
                pygame.display.update()
            self.mx, self.my = pygame.mouse.get_pos()

    def menu1(self):
        ok = True
        while ok:
            self.screen.blit(menu,(0,0));
            if self.mx in range(357, 412) and self.my in range(293,383):
                self.screen.blit(self.p11,(355,289))
            if self.mx in range(503,559) and self.my in range(293, 383):
                self.screen.blit(self.p21, (500,288))
            if self.mx in range(661,737) and self.my in range(293, 383):
                self.screen.blit(self.p31, (659,285))
            pygame.display.update()
            self.mx, self.my = 0, 0
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type ==pygame.MOUSEBUTTONDOWN:
                    self.mx,self.my = pygame.mouse.get_pos()
                    #print(self.mx,self.my)
                if self.mx in range(357,412) and self.my in range(293,383):
                    self.plane = pygame.image.load("resources/images/plane3.png")
                    ok = False
                elif self.mx in range(503,559) and self.my in range(293,383):
                    self.plane = pygame.image.load("resources/images/plane5.png")
                    ok = False
                elif self.mx in range(661,737) and self.my in range(293,383):
                    self.plane = pygame.image.load("resources/images/plane0.png")
                    ok = False
                pygame.display.update()
            self.mx, self.my = pygame.mouse.get_pos()

    def run(self):
        self.menu()
        self.menu1()
        while self.gamerunning:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    # shoot.play()
                    if event.key == K_w:
                        self.keys[0] = True
                    elif event.key == K_a:
                        self.keys[1] = True
                    elif event.key == K_s:
                        self.keys[2] = True
                    elif event.key == K_d:
                        self.keys[3] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.keys[0] = False
                    elif event.key == pygame.K_a:
                        self.keys[1] = False
                    elif event.key == pygame.K_s:
                        self.keys[2] = False
                    elif event.key == pygame.K_d:
                        self.keys[3] = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    shoot.play()
                    position = pygame.mouse.get_pos()
                    angle = math.atan2(position[1] - (self.y + 32), position[0] - (self.x + 26))
                    playerrot = pygame.transform.rotate(self.plane, 360 - angle * 57.29)
                    playerpos1 = (self.x - playerrot.get_rect().width / 2, self.y - playerrot.get_rect().height / 2)
                    self.acc[1] += 1
                    self.arrows.append([math.atan2(position[1] - (playerpos1[1] + 32), position[0] - (playerpos1[0] + 26)),
                                   playerpos1[0]+ 32, playerpos1[1]+ 32])

                if self.keys[0]:
                    self.y -= 10
                if self.keys[1]:
                    self.x -= 10
                if self.keys[2]:
                    self.y += 10
                if self.keys[3]:
                    self.x += 10
                if self.x + 50 > 1100:
                    self.x = 1050
                if self.x < 0:
                    self.x = 0
                if self.y + 50 > 600:
                    self.y = 550
                if self.y < 0:
                    self.y = 0

            if self.healthvalue<0:  # Nếu hết máu
                newGame = False
                while (True):
                    for event in pygame.event.get():  # Nếu nhấn
                        if event.type == pygame.QUIT:  # Thoát
                            self.gamerunning = False
                            newGame = True
                            break
                        if event.type == pygame.KEYDOWN:  # Thoát
                            newGame = True
                            break
                    if (newGame == True):  # Thoát vòng while để vào game mới
                        break
                    # in diem
                    pygame.font.init()
                    self.screen.blit(gameover, (0, 0))
                    score = self.font.render('Score: {}'.format(self.scores), True, (255, 255, 255))
                    if (self.highscore<self.scores):
                        self.highscore = self.scores
                    hscore = self.font.render('HighScore: {}'.format(self.highscore), True, (255, 255, 255))
                    playagain = self.font.render('Press to any key to play again!!'.format(self.highscore), True, (255, 255, 255))
                    self.screen.blit(score, (450, 320))
                    self.screen.blit(hscore, (408, 380))
                    self.screen.blit(playagain, (280, 450))
                    pygame.display.update()
                    self.draw()
                self.__init__()
                self.menu1()
            self.draw()
            # Draw arrows
            self.bullet()
            # Draw Enemy
            self.check_colisson()
            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()

