import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class Player(Widget):
    pass

class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def on_touch_down(self, touch):
        if touch.x < self.width/2:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width/2:
            self.player2.center_y = touch.y

    def serve_ball(self):
        self.ball.center = self.center
        self.ball.velocity = Vector(6, 0).rotate(randint(0, 369))
    
    def update(self, dt):
        self.ball.move()
         # collition
        if self.ball.collide_widget(self.player1) or self.ball.collide_widget(self.player2):
            self.ball.velocity_y *= -1
            self.ball.velocity_x *= -1

        # bounce off top and botton
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1
        # bounce off left and right
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1


class PongApp(App):

    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    PongApp().run()