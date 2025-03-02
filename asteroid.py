from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    

    def draw(self, x, y, radius):
        pygame.draw.circle(screen, "white", (self.x, self.y), width = 2)

    def update(self, dt):
        self.position += self.velocity * dt