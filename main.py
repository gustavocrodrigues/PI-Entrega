from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import Layout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty


class MainWin(Screen):
    pass


class Cliente(Screen):
    nome = ObjectProperty(None)
    email = ObjectProperty(None)
    tel = ObjectProperty(None)

    def btn(self):
        print("Nome: ", self.nome.text, "Email: ", self.email.text, "Tel: ", self.tel.text)


class Prestador(Screen):
    empresa = ObjectProperty(None)
    cnpj = ObjectProperty(None)
    servico = ObjectProperty(None)

    def btn(self):
        print("Nome: ", self.empresa.text, "Email: ", self.cnpj.text, "Tel: ", self.servico.text)


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('iservice.kv')


class Iservice(App):
    def build(self):
        return kv


Iservice().run()