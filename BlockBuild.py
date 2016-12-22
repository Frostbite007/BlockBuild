import arcade

from BlockModels import Block,World
 
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
 
class BlockBuilder(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.BLACK)

        self.block_sprite = arcade.Sprite('images/block.png')

        self.world = World(width, height) 
         
    def on_draw(self):
        arcade.start_render()
        self.block_sprite.draw()

    def animate(self, delta):
        self.world.animate(delta)
        
        self.block_sprite.set_position(self.world.block.x, self.world.block.y)
        
if __name__ == '__main__':
    window = BlockBuilder(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
