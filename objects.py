import pymunk
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

def creating_environment(space: pymunk.Space, object_type: Dict[str, Any]):
    create_segment(space, (6, 70), (223, 120), object_type["radius"], object_type["friction"], object_type["elasticity"], object_type["color"])
    create_segment(space, (223, 120), (433, 120), object_type["radius"], object_type["friction"], object_type["elasticity"], object_type["color"])
