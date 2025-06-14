import pygame
import pymunk
import pymunk.pygame_util
from objects import create_boundaries, create_ball, creating_environment, create_domino, create_stick, create_pendulum
from typing import Tuple, Any, Dict

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
    "mass": 8,
    "radius": 11.5
}

catapult_ball = {
    "friction": 0.4,
    "elasticity": 0.75,
    "mass": 7,
    "radius": 12
}

wood_object = {
    "friction": 0.4,
    "elasticity": 0.5,
    "radius": 5,
    "color": (101, 67, 33, 255)
}

red_stick = {
    "mass": 5,
    "friction": 0.4,
    "elasticity": 0.5,
    "radius": 5,
    "color": (200, 50, 50, 255),
    "position": [(300, 430), (400, 290)]
}

blue_stick = {
    "mass": 0.1,
    "friction": 0.4,
    "elasticity": 0.5,
    "radius": 5,
    "color": (100, 100, 255, 255)
}

first_pendulum = {
    "anchor_pos": (410, 245),
    "pendulum_mass": {
        "mass": 0.5,
        "radius": 10,
        "pos": (410, 290)
    },
    "rope": {
        "pos": [(0, 0), (0, -15)],
        "radius": 1.5
    }
}

DOMINO_PROPERTIES = {
    "num_dominoes": 12,
    "width": 10,
    "height": 45,
    "mass": 0.5,
    "friction": 0.4,
    "elasticity": 0.4,
    "spacing_factor": 0.4,
    "start_x": 415
}

def draw_fixed_stick(space: pymunk.Space, stick_object: Dict[str, Any], pivot_pos: Tuple[float, float]):
    stick_body = create_stick(space, stick_object["position"][0], stick_object["position"][1], stick_object["mass"], stick_object["radius"], stick_object["friction"], stick_object["elasticity"], stick_object["color"])

    pivot_joint = pivot_pos
    pivot = pymunk.PivotJoint(space.static_body, stick_body, pivot_joint)
    space.add(pivot)

def create_dominoes(space: pymunk.Space) -> None:
    """
    Crea una fila de dominós en el espacio físico.

    :param space: Espacio físico de Pymunk.
    """
    properties = DOMINO_PROPERTIES
    cumulative_x = properties["start_x"]
    last_half_width = properties["width"] / 2

    for _ in range(properties["num_dominoes"]):
        current_half_width = properties["width"] / 2
        current_spacing = properties["height"] * properties["spacing_factor"]
        x_pos = cumulative_x + last_half_width + current_spacing + current_half_width

        create_domino(
            x_pos,
            316,
            properties["width"],
            properties["height"],
            properties["mass"],
            properties["friction"],
            properties["elasticity"],
            space,
        )

        cumulative_x = x_pos
        last_half_width = current_half_width

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
    creating_environment(space, wood_object)

    create_ball(space, (110,80), primary_ball["mass"], primary_ball["radius"], primary_ball["friction"], primary_ball["elasticity"])
    create_ball(space, (80,80), primary_ball["mass"], primary_ball["radius"], primary_ball["friction"], primary_ball["elasticity"])
    create_ball(space, (50,80), primary_ball["mass"], primary_ball["radius"], primary_ball["friction"], primary_ball["elasticity"])
    create_ball(space, (15,80), primary_ball["mass"], primary_ball["radius"], primary_ball["friction"], primary_ball["elasticity"])
    
    #Activated ball
    create_ball(space, (792, 307), 15, 6, 0.4, 0.75)
    create_ball(space, (757, 427), catapult_ball["mass"], catapult_ball["radius"], catapult_ball["friction"], catapult_ball["elasticity"])

    draw_fixed_stick(space, red_stick, (330, 395))
    create_dominoes(space)

    create_pendulum(space, first_pendulum)
    
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
                if event.button == 1:
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