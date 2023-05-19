import pygame
import math

class MouseHandler():
    mouse_duration_count = 0
    def __init__(self):
        pass

    def increment_counter(self):
        self.mouse_duration_count += 1

    def mouse_angle(self, mouse_player, player_cords):
        angle = math.atan2((mouse_player[1]-player_cords[1]), mouse_player[0]-player_cords[0])  # Calculate the angle in radians
        angle_degrees = math.degrees(angle)  # Convert the angle to degrees

        return angle_degrees

