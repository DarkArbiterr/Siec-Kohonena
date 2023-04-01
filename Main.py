from Kohonen import Kohonen
import time
import sys
import pygame
import numpy as np
import random

margin = 5
width = 45
height = 21.5
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode([500, 550])
font = pygame.font.SysFont('Calibri', 20)
somH = 5
somW = 5

def Button(col, row, margin, txt="", color=(254, 134, 177)):
    pygame.draw.rect(screen, color, [(margin + width) * col + margin, (margin + height) * row + margin, width, height])
    label = font.render(txt, 1, (255,255,255))
    screen.blit(label, ((margin + width) * col + 2 * margin, (margin + height) * row + margin))

def IsClosedWindow():
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            return True
    return False

def DrawPoint(point, color):
    pygame.draw.circle(screen, color, (point[0], point[1]), 5)

def DrawMenu(points):
    newFont = pygame.font.SysFont('Calibri', 40)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen,(3, 166, 147),[50,50,400,400])
    Button(6,18,5, txt="Start" )
    Button(5,18,5, txt="Usun" )
    Button(4,17,5, txt="+" )
    Button(4,18,5, txt="-" )
    Button(2,17,5, txt="+" )
    Button(2,18,5, txt="-" )
    heightLabel = newFont.render(str(somH), 1, (255,255,255))
    widthLabel = newFont.render(str(somW), 1, (255,255,255))
    screen.blit(heightLabel, ((margin + width) * 1 + 3 * margin, (margin + height) * 17 + 2 * margin))
    screen.blit(widthLabel, ((margin + width) * 3 + 3 * margin, (margin + height) * 17 + 2 * margin))
    for p in points:
        DrawPoint(p, (255,255,255))
    pygame.display.flip()

def Animation(kohonen, data):
    for i in range(400):
        kohonen.Training(data)
        DrawMenu(data)
        listt = []

        for x in range(kohonen.shape[0]):
            for y in range(kohonen.shape[1]):
                listt.append(kohonen.som[x,y])
                if x < kohonen.shape[0] - 1:
                    pygame.draw.line(screen, (254, 134, 177), kohonen.som[x,y], kohonen.som[x+1,y], 5)
                if y < kohonen.shape[1] - 1:
                    pygame.draw.line(screen, (254, 134, 177), kohonen.som[x,y], kohonen.som[x,y+1], 5)
                pygame.draw.circle(screen, (254, 134, 177), kohonen.som[x,y], 5)
        pygame.display.flip()
        if IsClosedWindow():
            pygame.quit()
            exit()
        pygame.time.delay(50)

def main(alpha = 0.6, sigma = 1.2):
    points = []
    global somW, somH
    screen.fill((255,255,255))
    pygame.display.flip()
    isRun = True
    DrawMenu(points)

    while isRun:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                isRun = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                col = position[0] // (width + margin)
                row = position[1] // (height + margin)
                if row == 18 and col == 6:
                    kohonen = Kohonen(somH, somW, 2, alpha, sigma)
                    kohonen.som *= [400,400]
                    kohonen.som += [50,50]
                    Animation(kohonen, points)
                elif row == 18 and col == 5:
                    points = []
                    DrawMenu(points)
                elif row == 17 and col == 4:
                    somW += 1
                    DrawMenu(points)
                elif row == 18 and col == 4:
                    somW -= 1
                    DrawMenu(points)
                elif row == 17 and col == 2:
                    somH += 1
                    DrawMenu(points)
                elif row == 18 and col == 2:
                    somH -= 1
                    DrawMenu(points)
                elif position[0] >= 50 and position[1] >= 50 and position[0] <= 450 and position[1] <= 450:
                    points.append((position[0], position[1]))
                    DrawMenu(points)
    pygame.quit()


        
if __name__ == "__main__":
    main()