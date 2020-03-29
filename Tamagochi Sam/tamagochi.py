import pygame
import threading

pygame.init()

#CARGA LA VENTANA
win = pygame.display.set_mode((500,480))
pygame.display.set_caption("Tamagochi de Sam")

#CARGA LAS IMAGENES
walkRight = pygame.image.load('der.png')
walkLeft = pygame.image.load('izq.png')
bg = pygame.image.load('bg.png')
char = pygame.image.load('parado.png')

clock = pygame.time.Clock()

#CREO MIS CLASES
class barra():
    def __init__(self,color,x,y,fondo,width,height):
        self.color = color
        self.x = x
        self.y = y
        self.fondo = fondo
        self.width = width
        self.height = height

    def draw(self,win):
        pygame.draw.rect(win, (108,108,108), (self.x, self.y, self.width, self.fondo))
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 15
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft, (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight, (self.x,self.y))
            self.walkCount +=1
        else:
            win.blit(char, (self.x,self.y))
class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 25)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y - 20))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True


def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    boton_hambre.draw(win,(0,0,0))
    barra_hambre.draw(win)


    pygame.display.update()


#mainloop
man = player(200, 327, 150,150)
run = True

boton_hambre = button((255,0,132),430,50,30,30,"Alimentar")


barra_hambre = barra((255,172,0),20,20,100,30,100)

while run:
    clock.tick(27)

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if boton_hambre.isOver(pos):
                print("click!")



    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
    else:
        man.right = False
        man.left = False
        man.walkCount = 0

    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()
