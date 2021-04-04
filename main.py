import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Welcome to Arcade"

# Circle
RADIUS = 150

# Rectangles
RECT_WIDTH = 300
RECT_HEIGHT = 50

# Colors
BLUE = arcade.color.BLUE
BLACK = arcade.color.BLACK
GRAY = arcade.color.GRAY

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

arcade.draw_circle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, RADIUS, BLUE)

arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4, RECT_WIDTH, RECT_HEIGHT, BLACK)
arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4 + SCREEN_HEIGHT / 8, RECT_WIDTH, RECT_HEIGHT, GRAY)
arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + SCREEN_HEIGHT / 8, RECT_WIDTH, RECT_HEIGHT, GRAY)
arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + SCREEN_HEIGHT / 4, RECT_WIDTH, RECT_HEIGHT, BLACK)

arcade.finish_render()
arcade.run()
