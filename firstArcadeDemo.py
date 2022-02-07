import arcade

def main():
    arcade.open_window(500, 400, "first window ever")
    arcade.set_background_color(arcade.color.LIGHT_DEEP_PINK)
    block = arcade.create_rectangle(200, 200, 100, 200, arcade.color.BULGARIAN_ROSE)
    arcade.start_render()
    block.draw()
    arcade.draw_text("We got something up", 300, 300, arcade.color.FELDSPAR, 18)
    arcade.finish_render()
    arcade.run()

main()