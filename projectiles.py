import pygame 
import math
from Vector import Vector

class Projectile():

    def deflect(self,xPosition1,xPosition2,yPosition1,yPosition2,xSpeed1,xSpeed2,ySpeed1,ySpeed2):

        # // The position and speed of each of the two balls in the x and y axis before collision.
        # // YOU NEED TO FILL THESE VALUES IN AS APPROPRIATE...
        # double xPosition1, xPosition2, yPosition1, yPosition2
        # double xSpeed1, xSpeed2, ySpeed1, ySpeed2
        # // Calculate initial momentum of the balls... We assume unit mass here.
        p1InitialMomentum = math.sqrt(xSpeed1 * xSpeed1 + ySpeed1 * ySpeed1)
        p2InitialMomentum = math.sqrt(xSpeed2 * xSpeed2 + ySpeed2 * ySpeed2)
        # // calculate motion vectors
        p1Trajectory = [xSpeed1, ySpeed1]
        p2Trajectory = [xSpeed2, ySpeed2]
        # // Calculate Impact Vector
        impactVector = [xPosition2 - xPosition1, yPosition2 - yPosition1]
        impactVectorNorm = self.normalizeVector(impactVector)
        # // Calculate scalar product of each trajectory and impact vector
        p1dotImpact = abs(p1Trajectory[0] * impactVectorNorm[0] + p1Trajectory[1] * impactVectorNorm[1])
        p2dotImpact = abs(p2Trajectory[0] * impactVectorNorm[0] + p2Trajectory[1] * impactVectorNorm[1])
        # // Calculate the deflection vectors - the amount of energy transferred from one ball to the other in each axis
        p1Deflect = [ -impactVectorNorm[0] * p2dotImpact, -impactVectorNorm[1] * p2dotImpact ]
        p2Deflect = [ impactVectorNorm[0] * p1dotImpact, impactVectorNorm[1] * p1dotImpact ]
        # // Calculate the final trajectories
        p1FinalTrajectory = [p1Trajectory[0] + p1Deflect[0] - p2Deflect[0], p1Trajectory[1] + p1Deflect[1] - p2Deflect[1]]
        p2FinalTrajectory = [p2Trajectory[0] + p2Deflect[0] - p1Deflect[0], p2Trajectory[1] + p2Deflect[1] - p1Deflect[1]]
        # // Calculate the final energy in the system.
        p1FinalMomentum = math.sqrt(p1FinalTrajectory[0] * p1FinalTrajectory[0] + p1FinalTrajectory[1] * p1FinalTrajectory[1])
        p2FinalMomentum = math.sqrt(p2FinalTrajectory[0] * p2FinalTrajectory[0] + p2FinalTrajectory[1] * p2FinalTrajectory[1])
        # // Scale the resultant trajectories if we've accidentally broken the laws of physics.
        if (p1FinalMomentum + p2FinalMomentum) != 0:
            mag = ((p1InitialMomentum + p2InitialMomentum) / (p1FinalMomentum + p2FinalMomentum))*0.9
        else:
            mag = ((p1InitialMomentum + p2InitialMomentum) / ((p1FinalMomentum + p2FinalMomentum)+0.01))*0.9
        # // Calculate the final x and y speed settings for the two balls after collision.
        xSpeed1 = p1FinalTrajectory[0] * mag
        ySpeed1 = p1FinalTrajectory[1] * mag
        xSpeed2 = p2FinalTrajectory[0] * mag
        ySpeed2 = p2FinalTrajectory[1] * mag
        
        self.velocity.x = xSpeed1
        self.velocity.y = ySpeed1
        #
        # Converts a vector into a unit vector.
        # Used by the deflect() method to calculate the resultant direction after a collision.
        #
    def normalizeVector(self,vec):
        mag = 0.0
        dimensions = len(vec)
        result = [None]*dimensions
        for i in range(0,dimensions):
            mag += vec[i] * vec[i]
            mag = math.sqrt(mag)
                
            if (mag == 0.0):
                result[0] = 1.0
                for i in range(1,dimensions):
                    result[i] = 0.0
            else:
                for i in range(0,dimensions):
                    result[i] = vec[i] / mag
            
        return result
            

    def checkCollision(self):
        
        #tiles = self.background.getTilesAround(self.coordinates)
        tiles = self.background.getTileArray()
        for tile in tiles:
            if tile.rect.colliderect(pygame.Rect(self.position.x,self.position.y,self.radius,self.radius)):
                self.draw()
                previousPosition = pygame.Vector2(self.position.x - self.velocity.x, self.position.y - self.velocity.y)
            
                # Check if the ball is bouncing off the bottom or the side of the rect
                if self.position.y - self.radius < tile.rect.bottom and previousPosition.y - self.radius >= tile.rect.bottom:
                    # Ball is bouncing off the bottom of the rect
                    self.deflect(self.position.x,tile.rect.center[0],self.position.y,tile.rect.center[1],self.velocity.x,self.velocity.x,self.velocity.y,0-self.velocity.y)
                else:
                    # Ball is bouncing off the side of the rect
                    self.deflect(self.position.x,tile.rect.center[0],self.position.y,tile.rect.center[1],self.velocity.x,0-self.velocity.x,self.velocity.y,self.velocity.y)
                
                self.background.addLight(self.position.x-self.radius,self.position.y-self.radius,100,200-(self.bounces*20))
                self.bounces+=1
                

    def update(self):
        # self.previousPosition = self.position    
        self.position.x += (self.velocity.x/2)
        self.position.y += (self.velocity.y/2)
        self.checkCollision()
        # self.previousPosition = self.position
        self.position.x += (self.velocity.x/2)
        self.position.y += (self.velocity.y/2)
        self.coordinates = Vector(int(self.position.x/self.background.tileSize),round(self.position.y/self.background.tileSize))
        self.checkCollision()   
        if((self.velocity.x<3 and self.velocity.x>-3 )and (self.velocity.y<3 and self.velocity.y>-3)):
            return True
        return False

    def draw(self):
        # pygame.draw.circle(self.screen,"white",(self.position.x,self.position.y),self.radius)
        color = (255, 255, 255)  # White color (you can customize this)
        radius = self.radius # Radius of the arc
        arc_angle = 90  # Angle of the arc (in degrees)
        bend_angle = 45  # Angle by which the arc is bent (in degrees)
        width = 1  # Line width of the arc (in pixels)

        start_angle = math.radians(bend_angle)  # Convert bend angle to radians
        end_angle = start_angle + math.radians(arc_angle)  # Calculate end angle

        # Calculate the position of the arc's center
        center_x = self.position.x + radius * math.cos(start_angle)
        center_y = self.position.y - radius * math.sin(start_angle)
        center = (int(center_x), int(center_y))

        pygame.draw.arc(self.screen, color, (center_x - radius, center_y - radius, radius * 2, radius * 2), start_angle, end_angle, width)

        

    def __init__(self, x, y,xVelocity,yVelocity,background,screen):
        self.position = pygame.Vector2(x,y)
        self.previousPosition = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(xVelocity,yVelocity)
        self.projectileRectangle = pygame.Rect(x, y, 3, 6)
        self.background = background
        self.screen = screen
        self.bounces=0
        self.radius=5
    