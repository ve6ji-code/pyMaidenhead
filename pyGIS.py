import math


def deg2rad(deg):
    """Convert degrees to radians"""
    rad = deg * (math.pi/180.0)
    return rad


def rad2deg(rad):
    """Convert radians to degrees"""
    deg = rad * (180.0/math.pi)
    return deg
