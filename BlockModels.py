import arcade.key

class Model:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def hit(self, other, height):
        return  (((self.x + 75 < other.x + 75) and (self.x + 75 > other.x - 75)) or ((self.x - 75 < other.x + 75) and (self.x - 75 > other.x - 75))) and self.y - height <= 12

class Block(Model):
    def __init__(self, world, x, y, old_height):
        super().__init__(world, x, y)
        
        self.old_height = old_height
        self.speed = 5
        self.down_speed = 10
        self.move_down = False

 
    def animate(self, delta):
        if self.x + 75 > 500:
            self.speed = self.speed * -1
        if self.x - 75 < 0:
            self.speed = self.speed * -1
        if self.y - 10 < self.old_height:
            self.down_speed = 0
            self.y = self.old_height + 10

        self.x += self.speed
        
        if self.move_down:
            self.speed = 0
            self.y -= self.down_speed

class World:
    NUM_BLOCK = 29
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.old_height = 0
        self.i = 0
        self.score = 0
        self.blocks = []
        for i in range(World.NUM_BLOCK):
            block = Block(self, width / 2, height - 10, i * 20)
            self.blocks.append(block)

    def animate(self, delta):
        for block in self.blocks:
            block.animate(delta)

        if self.blocks[self.i].y - 10 < self.old_height:
            self.i += 1

        if self.blocks[self.i].hit(self.blocks[self.i - 1], self.old_height):
            self.score -= 1
        else:
            self.score += 0
            

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.blocks[self.i].move_down = True
            self.old_height +=20
