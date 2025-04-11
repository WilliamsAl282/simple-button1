import pygame
import sys
import config # Import the config Module
from config import *
import random
import shapes


def init_game():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constanst from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events(button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True


def draw_text(screen, text,font,text_col,x,y):
    image = font.render(text,True,text_col)
    screen.blit(image,(x,y))

def draw_rectangle(screen, color, x, y, width, height):
    pygame.draw.rect(screen,color,x,y,width,height)

def draw_circle(screen,x,y,radius,color,thickness):
    pygame.draw.circle(screen,color,(x,y),radius, thickness)

def main():
    screen = init_game()
    running = True
    clock = pygame.time.Clock() # Initialize the clock her
    
    text_font = pygame.font.SysFont('Arial', 40, bold = True)
    surf = text_font.render('Quit', True, GREEN)

    button_length = 200
    button_width = 60
    button_x = 300
    button_y = 125
    button = pygame.Rect(button_x,button_y,button_length,button_width)

    surf_rect = surf.get_rect()
    surf_rect.center = button.center

    


    while running:
        running = handle_events(button)
        screen.fill(config.WHITE) # Use color from config

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if button.collidepoint(mouse_x, mouse_y):
            button_color = (180, 180, 180)
        else:
            button_color = (110,110,110)

            pygame.draw.rect(screen, button_color, button)

            screen.blit(surf, surf_rect)


        circle_color = config.RED

        draw_circle(screen,535,520, 40, circle_color, 0)
        draw_text(screen, "button", text_font, config.BLACK, 500,500)

         
        
        pygame.display.flip()

        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS) # use the clock to control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()