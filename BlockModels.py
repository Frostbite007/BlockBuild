class Block:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.speed = 5
 
    def animate(self, delta):
        if self.x + 75 > 500:
            self.speed = self.speed * -1
        if self.x - 75 < 0:
            self.speed = self.speed * -1
        self.x += self.speed

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.block = Block(self, 250, 590)
 
    def animate(self, delta):
        self.block.animate(delta)
