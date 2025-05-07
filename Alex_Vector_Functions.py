import pygame
import sys
import numpy as np
import random
import itertools
import math

#useful vector functions
def unit_vector(vector):
    norm = np.linalg.norm(vector)
    if norm != 0: return vector/norm
    else: return 0 * vector

#projects x onto y
def projection(x, y):
    return y * np.dot(x, y) / np.dot(y, y)

#returns the magnitude of a vector
def magnitude(vector):
    return np.linalg.norm(vector)

#returns components of x tangent and normal to y
def components(x, y):
    x_tangent = projection(x, y)
    x_normal = x - projection(x, y)
    return x_tangent, x_normal

#returns the angle a vector is pointing in
def get_angle(vector):
    if vector[0] > 0: return math.atan(vector[1]/vector[0])
    elif vector[0] < 0: return math.atan(vector[1]/vector[0]) + math.pi
    elif vector[0] == 0 and vector[1] > 0: return math.pi/2
    elif vector[0] == 0 and vector[1] < 0: return -1*math.pi/2
    else: return 0

def rotate_vector(vector, theta): #2d vectors
    vector = np.array(vector, dtype = float)
    c, s = np.cos(theta), np.sin(theta)
    R = np.array([[c, -s], [s, c]], dtype = float)
    return np.dot(R, vector)

def cross_product(x, y):
    return np.cross(x, y)

if __name__ == "__main__":
    print(rotate_vector((0, 1), .125*math.pi))
    print(cross_product(np.array([2, 3], dtype = float), np.array([4, 4], dtype = float)))