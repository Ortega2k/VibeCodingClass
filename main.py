print("Hello, World!")


a = 10
b = 20

def add(a, b):
    return a + b

result = add(a, b)
print("The sum is:", result)

import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('My Pygame Window')
