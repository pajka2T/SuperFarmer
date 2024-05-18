import pygame as py
import math
import players_data as pd


class Image:
    def __init__(self, x, y, image, width, height):
        #print("UUU")
        self.image = py.transform.scale(image, (width, height))
        self.rect = image.get_rect()  # copy the image dimensions
        self.rect.x = x
        self.rect.y = y                 # move to location
    def draw(self, window):
        window.blit(self.image, self.rect)
def draw_additional_animals(window, color1, color2, color3, x, x2, y, animal, size, CELL_SIZE):
    py.draw.circle(window, color3, (x + CELL_SIZE / 1.8, y + CELL_SIZE / 1.8), CELL_SIZE / 2.4)
    py.draw.circle(window, color2, (x2 + CELL_SIZE + CELL_SIZE / 2, y + CELL_SIZE / 1.7), CELL_SIZE / 2.4)
    py.draw.circle(window, color1, (x2 + CELL_SIZE + CELL_SIZE / 1.8, y + CELL_SIZE / 2.4), CELL_SIZE / 2.4)
    #print(y, " ", y+(CELL_SIZE/1.7)*2)
    Image(x2 + CELL_SIZE + CELL_SIZE / 1.8 + CELL_SIZE / 12 - CELL_SIZE / 2.4, y + CELL_SIZE / 2.4 + CELL_SIZE / 12 - CELL_SIZE / 2.4, animal, CELL_SIZE * size, CELL_SIZE * size).draw(window)

    #print(animalBoardCoordinates[player][animalnumber][5-animalnumber])

def draw_empty_circles(window, color1, color2, x, y, CELL_SIZE):
    py.draw.circle(window, color1, (x, y), CELL_SIZE/2)
    py.draw.circle(window, color2, (x, y), CELL_SIZE/2.2)

def drawanimals(window, color1, x, y, r, size, animal):
    py.draw.circle(window, color1, (x, y), r)
    Image(x - r + 2 * r / size, y - r + 2 * r / size, animal, (1 - 2 / size) * 2 * r, (1 - 2 / size) * 2 * r).draw(window)
    #ImageGrid(x, y, animal, r*2, r*2).draw(window)


players = 2
animalBoardCoordinates = [[[] for j in range(5)] for k in range(players)]



def createBoard(WINDOW):
    #players = int(input("Gracze"))

    py.init()
    #WINDOW = py.display.set_mode((0, 0), py.FULLSCREEN)
    #WINDOW = py.display.set_mode((1500, 800))
    #py.display.set_caption("SuperFarmer")
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

    #barrier = py.image.load('Images/barrier.png').convert_alpha()
    fence = py.image.load('Images/fence2.png').convert_alpha()
    bluefarmer = py.image.load('Images/bluefarmer.png').convert_alpha()
    bluefarmer_width, bluefarmer_height = bluefarmer.get_size()
    #print(bluefarmer_width, bluefarmer_height)
    redfarmer = py.image.load('Images/redfarmer.png').convert_alpha()
    redfarmer_width, redfarmer_height = redfarmer.get_size()

    Image(SCREENWIDTH - bluefarmer_width / 4, SCREENHEIGHT - bluefarmer_height / 3, bluefarmer, bluefarmer_width / 3, bluefarmer_height / 3).draw(WINDOW)
    Image(-redfarmer_width / 10, SCREENHEIGHT - redfarmer_height / 3, redfarmer, redfarmer_width / 3, redfarmer_height / 3).draw(WINDOW)

    BLU = (52, 229, 235)
    BLU2 = (93, 190, 194)
    BLU3 = (38, 125, 128)
    BLACK = (0, 0, 0)

    szerokosc_pola = CELL_SIZE*5+BETWEEN_CELLS*4

    # Player one
    for i in range(8):
        Image(BUNNY_MARGIN_SIDE + szerokosc_pola / 8 * i, BOARD_MARGIN_TOP - szerokosc_pola / 12, fence, szerokosc_pola / 8, szerokosc_pola / 12).draw(WINDOW)

    py.draw.polygon(WINDOW, (255, 255, 255), [(BUNNY_MARGIN_SIDE, BOARD_MARGIN_TOP), (BUNNY_MARGIN_SIDE+szerokosc_pola, BOARD_MARGIN_TOP), (BUNNY_MARGIN_SIDE+szerokosc_pola/2, BOARD_MARGIN_TOP+CELL_SIZE*5)], 0)

    for i in range(5):
        if i == 1:
            bunny.set_alpha(255)
            sheep.set_alpha(255)
            pig.set_alpha(255)
            cow.set_alpha(255)

        #ImageGrid(BUNNY_MARGIN_SIDE+DOFORA*i, BOARD_MARGIN_TOP, bunny, CELL_SIZE, CELL_SIZE).draw(WINDOW) #Rabbits
        if i == 0:
            py.draw.circle(WINDOW, BLU, (BUNNY_MARGIN_SIDE+CELL_SIZE/2*(i+1)+DOFORA2*i, BOARD_MARGIN_TOP+CELL_SIZE/2), CELL_SIZE/2)
            Image(BUNNY_MARGIN_SIDE + DOFORA * i + CELL_SIZE / 10, BOARD_MARGIN_TOP + CELL_SIZE / 10, bunny, CELL_SIZE * 4 / 5, CELL_SIZE * 4 / 5).draw(WINDOW)
        if i > 0:
            draw_empty_circles(WINDOW, BLU, BLACK, BUNNY_MARGIN_SIDE+CELL_SIZE/2*(i+1)+DOFORA2*i, BOARD_MARGIN_TOP+CELL_SIZE/2, CELL_SIZE)
        animalBoardCoordinates[0][0].append((BUNNY_MARGIN_SIDE+CELL_SIZE/2*(i+1)+DOFORA2*i, BOARD_MARGIN_TOP+CELL_SIZE/2))
        if i < 4: # Sheeps
            if i == 0:
                py.draw.circle(WINDOW, BLU,
                           (BUNNY_MARGIN_SIDE + CELL_SIZE + DOFORA * i, BOARD_MARGIN_TOP + CELL_SIZE*1.5+BETWEEN_CELLS/2),
                           CELL_SIZE / 2)
                Image(BUNNY_MARGIN_SIDE + CELL_SIZE / 2 + DOFORA * i + CELL_SIZE / 10, BOARD_MARGIN_TOP + BETWEEN_CELLS / 2 + CELL_SIZE + CELL_SIZE / 10, sheep, CELL_SIZE * 4 / 5, CELL_SIZE * 4 / 5).draw(WINDOW)
            if i > 0:
                draw_empty_circles(WINDOW, BLU, BLACK, BUNNY_MARGIN_SIDE + CELL_SIZE + DOFORA * i, BOARD_MARGIN_TOP + CELL_SIZE*1.5+BETWEEN_CELLS/2, CELL_SIZE)
            animalBoardCoordinates[0][1].append((BUNNY_MARGIN_SIDE + CELL_SIZE + DOFORA * i, BOARD_MARGIN_TOP + CELL_SIZE+CELL_SIZE/2+BETWEEN_CELLS/2))
        if i < 3: # Pigs
            if i == 0:
                py.draw.circle(WINDOW, BLU, (BUNNY_MARGIN_SIDE+DOFORA+CELL_SIZE/2*(i+1)+DOFORA2*i, BOARD_MARGIN_TOP+CELL_SIZE*2.5+BETWEEN_CELLS), CELL_SIZE/2)
                Image(BUNNY_MARGIN_SIDE + CELL_SIZE + BETWEEN_CELLS + DOFORA * i + CELL_SIZE / 8, BOARD_MARGIN_TOP + BETWEEN_CELLS + CELL_SIZE * 2 + CELL_SIZE / 12, pig, CELL_SIZE * 3 / 4, CELL_SIZE * 3 / 4).draw(WINDOW)
            if i > 0:
                draw_empty_circles(WINDOW, BLU, BLACK, BUNNY_MARGIN_SIDE+DOFORA+CELL_SIZE/2*(i+1)+DOFORA2*i, BOARD_MARGIN_TOP+CELL_SIZE*2.5+BETWEEN_CELLS, CELL_SIZE)
            animalBoardCoordinates[0][2].append((BUNNY_MARGIN_SIDE+DOFORA+CELL_SIZE/2*(i+1)+DOFORA2*i, BOARD_MARGIN_TOP+CELL_SIZE*2.5+BETWEEN_CELLS))
        if i < 2: # Cows
            if i == 0:
                py.draw.circle(WINDOW, BLU, (BUNNY_MARGIN_SIDE + CELL_SIZE*2 + BETWEEN_CELLS + DOFORA * i, BOARD_MARGIN_TOP + CELL_SIZE*3.5+BETWEEN_CELLS*1.5), CELL_SIZE/2)
                Image(BUNNY_MARGIN_SIDE + CELL_SIZE * 1.5 + BETWEEN_CELLS * 1.2 + DOFORA * i + CELL_SIZE / 10, BOARD_MARGIN_TOP + BETWEEN_CELLS * 1.5 + CELL_SIZE * 3 + CELL_SIZE / 10, cow, CELL_SIZE * 4 / 5, CELL_SIZE * 4 / 5).draw(WINDOW)
            if i > 0:
                draw_empty_circles(WINDOW, BLU, BLACK, BUNNY_MARGIN_SIDE + CELL_SIZE*2 + BETWEEN_CELLS + DOFORA * i, BOARD_MARGIN_TOP + CELL_SIZE*3.5+BETWEEN_CELLS*1.5, CELL_SIZE)
            animalBoardCoordinates[0][3].append((BUNNY_MARGIN_SIDE + CELL_SIZE*2 + BETWEEN_CELLS + DOFORA * i, BOARD_MARGIN_TOP + CELL_SIZE*3.5+BETWEEN_CELLS*1.5))
    py.draw.circle(WINDOW, BLU, (BUNNY_MARGIN_SIDE+DOFORA*2+CELL_SIZE/2, BOARD_MARGIN_TOP+CELL_SIZE*4.5+BETWEEN_CELLS*2), CELL_SIZE/2)
    Image(BUNNY_MARGIN_SIDE + CELL_SIZE * 2 + BETWEEN_CELLS * 2 + CELL_SIZE / 10, BOARD_MARGIN_TOP + BETWEEN_CELLS * 2 + CELL_SIZE * 4 + CELL_SIZE / 10, horse, CELL_SIZE * 3 / 4, CELL_SIZE * 3 / 4).draw(WINDOW)
    animalBoardCoordinates[0][4].append((BUNNY_MARGIN_SIDE+DOFORA*2+CELL_SIZE/2, BOARD_MARGIN_TOP+CELL_SIZE*4.5+BETWEEN_CELLS*2))
    horse.set_alpha(255)

    # Additional animals
    font = py.font.Font('Fonts/BRLNSDB.ttf', 32)
    text = "+3"
    black = (0, 0, 0)
    white = (255, 255, 255)
    textSurface = font.render(text, True, white)

    # animalBoardCoordinates[player][animal][len] = (x lewy narożnik, y margines od góry, x1 do drawcircles, x2 do drawcircles)
    # żeby mieć x2 do drawcircles trzeba od x odjąć CELL_SIZE + CELL_SIZE / 2 - CELL_SIZE / 2.4

    #drawcircles(WINDOW, BLU, BLU2, BLU3, BUNNY_MARGIN_SIDE+DOFORA*5, BUNNY_MARGIN_SIDE+DOFORA*4, BOARD_MARGIN_TOP, bunny, 2/3, 0, 0, CELL_SIZE)
    animalBoardCoordinates[0][0].append((BUNNY_MARGIN_SIDE+DOFORA*4 + CELL_SIZE + CELL_SIZE / 2 - CELL_SIZE / 2.4, BOARD_MARGIN_TOP, BUNNY_MARGIN_SIDE+DOFORA*5, BUNNY_MARGIN_SIDE+DOFORA*4, 2/3))

    #drawcircles(WINDOW, BLU, BLU2, BLU3, BUNNY_MARGIN_SIDE+DOFORA*4+CELL_SIZE/2, BUNNY_MARGIN_SIDE+DOFORA*3+CELL_SIZE/2, BOARD_MARGIN_TOP+CELL_SIZE+BETWEEN_CELLS/2, sheep, 2/3, 1, 0, CELL_SIZE)
    animalBoardCoordinates[0][1].append((BUNNY_MARGIN_SIDE+DOFORA*3+CELL_SIZE/2+CELL_SIZE + CELL_SIZE / 2 - CELL_SIZE / 2.4, BOARD_MARGIN_TOP+CELL_SIZE+BETWEEN_CELLS/2, BUNNY_MARGIN_SIDE+DOFORA*4+CELL_SIZE/2, BUNNY_MARGIN_SIDE+DOFORA*3+CELL_SIZE/2, 2/3))

    #drawcircles(WINDOW, BLU, BLU2, BLU3, BUNNY_MARGIN_SIDE+DOFORA*4, BUNNY_MARGIN_SIDE+DOFORA*3, BOARD_MARGIN_TOP+CELL_SIZE*2+BETWEEN_CELLS, pig, 7/12, 2, 0, CELL_SIZE)
    animalBoardCoordinates[0][2].append((BUNNY_MARGIN_SIDE+DOFORA*3 + CELL_SIZE + CELL_SIZE / 2 - CELL_SIZE / 2.4, BOARD_MARGIN_TOP+CELL_SIZE*2+BETWEEN_CELLS, BUNNY_MARGIN_SIDE+DOFORA*4, BUNNY_MARGIN_SIDE+DOFORA*3, 7/12))

    #drawcircles(WINDOW, BLU, BLU2, BLU3, BUNNY_MARGIN_SIDE+DOFORA*3+CELL_SIZE/2, BUNNY_MARGIN_SIDE+DOFORA*2+CELL_SIZE/2, BOARD_MARGIN_TOP+CELL_SIZE*3+BETWEEN_CELLS*1.5, cow, 2/3, 3, 0, CELL_SIZE)
    animalBoardCoordinates[0][3].append((BUNNY_MARGIN_SIDE+DOFORA*2+CELL_SIZE/2+ CELL_SIZE + CELL_SIZE / 2 - CELL_SIZE / 2.4, BOARD_MARGIN_TOP+CELL_SIZE*3+BETWEEN_CELLS*1.5, BUNNY_MARGIN_SIDE+DOFORA*3+CELL_SIZE/2, BUNNY_MARGIN_SIDE+DOFORA*2+CELL_SIZE/2, 2/3))

    #drawcircles(WINDOW, BLU, BLU2, BLU3, BUNNY_MARGIN_SIDE+DOFORA*3, BUNNY_MARGIN_SIDE+DOFORA*2, BOARD_MARGIN_TOP+CELL_SIZE*4+BETWEEN_CELLS*2, horse, 7/12, 4, 0, CELL_SIZE)
    animalBoardCoordinates[0][4].append((BUNNY_MARGIN_SIDE+DOFORA*2+ CELL_SIZE + CELL_SIZE / 2 - CELL_SIZE / 2.4, BOARD_MARGIN_TOP+CELL_SIZE*4+BETWEEN_CELLS*2, BUNNY_MARGIN_SIDE+DOFORA*3, BUNNY_MARGIN_SIDE+DOFORA*2, 7/12))

    #ImageGrid(BUNNY_MARGIN_SIDE+CELL_SIZE+BETWEEN_CELLS+DOFORA*3, BOARD_MARGIN_TOP+BETWEEN_CELLS*2+CELL_SIZE*2, pig, CELL_SIZE, CELL_SIZE).draw(WINDOW)
    #ImageGrid(BUNNY_MARGIN_SIDE+CELL_SIZE+BETWEEN_CELLS+CELL_SIZE/2+DOFORA*2, BOARD_MARGIN_TOP+BETWEEN_CELLS*3+CELL_SIZE*3, cow, CELL_SIZE, CELL_SIZE).draw(WINDOW)
    #ImageGrid(BUNNY_MARGIN_SIDE+CELL_SIZE*3+BETWEEN_CELLS*3, BOARD_MARGIN_TOP+BETWEEN_CELLS*4+CELL_SIZE*4, horse, CELL_SIZE, CELL_SIZE).draw(WINDOW)

    #print(animalBoardCoordinates)

    # WINDOW.blit(textSurface, (BUNNY_MARGIN_SIDE+DOFORA*5+CELL_SIZE-38, BOARD_MARGIN_TOP+CELL_SIZE-35))
    # WINDOW.blit(textSurface, (BUNNY_MARGIN_SIDE+CELL_SIZE/2+DOFORA*4+CELL_SIZE-38, BOARD_MARGIN_TOP+BETWEEN_CELLS+CELL_SIZE+CELL_SIZE-35))
    # WINDOW.blit(textSurface, (BUNNY_MARGIN_SIDE+CELL_SIZE+BETWEEN_CELLS+DOFORA*3+CELL_SIZE-38, BOARD_MARGIN_TOP+BETWEEN_CELLS*2+CELL_SIZE*2+CELL_SIZE-35))
    # WINDOW.blit(textSurface, (BUNNY_MARGIN_SIDE+CELL_SIZE+BETWEEN_CELLS+CELL_SIZE/2+DOFORA*2+CELL_SIZE-38, BOARD_MARGIN_TOP+BETWEEN_CELLS*3+CELL_SIZE*3+CELL_SIZE-35))
    # WINDOW.blit(textSurface, (BUNNY_MARGIN_SIDE+CELL_SIZE*3+BETWEEN_CELLS*3+CELL_SIZE-38, BOARD_MARGIN_TOP+BETWEEN_CELLS*4+CELL_SIZE*4+CELL_SIZE-35))

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
        if i == 0:
            py.draw.circle(WINDOW, BLU, (
            BUNNY_MARGIN_SIDE + CELL_SIZE / 2 * (i + 1) + DOFORA2 * i, BOARD_MARGIN_TOP + CELL_SIZE / 2), CELL_SIZE / 2)
            Image(BUNNY_MARGIN_SIDE + DOFORA * i + CELL_SIZE / 10, BOARD_MARGIN_TOP + CELL_SIZE / 10, bunny,
                  CELL_SIZE * 4 / 5, CELL_SIZE * 4 / 5).draw(WINDOW)
        if i > 0:
            draw_empty_circles(WINDOW, BLU, BLACK, BUNNY_MARGIN_SIDE + CELL_SIZE / 2 * (i + 1) + DOFORA2 * i,
                               BOARD_MARGIN_TOP + CELL_SIZE / 2, CELL_SIZE)

        animalBoardCoordinates[1][0].append((BUNNY_MARGIN_SIDE+CELL_SIZE/2*(i+1)+DOFORA2*i, BOARD_MARGIN_TOP+CELL_SIZE/2))
        #print(animalBoardCoordinates[0][0][i])
        if i < 4: # Sheeps
            if i == 0:
                py.draw.circle(WINDOW, BLU,
                               (BUNNY_MARGIN_SIDE + CELL_SIZE + DOFORA * i,
                                BOARD_MARGIN_TOP + CELL_SIZE * 1.5 + BETWEEN_CELLS / 2),
                               CELL_SIZE / 2)
                Image(BUNNY_MARGIN_SIDE + CELL_SIZE / 2 + DOFORA * i + CELL_SIZE / 10,
                      BOARD_MARGIN_TOP + BETWEEN_CELLS / 2 + CELL_SIZE + CELL_SIZE / 10, sheep, CELL_SIZE * 4 / 5,
                      CELL_SIZE * 4 / 5).draw(WINDOW)
            if i > 0:
                draw_empty_circles(WINDOW, BLU, BLACK, BUNNY_MARGIN_SIDE + CELL_SIZE + DOFORA * i,
                                   BOARD_MARGIN_TOP + CELL_SIZE * 1.5 + BETWEEN_CELLS / 2, CELL_SIZE)
        animalBoardCoordinates[1][1].append((BUNNY_MARGIN_SIDE + CELL_SIZE + DOFORA * i, BOARD_MARGIN_TOP + CELL_SIZE+CELL_SIZE/2+BETWEEN_CELLS/2))
        if i < 3: # Pigs
            if i == 0:
                py.draw.circle(WINDOW, BLU, (BUNNY_MARGIN_SIDE + DOFORA + CELL_SIZE / 2 * (i + 1) + DOFORA2 * i,
                                             BOARD_MARGIN_TOP + CELL_SIZE * 2.5 + BETWEEN_CELLS), CELL_SIZE / 2)
                Image(BUNNY_MARGIN_SIDE + CELL_SIZE + BETWEEN_CELLS + DOFORA * i + CELL_SIZE / 8,
                      BOARD_MARGIN_TOP + BETWEEN_CELLS + CELL_SIZE * 2 + CELL_SIZE / 12, pig, CELL_SIZE * 3 / 4,
                      CELL_SIZE * 3 / 4).draw(WINDOW)
            if i > 0:
                draw_empty_circles(WINDOW, BLU, BLACK,
                                   BUNNY_MARGIN_SIDE + DOFORA + CELL_SIZE / 2 * (i + 1) + DOFORA2 * i,
                                   BOARD_MARGIN_TOP + CELL_SIZE * 2.5 + BETWEEN_CELLS, CELL_SIZE)
            animalBoardCoordinates[1][2].append((BUNNY_MARGIN_SIDE+DOFORA+CELL_SIZE/2*(i+1)+DOFORA2*i, BOARD_MARGIN_TOP+CELL_SIZE*2.5+BETWEEN_CELLS))
        if i < 2: # Cows
            if i == 0:
                py.draw.circle(WINDOW, BLU, (BUNNY_MARGIN_SIDE + CELL_SIZE * 2 + BETWEEN_CELLS + DOFORA * i,
                                             BOARD_MARGIN_TOP + CELL_SIZE * 3.5 + BETWEEN_CELLS * 1.5), CELL_SIZE / 2)
                Image(BUNNY_MARGIN_SIDE + CELL_SIZE * 1.5 + BETWEEN_CELLS * 1.2 + DOFORA * i + CELL_SIZE / 10,
                      BOARD_MARGIN_TOP + BETWEEN_CELLS * 1.5 + CELL_SIZE * 3 + CELL_SIZE / 10, cow,
                      CELL_SIZE * 4 / 5, CELL_SIZE * 4 / 5).draw(WINDOW)
            if i > 0:
                draw_empty_circles(WINDOW, BLU, BLACK, BUNNY_MARGIN_SIDE + CELL_SIZE * 2 + BETWEEN_CELLS + DOFORA * i,
                                   BOARD_MARGIN_TOP + CELL_SIZE * 3.5 + BETWEEN_CELLS * 1.5, CELL_SIZE)
            animalBoardCoordinates[1][3].append((BUNNY_MARGIN_SIDE + CELL_SIZE*2 + BETWEEN_CELLS + DOFORA * i, BOARD_MARGIN_TOP + CELL_SIZE*3.5+BETWEEN_CELLS*1.5))
    py.draw.circle(WINDOW, BLU, (BUNNY_MARGIN_SIDE+DOFORA*2+CELL_SIZE/2, BOARD_MARGIN_TOP+CELL_SIZE*4.5+BETWEEN_CELLS*2), CELL_SIZE/2)
    Image(BUNNY_MARGIN_SIDE + CELL_SIZE * 2 + BETWEEN_CELLS * 2 + CELL_SIZE / 10, BOARD_MARGIN_TOP + BETWEEN_CELLS * 2 + CELL_SIZE * 4 + CELL_SIZE / 10, horse, CELL_SIZE * 3 / 4, CELL_SIZE * 3 / 4).draw(WINDOW)
    animalBoardCoordinates[1][4].append((BUNNY_MARGIN_SIDE+DOFORA*2+CELL_SIZE/2, BOARD_MARGIN_TOP+CELL_SIZE*4.5+BETWEEN_CELLS*2))
    horse.set_alpha(255)

    # Additional animals
    # drawcircles(WINDOW, BLU, BLU2, BLU3, BUNNY_MARGIN_SIDE+DOFORA*5, BUNNY_MARGIN_SIDE+DOFORA*4, BOARD_MARGIN_TOP, bunny, 2/3, 0, 1, CELL_SIZE)
    #animalBoardCoordinates[1][0].append()
    animalBoardCoordinates[1][0].append((BUNNY_MARGIN_SIDE + DOFORA * 4 + CELL_SIZE + CELL_SIZE / 2 - CELL_SIZE / 2.4,
                                         BOARD_MARGIN_TOP, BUNNY_MARGIN_SIDE + DOFORA * 5,
                                         BUNNY_MARGIN_SIDE + DOFORA * 4, 2 / 3))

    # drawcircles(WINDOW, BLU, BLU2, BLU3, BUNNY_MARGIN_SIDE+DOFORA*4+CELL_SIZE/2, BUNNY_MARGIN_SIDE+DOFORA*3+CELL_SIZE/2, BOARD_MARGIN_TOP+CELL_SIZE+BETWEEN_CELLS/2, sheep, 2/3, 1, 0, CELL_SIZE)
    animalBoardCoordinates[1][1].append((
                                        BUNNY_MARGIN_SIDE + DOFORA * 3 + CELL_SIZE / 2 + CELL_SIZE + CELL_SIZE / 2 - CELL_SIZE / 2.4,
                                        BOARD_MARGIN_TOP + CELL_SIZE + BETWEEN_CELLS / 2,
                                        BUNNY_MARGIN_SIDE + DOFORA * 4 + CELL_SIZE / 2,
                                        BUNNY_MARGIN_SIDE + DOFORA * 3 + CELL_SIZE / 2, 2 / 3))

    # drawcircles(WINDOW, BLU, BLU2, BLU3, BUNNY_MARGIN_SIDE+DOFORA*4, BUNNY_MARGIN_SIDE+DOFORA*3, BOARD_MARGIN_TOP+CELL_SIZE*2+BETWEEN_CELLS, pig, 7/12, 2, 0, CELL_SIZE)
    animalBoardCoordinates[1][2].append((BUNNY_MARGIN_SIDE + DOFORA * 3 + CELL_SIZE + CELL_SIZE / 2 - CELL_SIZE / 2.4,
                                         BOARD_MARGIN_TOP + CELL_SIZE * 2 + BETWEEN_CELLS,
                                         BUNNY_MARGIN_SIDE + DOFORA * 4, BUNNY_MARGIN_SIDE + DOFORA * 3, 7 / 12))

    # drawcircles(WINDOW, BLU, BLU2, BLU3, BUNNY_MARGIN_SIDE+DOFORA*3+CELL_SIZE/2, BUNNY_MARGIN_SIDE+DOFORA*2+CELL_SIZE/2, BOARD_MARGIN_TOP+CELL_SIZE*3+BETWEEN_CELLS*1.5, cow, 2/3, 3, 0, CELL_SIZE)
    animalBoardCoordinates[1][3].append((
                                        BUNNY_MARGIN_SIDE + DOFORA * 2 + CELL_SIZE / 2 + CELL_SIZE + CELL_SIZE / 2 - CELL_SIZE / 2.4,
                                        BOARD_MARGIN_TOP + CELL_SIZE * 3 + BETWEEN_CELLS * 1.5,
                                        BUNNY_MARGIN_SIDE + DOFORA * 3 + CELL_SIZE / 2,
                                        BUNNY_MARGIN_SIDE + DOFORA * 2 + CELL_SIZE / 2, 2 / 3))

    # drawcircles(WINDOW, BLU, BLU2, BLU3, BUNNY_MARGIN_SIDE+DOFORA*3, BUNNY_MARGIN_SIDE+DOFORA*2, BOARD_MARGIN_TOP+CELL_SIZE*4+BETWEEN_CELLS*2, horse, 7/12, 4, 0, CELL_SIZE)
    animalBoardCoordinates[1][4].append((BUNNY_MARGIN_SIDE + DOFORA * 2 + CELL_SIZE + CELL_SIZE / 2 - CELL_SIZE / 2.4,
                                         BOARD_MARGIN_TOP + CELL_SIZE * 4 + BETWEEN_CELLS * 2,
                                         BUNNY_MARGIN_SIDE + DOFORA * 3, BUNNY_MARGIN_SIDE + DOFORA * 2, 7 / 12))

    print(animalBoardCoordinates)

    py.display.flip()

    return CELL_SIZE

#createBoard(py.display.set_mode((1500, 800)))



# runnin = True
# while runnin:
#     for event in py.event.get():
#         if event.type == py.KEYDOWN:
#             if event.key == py.K_ESCAPE:
#                 runnin = False
#         if event.type == py.QUIT:
#             runnin = False
#
# py.quit()