import pygame
import sys
import config # Import the config Module
import random
import shapes


def init_game():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constanst from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True


def draw_text(screen, text,font,text_col,x,y):
    image = font.render(text,True,text_col)
    screen.blit(image,(x,y))

def draw_rectangle(screen, color, x, y, width, height):
    pygame.draw.rect(screen,color,x,y,width,height)

def main():
    screen = init_game()
    running = True
    clock = pygame.time.Clock() # Initialize the clock her
    
    text_font = pygame.font.SysFont('Arial', 30, bold = False, italic = False)

    while running:
        running = handle_events()
        screen.fill(config.WHITE) # Use color from config
        
        draw_text(screen, "hello", text_font, config.BLUE, 500,500 )
        pygame.display.flip()

        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS) # use the clock to control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()