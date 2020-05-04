import math
import numpy as np


def distance_on_unit_sphere(point_1: np.ndarray, point_2: np.ndarray) -> float:
    """
    Calculates Great Circle Distance
    :param point_1: coordinates of point 1 [latitude, longitude]
    :param point_2: coordinates of point 2 [latitude, longitude]
    :return: distance between two points
    """
    # skipping calculations for the same point
    if np.array_equal(point_1, point_2):
        return 0.0

    # Convert latitude and longitude to
    # spherical coordinates in radians.
    degrees_to_radians = math.pi / 180.0

    # phi = 90 - latitude
    phi1 = (90.0 - point_1[0]) * degrees_to_radians
    phi2 = (90.0 - point_2[0]) * degrees_to_radians

    # theta = longitude
    theta1 = point_1[1] * degrees_to_radians
    theta2 = point_2[1] * degrees_to_radians

    cos = (math.sin(phi1) * math.sin(phi2) * math.cos(theta1 - theta2) +
           math.cos(phi1) * math.cos(phi2))

    arc = math.acos(cos) * 6400
    return arc
