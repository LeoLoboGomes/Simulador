import pygame
from SimulatorModules import *


pygame.init()
surface_height = 500
surface_width = 240
main_surface = pygame.display.set_mode((surface_width, surface_height))
clock = pygame.time.Clock()
list = ["Arsenal", "Liverpool", "Chelsea"]
box_list = []
y = 30
for name in list:
    Box = SelectBox(70, y, 100, name)
    box_list.append(Box)
    y += 20
Next_Button = Button(130, 430, 100, 40, 34, 13, "Next")
main_surface.fill((33, 94, 33))
Next_Button.draw(main_surface)
done = False
while not done:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            done = True
            break
        for Box in box_list:
            Box.handle_event(ev)
        done = Next_Button.handle_event(ev, main_surface)
    for Box in box_list:
        Box.draw(main_surface)
    pygame.display.flip()
pygame.quit()
