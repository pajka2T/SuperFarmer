import pygame as py
import math


class ImageGrid:
    def __init__(self, x, y, image, width, height):
        #print("UUU")
        self.image = py.transform.scale(image, (width, height))
        self.rect = image.get_rect()  # copy the image dimensions
        self.rect.x = x
        self.rect.y = y                 # move to location
    def draw( self, window ):
        #print("HALO")
        window.blit(self.image, self.rect)    # paint it
def drawcircles(window, color1, color2, color3, x, x2, y, animal, size, animalnumber, player):
    py.draw.circle(window, color3, (x + CELL_SIZE / 1.8, y + CELL_SIZE / 1.8), CELL_SIZE / 2.4)
    py.draw.circle(window, color2, (x2 + CELL_SIZE + CELL_SIZE / 2, y + CELL_SIZE / 1.7), CELL_SIZE / 2.4)
    py.draw.circle(WINDOW, color1, (x2 + CELL_SIZE + CELL_SIZE / 1.8, y + CELL_SIZE / 2.4), CELL_SIZE / 2.4)
    #print(y, " ", y+(CELL_SIZE/1.7)*2)
    ImageGrid(x2 + CELL_SIZE + CELL_SIZE / 1.8 + CELL_SIZE / 12 - CELL_SIZE / 2.4, y + CELL_SIZE / 2.4 + CELL_SIZE / 12 - CELL_SIZE / 2.4, animal, CELL_SIZE * size, CELL_SIZE * size).draw(WINDOW)
    animalBoardCoordinates[player][animalnumber].append((x2 + CELL_SIZE + CELL_SIZE / 2 - CELL_SIZE / 2.4, y))
    print(animalBoardCoordinates[player][animalnumber][5-animalnumber])

#players = int(input("Gracze"))
players = 2
animalBoardCoordinates = [[[] for j in range(5)] for k in range(players)]

py.init()

#WINDOW = py.display.set_mode((0, 0), py.FULLSCREEN)
WINDOW = py.display.set_mode((1500, 800))
py.display.set_caption("SuperFarmer")
logo2 = py.image.load('Images/Logo2.png').convert_alpha()
#py.display.set_icon(logo2)

screeninfo = py.display.Info()
SCREENWIDTH = screeninfo.current_w
SCREENHEIGHT = screeninfo.current_h
print(SCREENWIDTH, SCREENHEIGHT)

CELL_SIZE = math.floor(SCREENHEIGHT/8)

#BOARD_MARGIN_TOP = SCREENHEIGHT/2 - CELL_SIZE*2
BOARD_MARGIN_TOP = SCREENHEIGHT/2 - CELL_SIZE*2.5
BUNNY_MARGIN_SIDE = SCREENWIDTH/2 - CELL_SIZE*7
BETWEEN_CELLS = 7
#BUNNY_MARGIN_SIDE_TWO = BUNNY_MARGIN_SIDE + CELL_SIZE*6 + BETWEEN_CELLS*8
BUNNY_MARGIN_SIDE_TWO = SCREENWIDTH - BUNNY_MARGIN_SIDE - CELL_SIZE*6 - BETWEEN_CELLS*6

DOFORA = BETWEEN_CELLS+CELL_SIZE
DOFORA2 = BETWEEN_CELLS+CELL_SIZE/2

#ImageGrid(SCREENWIDTH/2-200, 30, logo, 400, 125).draw(WINDOW)

bunny = py.image.load('Images/bunny.png').convert_alpha()
py.display.set_icon(bunny)
bunny.set_alpha(128)
sheep = py.image.load('Images/sheep.png').convert_alpha()
sheep.set_alpha(128)
pig = py.image.load('Images/pig.png').convert_alpha()
pig.set_alpha(128)
cow = py.image.load('Images/cow.png').convert_alpha()
cow.set_alpha(128)
horse = py.image.load('Images/horse.png').convert_alpha()
horse.set_alpha(128)
#for i in range(5):
#    ImageGrid(BUNNY_MARGIN_SIDE, BOARD_MARGIN_TOP+i*10+i*CELL_SIZE, bunny, CELL_SIZE, CELL_SIZE).draw(WINDOW)

BLU = (52, 229, 235)
BLU2 = (93, 190, 194)
BLU3 = (38, 125, 128)

# Player one
for i in range(5):
    if i == 1:
        bunny.set_alpha(255)
        sheep.set_alpha(255)
        pig.set_alpha(255)
        cow.set_alpha(255)

    #ImageGrid(BUNNY_MARGIN_SIDE+DOFORA*i, BOARD_MARGIN_TOP, bunny, CELL_SIZE, CELL_SIZE).draw(WINDOW) #Rabbits
    py.draw.circle(WINDOW, BLU, (BUNNY_MARGIN_SIDE+CELL_SIZE/2*(i+1)+DOFORA2*i, BOARD_MARGIN_TOP+CELL_SIZE/2), CELL_SIZE/2)
    ImageGrid(BUNNY_MARGIN_SIDE+DOFORA*i+CELL_SIZE/10, BOARD_MARGIN_TOP+CELL_SIZE/10, bunny, CELL_SIZE*4/5, CELL_SIZE*4/5).draw(WINDOW)
    animalBoardCoordinates[0][0].append((BUNNY_MARGIN_SIDE+CELL_SIZE/2*(i+1)+DOFORA2*i, BOARD_MARGIN_TOP+CELL_SIZE/2))
    #print(animalBoardCoordinates[0][0][i])
    if i < 4: # Sheeps
        py.draw.circle(WINDOW, BLU,
                       (BUNNY_MARGIN_SIDE + CELL_SIZE + DOFORA * i, BOARD_MARGIN_TOP + CELL_SIZE*1.5+BETWEEN_CELLS/2),
                       CELL_SIZE / 2)
        ImageGrid(BUNNY_MARGIN_SIDE+CELL_SIZE/2+DOFORA*i+CELL_SIZE/10, BOARD_MARGIN_TOP+BETWEEN_CELLS/2+CELL_SIZE+CELL_SIZE/10, sheep, CELL_SIZE*4/5, CELL_SIZE*4/5).draw(WINDOW)
        animalBoardCoordinates[0][1].append((BUNNY_MARGIN_SIDE + CELL_SIZE + DOFORA * i, BOARD_MARGIN_TOP + CELL_SIZE+CELL_SIZE/2+BETWEEN_CELLS/2))
    if i < 3: # Pigs
        py.draw.circle(WINDOW, BLU, (BUNNY_MARGIN_SIDE+DOFORA+CELL_SIZE/2*(i+1)+DOFORA2*i, BOARD_MARGIN_TOP+CELL_SIZE*2.5+BETWEEN_CELLS), CELL_SIZE/2)
        ImageGrid(BUNNY_MARGIN_SIDE+CELL_SIZE+BETWEEN_CELLS+DOFORA*i+CELL_SIZE/8, BOARD_MARGIN_TOP+BETWEEN_CELLS+CELL_SIZE*2+CELL_SIZE/12, pig, CELL_SIZE*3/4, CELL_SIZE*3/4).draw(WINDOW)
        animalBoardCoordinates[0][2].append((BUNNY_MARGIN_SIDE+DOFORA+CELL_SIZE/2*(i+1)+DOFORA2*i, BOARD_MARGIN_TOP+CELL_SIZE*2.5+BETWEEN_CELLS))
    if i < 2: # Cows
        py.draw.circle(WINDOW, BLU, (BUNNY_MARGIN_SIDE + CELL_SIZE*2 + BETWEEN_CELLS + DOFORA * i, BOARD_MARGIN_TOP + CELL_SIZE*3.5+BETWEEN_CELLS*1.5), CELL_SIZE/2)
        ImageGrid(BUNNY_MARGIN_SIDE+CELL_SIZE*1.5+BETWEEN_CELLS*1.2+DOFORA*i+CELL_SIZE/10, BOARD_MARGIN_TOP+BETWEEN_CELLS*1.5+CELL_SIZE*3+CELL_SIZE/10, cow, CELL_SIZE*4/5, CELL_SIZE*4/5).draw(WINDOW)
        animalBoardCoordinates[0][3].append((BUNNY_MARGIN_SIDE + CELL_SIZE*2 + BETWEEN_CELLS + DOFORA * i, BOARD_MARGIN_TOP + CELL_SIZE*3.5+BETWEEN_CELLS*1.5))
py.draw.circle(WINDOW, BLU, (BUNNY_MARGIN_SIDE+DOFORA*2+CELL_SIZE/2, BOARD_MARGIN_TOP+CELL_SIZE*4.5+BETWEEN_CELLS*2), CELL_SIZE/2)
ImageGrid(BUNNY_MARGIN_SIDE+CELL_SIZE*2+BETWEEN_CELLS*2+CELL_SIZE/10, BOARD_MARGIN_TOP+BETWEEN_CELLS*2+CELL_SIZE*4+CELL_SIZE/10, horse, CELL_SIZE*3/4, CELL_SIZE*3/4).draw(WINDOW)
animalBoardCoordinates[0][4].append((BUNNY_MARGIN_SIDE+DOFORA*2+CELL_SIZE/2, BOARD_MARGIN_TOP+CELL_SIZE*4.5+BETWEEN_CELLS*2))
horse.set_alpha(255)

# Additional animals
font = py.font.Font('C:\Windows\Fonts\BRLNSDB.TTF', 32)
text = "+3"
black = (0, 0, 0)
white = (255, 255, 255)
textSurface = font.render(text, True, white)

drawcircles(WINDOW, BLU, BLU2, BLU3, BUNNY_MARGIN_SIDE+DOFORA*5, BUNNY_MARGIN_SIDE+DOFORA*4, BOARD_MARGIN_TOP, bunny, 2/3, 0, 0)
drawcircles(WINDOW, BLU, BLU2, BLU3, BUNNY_MARGIN_SIDE+DOFORA*4+CELL_SIZE/2, BUNNY_MARGIN_SIDE+DOFORA*3+CELL_SIZE/2, BOARD_MARGIN_TOP+CELL_SIZE+BETWEEN_CELLS/2, sheep, 2/3, 1, 0)
drawcircles(WINDOW, BLU, BLU2, BLU3, BUNNY_MARGIN_SIDE+DOFORA*4, BUNNY_MARGIN_SIDE+DOFORA*3, BOARD_MARGIN_TOP+CELL_SIZE*2+BETWEEN_CELLS, pig, 7/12, 2, 0)
drawcircles(WINDOW, BLU, BLU2, BLU3, BUNNY_MARGIN_SIDE+DOFORA*3+CELL_SIZE/2, BUNNY_MARGIN_SIDE+DOFORA*2+CELL_SIZE/2, BOARD_MARGIN_TOP+CELL_SIZE*3+BETWEEN_CELLS*1.5, cow, 2/3, 3, 0)
drawcircles(WINDOW, BLU, BLU2, BLU3, BUNNY_MARGIN_SIDE+DOFORA*3, BUNNY_MARGIN_SIDE+DOFORA*2, BOARD_MARGIN_TOP+CELL_SIZE*4+BETWEEN_CELLS*2, horse, 7/12, 4, 0)
#ImageGrid(BUNNY_MARGIN_SIDE+CELL_SIZE+BETWEEN_CELLS+DOFORA*3, BOARD_MARGIN_TOP+BETWEEN_CELLS*2+CELL_SIZE*2, pig, CELL_SIZE, CELL_SIZE).draw(WINDOW)
#ImageGrid(BUNNY_MARGIN_SIDE+CELL_SIZE+BETWEEN_CELLS+CELL_SIZE/2+DOFORA*2, BOARD_MARGIN_TOP+BETWEEN_CELLS*3+CELL_SIZE*3, cow, CELL_SIZE, CELL_SIZE).draw(WINDOW)
#ImageGrid(BUNNY_MARGIN_SIDE+CELL_SIZE*3+BETWEEN_CELLS*3, BOARD_MARGIN_TOP+BETWEEN_CELLS*4+CELL_SIZE*4, horse, CELL_SIZE, CELL_SIZE).draw(WINDOW)

print(animalBoardCoordinates)

WINDOW.blit(textSurface, (BUNNY_MARGIN_SIDE+DOFORA*5+CELL_SIZE-38, BOARD_MARGIN_TOP+CELL_SIZE-35))
WINDOW.blit(textSurface, (BUNNY_MARGIN_SIDE+CELL_SIZE/2+DOFORA*4+CELL_SIZE-38, BOARD_MARGIN_TOP+BETWEEN_CELLS+CELL_SIZE+CELL_SIZE-35))
WINDOW.blit(textSurface, (BUNNY_MARGIN_SIDE+CELL_SIZE+BETWEEN_CELLS+DOFORA*3+CELL_SIZE-38, BOARD_MARGIN_TOP+BETWEEN_CELLS*2+CELL_SIZE*2+CELL_SIZE-35))
WINDOW.blit(textSurface, (BUNNY_MARGIN_SIDE+CELL_SIZE+BETWEEN_CELLS+CELL_SIZE/2+DOFORA*2+CELL_SIZE-38, BOARD_MARGIN_TOP+BETWEEN_CELLS*3+CELL_SIZE*3+CELL_SIZE-35))
WINDOW.blit(textSurface, (BUNNY_MARGIN_SIDE+CELL_SIZE*3+BETWEEN_CELLS*3+CELL_SIZE-38, BOARD_MARGIN_TOP+BETWEEN_CELLS*4+CELL_SIZE*4+CELL_SIZE-35))

# Player two
BUNNY_MARGIN_SIDE = BUNNY_MARGIN_SIDE_TWO
# for i in range(5):
#     if i == 1:
#         bunny.set_alpha(255)
#         sheep.set_alpha(255)
#         pig.set_alpha(255)
#         cow.set_alpha(255)
#
#     ImageGrid(BUNNY_MARGIN_SIDE+DOFORA*i, BOARD_MARGIN_TOP, bunny, CELL_SIZE, CELL_SIZE).draw(WINDOW) #Rabbits
#     if i < 4: # Sheeps
#         ImageGrid(BUNNY_MARGIN_SIDE+CELL_SIZE/2+DOFORA*i, BOARD_MARGIN_TOP+BETWEEN_CELLS+CELL_SIZE, sheep, CELL_SIZE, CELL_SIZE).draw(WINDOW)
#     if i < 3: # Pigs
#         ImageGrid(BUNNY_MARGIN_SIDE+CELL_SIZE+BETWEEN_CELLS+DOFORA*i, BOARD_MARGIN_TOP+BETWEEN_CELLS*2+CELL_SIZE*2, pig, CELL_SIZE, CELL_SIZE).draw(WINDOW)
#     if i < 2: # Cows
#         ImageGrid(BUNNY_MARGIN_SIDE+CELL_SIZE+BETWEEN_CELLS+CELL_SIZE/2+DOFORA*i, BOARD_MARGIN_TOP+BETWEEN_CELLS*3+CELL_SIZE*3, cow, CELL_SIZE, CELL_SIZE).draw(WINDOW)
# ImageGrid(BUNNY_MARGIN_SIDE+CELL_SIZE*2+BETWEEN_CELLS*2, BOARD_MARGIN_TOP+BETWEEN_CELLS*4+CELL_SIZE*4, horse, CELL_SIZE, CELL_SIZE).draw(WINDOW)
#
# # Additional animals
# font = py.font.Font('C:\Windows\Fonts\BRLNSDB.TTF', 32)
# text = "+3"
# black = (0,0,0)
# textSurface = font.render(text, True, black)
# ImageGrid(BUNNY_MARGIN_SIDE+DOFORA*5, BOARD_MARGIN_TOP, bunny, CELL_SIZE, CELL_SIZE).draw(WINDOW)
# ImageGrid(BUNNY_MARGIN_SIDE + CELL_SIZE / 2 + DOFORA * 4, BOARD_MARGIN_TOP + BETWEEN_CELLS + CELL_SIZE, sheep,
#           CELL_SIZE, CELL_SIZE).draw(WINDOW)
# ImageGrid(BUNNY_MARGIN_SIDE+CELL_SIZE+BETWEEN_CELLS+DOFORA*3, BOARD_MARGIN_TOP+BETWEEN_CELLS*2+CELL_SIZE*2, pig, CELL_SIZE, CELL_SIZE).draw(WINDOW)
# ImageGrid(BUNNY_MARGIN_SIDE+CELL_SIZE+BETWEEN_CELLS+CELL_SIZE/2+DOFORA*2, BOARD_MARGIN_TOP+BETWEEN_CELLS*3+CELL_SIZE*3, cow, CELL_SIZE, CELL_SIZE).draw(WINDOW)
# ImageGrid(BUNNY_MARGIN_SIDE+CELL_SIZE*3+BETWEEN_CELLS*3, BOARD_MARGIN_TOP+BETWEEN_CELLS*4+CELL_SIZE*4, horse, CELL_SIZE, CELL_SIZE).draw(WINDOW)
#
# WINDOW.blit(textSurface, (BUNNY_MARGIN_SIDE+DOFORA*5+CELL_SIZE-38, BOARD_MARGIN_TOP+CELL_SIZE-35))
# WINDOW.blit(textSurface, (BUNNY_MARGIN_SIDE+CELL_SIZE/2+DOFORA*4+CELL_SIZE-38, BOARD_MARGIN_TOP+BETWEEN_CELLS+CELL_SIZE+CELL_SIZE-35))
# WINDOW.blit(textSurface, (BUNNY_MARGIN_SIDE+CELL_SIZE+BETWEEN_CELLS+DOFORA*3+CELL_SIZE-38, BOARD_MARGIN_TOP+BETWEEN_CELLS*2+CELL_SIZE*2+CELL_SIZE-35))
# WINDOW.blit(textSurface, (BUNNY_MARGIN_SIDE+CELL_SIZE+BETWEEN_CELLS+CELL_SIZE/2+DOFORA*2+CELL_SIZE-38, BOARD_MARGIN_TOP+BETWEEN_CELLS*3+CELL_SIZE*3+CELL_SIZE-35))
# WINDOW.blit(textSurface, (BUNNY_MARGIN_SIDE+CELL_SIZE*3+BETWEEN_CELLS*3+CELL_SIZE-38, BOARD_MARGIN_TOP+BETWEEN_CELLS*4+CELL_SIZE*4+CELL_SIZE-35))
bunny.set_alpha(128)
sheep.set_alpha(128)
pig.set_alpha(128)
cow.set_alpha(128)
horse.set_alpha(128)

for i in range(5):
    if i == 1:
        bunny.set_alpha(255)
        sheep.set_alpha(255)
        pig.set_alpha(255)
        cow.set_alpha(255)

    #ImageGrid(BUNNY_MARGIN_SIDE+DOFORA*i, BOARD_MARGIN_TOP, bunny, CELL_SIZE, CELL_SIZE).draw(WINDOW) #Rabbits
    py.draw.circle(WINDOW, BLU, (BUNNY_MARGIN_SIDE+CELL_SIZE/2*(i+1)+DOFORA2*i, BOARD_MARGIN_TOP+CELL_SIZE/2), CELL_SIZE/2)
    ImageGrid(BUNNY_MARGIN_SIDE+DOFORA*i+CELL_SIZE/10, BOARD_MARGIN_TOP+CELL_SIZE/10, bunny, CELL_SIZE*4/5, CELL_SIZE*4/5).draw(WINDOW)
    animalBoardCoordinates[0][0].append((BUNNY_MARGIN_SIDE+CELL_SIZE/2*(i+1)+DOFORA2*i, BOARD_MARGIN_TOP+CELL_SIZE/2))
    #print(animalBoardCoordinates[0][0][i])
    if i < 4: # Sheeps
        py.draw.circle(WINDOW, BLU,
                       (BUNNY_MARGIN_SIDE + CELL_SIZE + DOFORA * i, BOARD_MARGIN_TOP + CELL_SIZE*1.5+BETWEEN_CELLS/2),
                       CELL_SIZE / 2)
        ImageGrid(BUNNY_MARGIN_SIDE+CELL_SIZE/2+DOFORA*i+CELL_SIZE/10, BOARD_MARGIN_TOP+BETWEEN_CELLS/2+CELL_SIZE+CELL_SIZE/10, sheep, CELL_SIZE*4/5, CELL_SIZE*4/5).draw(WINDOW)
        animalBoardCoordinates[0][1].append((BUNNY_MARGIN_SIDE + CELL_SIZE + DOFORA * i, BOARD_MARGIN_TOP + CELL_SIZE+CELL_SIZE/2+BETWEEN_CELLS/2))
    if i < 3: # Pigs
        py.draw.circle(WINDOW, BLU, (BUNNY_MARGIN_SIDE+DOFORA+CELL_SIZE/2*(i+1)+DOFORA2*i, BOARD_MARGIN_TOP+CELL_SIZE*2.5+BETWEEN_CELLS), CELL_SIZE/2)
        ImageGrid(BUNNY_MARGIN_SIDE+CELL_SIZE+BETWEEN_CELLS+DOFORA*i+CELL_SIZE/8, BOARD_MARGIN_TOP+BETWEEN_CELLS+CELL_SIZE*2+CELL_SIZE/12, pig, CELL_SIZE*3/4, CELL_SIZE*3/4).draw(WINDOW)
        animalBoardCoordinates[0][2].append((BUNNY_MARGIN_SIDE+DOFORA+CELL_SIZE/2*(i+1)+DOFORA2*i, BOARD_MARGIN_TOP+CELL_SIZE*2.5+BETWEEN_CELLS))
    if i < 2: # Cows
        py.draw.circle(WINDOW, BLU, (BUNNY_MARGIN_SIDE + CELL_SIZE*2 + BETWEEN_CELLS + DOFORA * i, BOARD_MARGIN_TOP + CELL_SIZE*3.5+BETWEEN_CELLS*1.5), CELL_SIZE/2)
        ImageGrid(BUNNY_MARGIN_SIDE+CELL_SIZE*1.5+BETWEEN_CELLS*1.2+DOFORA*i+CELL_SIZE/10, BOARD_MARGIN_TOP+BETWEEN_CELLS*1.5+CELL_SIZE*3+CELL_SIZE/10, cow, CELL_SIZE*4/5, CELL_SIZE*4/5).draw(WINDOW)
        animalBoardCoordinates[0][3].append((BUNNY_MARGIN_SIDE + CELL_SIZE*2 + BETWEEN_CELLS + DOFORA * i, BOARD_MARGIN_TOP + CELL_SIZE*3.5+BETWEEN_CELLS*1.5))
py.draw.circle(WINDOW, BLU, (BUNNY_MARGIN_SIDE+DOFORA*2+CELL_SIZE/2, BOARD_MARGIN_TOP+CELL_SIZE*4.5+BETWEEN_CELLS*2), CELL_SIZE/2)
ImageGrid(BUNNY_MARGIN_SIDE+CELL_SIZE*2+BETWEEN_CELLS*2+CELL_SIZE/10, BOARD_MARGIN_TOP+BETWEEN_CELLS*2+CELL_SIZE*4+CELL_SIZE/10, horse, CELL_SIZE*3/4, CELL_SIZE*3/4).draw(WINDOW)
animalBoardCoordinates[0][4].append((BUNNY_MARGIN_SIDE+DOFORA*2+CELL_SIZE/2, BOARD_MARGIN_TOP+CELL_SIZE*4.5+BETWEEN_CELLS*2))
horse.set_alpha(255)

# Additional animals
drawcircles(WINDOW, BLU, BLU2, BLU3, BUNNY_MARGIN_SIDE+DOFORA*5, BUNNY_MARGIN_SIDE+DOFORA*4, BOARD_MARGIN_TOP, bunny, 2/3, 0, 0)
drawcircles(WINDOW, BLU, BLU2, BLU3, BUNNY_MARGIN_SIDE+DOFORA*4+CELL_SIZE/2, BUNNY_MARGIN_SIDE+DOFORA*3+CELL_SIZE/2, BOARD_MARGIN_TOP+CELL_SIZE+BETWEEN_CELLS/2, sheep, 2/3, 1, 0)
drawcircles(WINDOW, BLU, BLU2, BLU3, BUNNY_MARGIN_SIDE+DOFORA*4, BUNNY_MARGIN_SIDE+DOFORA*3, BOARD_MARGIN_TOP+CELL_SIZE*2+BETWEEN_CELLS, pig, 7/12, 2, 0)
drawcircles(WINDOW, BLU, BLU2, BLU3, BUNNY_MARGIN_SIDE+DOFORA*3+CELL_SIZE/2, BUNNY_MARGIN_SIDE+DOFORA*2+CELL_SIZE/2, BOARD_MARGIN_TOP+CELL_SIZE*3+BETWEEN_CELLS*1.5, cow, 2/3, 3, 0)
drawcircles(WINDOW, BLU, BLU2, BLU3, BUNNY_MARGIN_SIDE+DOFORA*3, BUNNY_MARGIN_SIDE+DOFORA*2, BOARD_MARGIN_TOP+CELL_SIZE*4+BETWEEN_CELLS*2, horse, 7/12, 4, 0)


py.display.flip()





runnin = True
while runnin:
    for event in py.event.get():
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                runnin = False
        if event.type == py.QUIT:
            runnin = False

py.quit()
