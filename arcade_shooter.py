import arcade
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Arcade Space Shooter"
SCALING = 2.0
HEALTH_BAR_MAX_WIDTH = 300


class FlyingSprite(arcade.Sprite):
    def update(self):
        super().update()
        if self.right < 0:
            self.remove_from_sprite_lists()


class SpaceShooter(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.paused = False
        self.player = arcade.Sprite("images/space_ship.png", SCALING)
        self.player_health = 300
        self.enemy_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)

        self.player.angle = -90
        self.player.center_y = self.height / 2
        self.player.left = 10
        self.all_sprites.append(self.player)

        arcade.schedule(self.add_enemy, 0.5)
        arcade.schedule(self.add_star, 0.1)

    def on_update(self, delta_time: float):
        if self.paused:
            return

        if self.is_game_over():
            arcade.close_window()

        if self.player.collides_with_list(self.enemy_list):
            self.damage_player(10)
            for sprite in self.player.collides_with_list(self.enemy_list):
                sprite.remove_from_sprite_lists()

        self.all_sprites.update()

        if self.player.top > self.height:
            self.player.top = self.height
        if self.player.right > self.width:
            self.player.right = self.width
        if self.player.bottom < 0:
            self.player.bottom = 0
        if self.player.left < 0:
            self.player.left = 0

    def on_draw(self):
        arcade.start_render()
        self.all_sprites.draw()
        self.draw_health_interface()
        if self.paused:
            arcade.draw_rectangle_filled(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2, 100, 400, arcade.color.WHITE)
            arcade.draw_rectangle_filled(SCREEN_WIDTH / 2 + 100, SCREEN_HEIGHT / 2, 100, 400, arcade.color.WHITE)

    def add_enemy(self, delta_time: float):
        enemy = FlyingSprite("images/missile.png", SCALING)
        enemy.angle = 180
        enemy.left = random.randint(self.width, self.width + 80)
        enemy.top = random.randint(10, self.height - 10)
        enemy.velocity = (random.randint(-20, -5), 0)
        self.enemy_list.append(enemy)
        self.all_sprites.append(enemy)

    def add_star(self, delta_time: float):
        star = FlyingSprite("images/star.png", SCALING)
        star_size = random.randint(5, 30)
        star.width = star_size
        star.height = star_size
        star.left = random.randint(self.width, self.width + 80)
        star.top = random.randint(10, self.height - 10)
        star.velocity = (random.randint(-5, -2), 0)
        self.star_list.append(star)
        self.all_sprites.append(star)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.Q:
            arcade.close_window()
        if symbol == arcade.key.P:
            self.paused = not self.paused
        if symbol == arcade.key.I or symbol == arcade.key.UP:
            self.player.change_y = 5
        if symbol == arcade.key.K or symbol == arcade.key.DOWN:
            self.player.change_y = -5
        if symbol == arcade.key.J or symbol == arcade.key.LEFT:
            self.player.change_x = -5
        if symbol == arcade.key.L or symbol == arcade.key.RIGHT:
            self.player.change_x = 5

    def on_key_release(self, symbol: int, modifiers: int):
        if (symbol == arcade.key.I
                or symbol == arcade.key.K
                or symbol == arcade.key.UP
                or symbol == arcade.key.DOWN
        ):
            self.player.change_y = 0
        if (symbol == arcade.key.J
                or symbol == arcade.key.L
                or symbol == arcade.key.LEFT
                or symbol == arcade.key.RIGHT
        ):
            self.player.change_x = 0

    def damage_player(self, amount: int):
        self.player_health -= amount

    def is_game_over(self):
        return self.player_health <= 0

    def draw_health_interface(self, max_health: float = 100, health_left: float = 100):
        arcade.draw_text('Health', SCREEN_WIDTH - 55, SCREEN_HEIGHT - 20, arcade.color.WHITE, align="right")
        arcade.draw_rectangle_filled(SCREEN_WIDTH - 10 - self.player_health / 2, SCREEN_HEIGHT - 30, self.player_health, 10, arcade.color.RED)


# Main code entry point
if __name__ == "__main__":
    app = SpaceShooter(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    app.setup()
    arcade.run()
