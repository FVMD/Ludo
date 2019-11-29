import arcade
import os

sprite_scaling = 1.5
sprite_count = 20

screen_width = 700
screen_height = 700
screen_title = "Test"

move_speed = 5

sprites = ["blue_sprite.png", "red_sprite.png", "blue_sprite.png", "red_sprite.png"]


class Piece(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.angle += self.change_angle

        if self.left < 0:
            self.left = 0
        elif self.right > screen_width - 1:
            self.right = screen_width - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > screen_height - 1:
            self.top = screen_height - 1


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.background = None

        self.player_list = None

        self.player_sprite = None

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):

        self.background = arcade.load_texture(".\\Ludo4.png")

        self.player_list = arcade.SpriteList()

        self.player_sprite = Piece("C:\\Users\\Gina\\PycharmProjects\\sprite_test.py\\blue_sprite.png", sprite_scaling)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        pos_x = 100
        pos_y = 100
        count = 0
        #for i in range(int(sprite_count / 4)):

        if count == 0:

            inner_count = 0

            for k in range(4):
                sprite = arcade.Sprite(("C:\\Users\\Gina\\PycharmProjects\\sprite_test.py\\" + sprites[k]), sprite_scaling)

                sprite.center_x = pos_x
                sprite.center_y = pos_y

                if k == 0:
                    pos_y += 75
                elif k == 1:
                    pos_x += 75
                elif k == 2:
                    pos_y -= 75

                self.player_list.append(sprite)

    def on_draw(self):

        arcade.start_render()

        arcade.draw_texture_rectangle(screen_width // 2, screen_height // 2,
                                      screen_width, screen_height, self.background)

        self.player_list.draw()

    def on_update(self, delta_time):

        self.player_list.update()

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.player_sprite.change_y = move_speed
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -move_speed
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -move_speed
            # self.player_sprite.change_angle = 45
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = move_speed
            # self.player_sprite.change_angle = 5

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
            # self.player_sprite.change_angle = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
            # self.player_sprite.change_angle = 0


def main():
    window = MyGame(screen_width, screen_height, screen_title)
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()
