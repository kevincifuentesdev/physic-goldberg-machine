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

def creating_environment(space: pymunk.Space, object_type: Dict[str, Any]):
    create_segment(space, (7, 92), (221, 100), object_type["radius"], object_type["friction"], object_type["elasticity"], object_type["color"])
    create_segment(space, (255, 105), (497, 122), object_type["radius"], object_type["friction"], object_type["elasticity"], object_type["color"])
    create_segment(space, (529, 134), (1116, 155), object_type["radius"], object_type["friction"], object_type["elasticity"], object_type["color"])
    create_segment(space, (1173, 186), (941, 203), object_type["radius"], object_type["friction"], object_type["elasticity"], object_type["color"])
    create_segment(space, (1176, 186), (1184, 164), object_type["radius"], object_type["friction"], object_type["elasticity"], object_type["color"])
    create_segment(space, (905, 215), (133, 259), object_type["radius"], object_type["friction"], object_type["elasticity"], object_type["color"])

    # Load and create all holes from holes.json
    holes_data = load_holes_from_json("holes.json")
    create_all_holes(space, holes_data)
