import pymunk
import json
from typing import Tuple, Dict, Any


def create_boundaries(space: pymunk.Space):
    # Left boundary
    left_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    left_shape = pymunk.Segment(left_body, (0, 38), (0, 690), 5)
    left_shape.elasticity = 0.8
    left_shape.friction = 0.5
    space.add(left_body, left_shape)

    # Right boundary
    right_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    right_shape = pymunk.Segment(right_body, (1353, 38), (1353, 690), 5)
    right_shape.elasticity = 0.8
    right_shape.friction = 0.5
    space.add(right_body, right_shape)

    # Top boundary
    top_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    top_shape = pymunk.Segment(top_body, (0, 38), (1353, 38), 5)
    top_shape.elasticity = 0.8
    top_shape.friction = 0.5
    space.add(top_body, top_shape)

    # Bottom boundary
    bottom_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    bottom_shape = pymunk.Segment(bottom_body, (0, 690), (1353, 690), 5)
    bottom_shape.elasticity = 0.4
    bottom_shape.friction = 0.5
    space.add(bottom_body, bottom_shape)

def create_ball(space: pymunk.Space, position: Tuple[int, int], mass: float, radius: float, friction: float, elasticity: float):
    ball_body = pymunk.Body()
    ball_shape = pymunk.Circle(ball_body, radius)

    ball_body.position = position
    ball_shape.friction = friction
    ball_shape.elasticity = elasticity
    ball_shape.mass = mass

    ball_shape.color = (248, 196, 113, 255)

    space.add(ball_body, ball_shape)

def create_segment(space: pymunk.Space, initial: Tuple[float, float], final: Tuple[float, float], radius: float, friction: float, elasticity: float, color: Tuple[int, int, int, int] = (0,0,0,0)):
    segment_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    segment_shape = pymunk.Segment(segment_body, initial, final, radius)

    segment_shape.friction = friction
    segment_shape.elasticity = elasticity
    segment_shape.color = color

    space.add(segment_body, segment_shape)

def create_stick(space: pymunk.Space, initial: Tuple[float, float], final: Tuple[float, float], mass: float, radius: float, friction: float, elasticity: float, color: Tuple[int, int, int, int] = (0,0,0,0)):
    stick_body = pymunk.Body()
    stick_shape = pymunk.Segment(stick_body, initial, final, radius)

    stick_shape.color = color
    stick_shape.mass = mass
    stick_shape.friction = friction
    stick_shape.elasticity = elasticity

    space.add(stick_body, stick_shape)

    return stick_body

# Hole
def load_holes_from_json(path: str) -> list[Dict[str, Any]]:
    with open(path, "r") as f:
        holes_data = json.load(f)
    return holes_data

def create_all_holes(space: pymunk.Space, holes_data: list[Dict[str, Any]]):
    for hole_data in holes_data:
        create_hole_segment(space, hole_data)

def create_hole_segment(space: pymunk.Space, object_hole: Dict[str, Any]):
    #Left wall
    create_segment(space, object_hole["left_wall"][0], object_hole["left_wall"][1], object_hole["radius"], object_hole["friction"], object_hole["elasticity"], object_hole["color"])
    
    # Right wall
    create_segment(space, object_hole["right_wall"][0], object_hole["right_wall"][1], object_hole["radius"], object_hole["friction"], object_hole["elasticity"], object_hole["color"])
    
    # Bottom
    create_segment(space, object_hole["bottom"][0], object_hole["bottom"][1], object_hole["radius"], object_hole["friction"], object_hole["elasticity"], object_hole["color"])

def create_lever(
    space: pymunk.Space,
    start: Tuple[float, float],
    end: Tuple[float, float],
    thickness: float = 10,
    mass: float = 1.0
) -> None:
    length = end[0] - start[0]
    pivot_x = (start[0] + end[0]) / 2
    pivot_y = (start[1] + end[1]) / 2

    pivot_body = pymunk.Body(body_type=pymunk.Body.STATIC)
    pivot_body.position = (pivot_x, pivot_y)

    moment = pymunk.moment_for_box(mass, (length, thickness))
    lever_body = pymunk.Body(mass, moment)
    lever_body.position = (pivot_x, pivot_y)
    lever_shape = pymunk.Poly.create_box(lever_body, (length, thickness))
    lever_shape.friction = 0.5
    lever_shape.elasticity = 0.2

    pivot_joint = pymunk.PivotJoint(pivot_body, lever_body, (pivot_x, pivot_y))

    space.add(pivot_body, lever_body, lever_shape, pivot_joint)

def create_domino(
    pos_x: float,
    pos_y: float,
    width: float,
    height: float,
    mass: float,
    friction: float,
    elasticity: float,
    space: pymunk.Space
) -> Tuple[pymunk.Body, pymunk.Shape]:
    """
    Crea un dominó en el espacio físico.

    Esta función fue tomada de **ettskd** (Usuario de Github) y adaptada para este proyecto.

    Fuente original: [python-domino Repository](https://github.com/ettskd/python-domino/blob/main/domino.py)

    :param pos_x: Posición en X del dominó.
    :param pos_y: Posición en Y del dominó.
    :param width: Ancho del dominó.
    :param height: Alto del dominó.
    :param mass: Masa del dominó.
    :param friction: Fricción del dominó.
    :param elasticity: Elasticidad del dominó.
    :param space: Espacio físico de Pymunk.
    :return: El cuerpo y la forma del dominó creados.
    """
    body = pymunk.Body(mass, pymunk.moment_for_box(mass, (width, height)))
    body.position = (pos_x, pos_y)
    shape = pymunk.Poly.create_box(body, (width, height))
    shape.friction = friction
    shape.elasticity = elasticity
    shape.collision_type = 1
    space.add(body, shape)
    return body, shape

def creating_environment(space: pymunk.Space, object_type: Dict[str, Any]):
    create_segment(space, (7, 92), (221, 100), object_type["radius"], object_type["friction"], object_type["elasticity"], object_type["color"])
    create_segment(space, (255, 105), (497, 122), object_type["radius"], object_type["friction"], object_type["elasticity"], object_type["color"])
    create_segment(space, (529, 134), (1116, 155), object_type["radius"], object_type["friction"], object_type["elasticity"], object_type["color"])
    create_segment(space, (1173, 186), (941, 203), object_type["radius"], object_type["friction"], object_type["elasticity"], object_type["color"])
    create_segment(space, (1176, 186), (1184, 164), object_type["radius"], object_type["friction"], object_type["elasticity"], object_type["color"])
    create_segment(space, (905, 215), (133, 259), object_type["radius"], object_type["friction"], object_type["elasticity"], object_type["color"])

    create_segment(space, (5, 309), (190, 400), object_type["radius"], object_type["friction"], object_type["elasticity"], object_type["color"])

    create_segment(space, (5, 450), (609, 450), object_type["radius"], object_type["friction"], object_type["elasticity"], object_type["color"])
    create_segment(space, (610, 450), (610, 420), object_type["radius"], object_type["friction"], object_type["elasticity"], object_type["color"])

    create_segment(space, (393, 323), (799, 323), object_type["radius"], object_type["friction"], object_type["elasticity"], object_type["color"])
    

    # Load and create all holes from holes.json
    holes_data = load_holes_from_json("holes.json")
    create_all_holes(space, holes_data)

