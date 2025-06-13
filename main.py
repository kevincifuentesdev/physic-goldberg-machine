import pygame
import pymunk
import pymunk.pygame_util
from objects import create_boundaries, create_ball, creating_environment

# Screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60

# Pymunk constants
GRAVITY = (0, 981)
TIME_STEP = 1/FPS
DAMPING = 0.99

# Pymunk Shapes
primary_ball = {
    "friction": 0.4,
    "elasticity": 0.75,
    "mass": 0.10,
    "radius": 11.5
}

wood_segment = {
    "friction": 0.4,
    "elasticity": 0.5,
    "radius": 5,
    "color": (101, 67, 33, 255)
}

def main():
    # Pygame initialization
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simulación de Máquina de Goldberg con Pymunk")
    clock = pygame.time.Clock()

    # Pymunk space initialization
    space = pymunk.Space()
    space.gravity = GRAVITY
    space.damping = DAMPING
    
    # Drawing Objects
    create_boundaries(space)
    creating_environment(space, wood_segment)
    
    # Pymunk draw options
    draw_options = pymunk.pygame_util.DrawOptions(screen)

    # Font for messages
    font = pygame.font.Font(None, 36)
    text_surface = font.render("Presione la tecla ESC para salir de la simulación.", True, pygame.Color("black"))
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, 20))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 1 is for left mouse button
                    print(f"Left mouse click at: {event.pos}")
                if event.button == 3:
                    create_ball(space, event.pos, primary_ball["mass"], primary_ball["radius"], primary_ball["friction"], primary_ball["elasticity"])

        # Clear screen
        screen.fill(pygame.Color("white"))

        # Draw Pymunk space
        space.debug_draw(draw_options)

        # Display message
        screen.blit(text_surface, text_rect)

        # Update Pymunk space
        space.step(TIME_STEP)

        for body in space.bodies:
            if body.body_type == pymunk.Body.DYNAMIC:
                body.angular_velocity *= 0.99

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

        

    pygame.quit()

if __name__ == "__main__":
    main()