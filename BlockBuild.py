import arcade
import arcade.key

from BlockModels import Block,World
 
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
GAME_RUNNING = 1
GAME_OVER = 2

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
 
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
 
    def draw(self):
        self.sync_with_model()
        super().draw()
 
class BlockBuilder(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.BLACK)

        self.world = World(width, height)
        
        self.block_sprites = []
        for block in self.world.blocks:
            self.block_sprites.append(ModelSprite('images/block.png',model = block))
         
    def on_draw(self):
        arcade.start_render()
        for sprite in self.block_sprites:
            sprite.draw()

        arcade.draw_text(str(self.world.score),
                         self.width - 30, self.height - 30,
                         arcade.color.WHITE, 20) 

    def animate(self, delta):
        self.world.animate(delta)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)
                
if __name__ == '__main__':
    window = BlockBuilder(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
