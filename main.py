from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import Layout
from kivy.core.window import Window


Window.clearColor = (5/255,205/255,55/255,1)

GUI = Builder.load_file("tela1.kv")

class Iservice(App):
    def build(self):
        return GUI


   
Iservice().run()