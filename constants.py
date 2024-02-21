import pygame as pg
import math
import glm

# Constants

WIN_SIZE = glm.vec2(240, 360)
DICE_SIZE = glm.vec2(WIN_SIZE.x / 2)
BG_COLOR = glm.vec3(4, 135, 143)
BUTTON_COLOR = glm.vec3(255, 255, 255)
BUTTON_SIZE = glm.vec2(20, 10)
BUTTON_POS = (WIN_SIZE.x // 2 - BUTTON_SIZE.x // 2, WIN_SIZE.y - 2 * BUTTON_SIZE.y)
MENU_COLOR = glm.vec3(34, 177, 76)
