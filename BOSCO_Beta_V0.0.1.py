from kivy.core.window import Window
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from datetime import datetime
import json

RedVal = 0
GrnVal = 0
BluVal = 0
AlpVal = 0

class timeManager(Widget):
    def on_Rslider_change(self, instance, value):
        global RedVal
        RedVal = value
    def on_Gslider_change(self, instance, value):
        global GrnVal
        GrnVal = value
    def on_Bslider_change(self, instance, value):
        global BluVal
        BluVal = value
    def on_Aslider_change(self, instance, value):
        global AlpVal
        AlpVal = value


class BOSCO_BetaApp(App):
    def build(self):
        self.event = Clock.schedule_interval(self.update_background, 0.1)
        return timeManager()

    def update_background(self, dt):
        global RedVal
        global GrnVal
        global BluVal
        global AlpVal

        Window.clearcolor = RedVal, GrnVal, BluVal, AlpVal


if __name__ == '__main__':
    BOSCO_BetaApp().run()