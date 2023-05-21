import pygame
import math

class MouseHandler():
    mouse_duration_count = 0
    mouse_down = False
    def __init__(self):
        pass
        

    def increment_counter(self):
        self.mouse_duration_count += 1

    def mouse_angle(self, mouse_player, player_cords):
        angle = math.atan2((mouse_player[1]-player_cords.y), mouse_player[0]-player_cords.x)  # Calculate the angle in radians
        angle_degrees = math.degrees(angle)  # Convert the angle to degrees
        return angle_degrees
    
    def click_duration(self):
        duration = self.mouse_duration_count
        self.mouse_duration_count = 0
        return duration

    def handleClicks(self,event,player):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            angle = self.mouse_angle(pygame.mouse.get_pos(), player.position)
            click_duration = self.click_duration()
            player.fire(angle, click_duration)
            self.mouse_down = False

        if self.mouse_down:
            self.increment_counter()

