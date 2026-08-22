from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel

class TumaApp(MDApp):
    def build(self):
        return MDScreen(md_bg_color="#FFFFFF", children=[MDLabel(text="TUMA V23.4", halign="center")])

TumaApp().run()