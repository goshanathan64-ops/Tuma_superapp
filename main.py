from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel

class TumaApp(MDApp):
    def build(self):
        self.title = "TUMA V23.3"
        self.theme_cls.primary_palette = "Blue"
        screen = MDScreen()
        screen.add_widget(
            MDLabel(text="TUMA Super App V23.3", halign="center", font_style="H3")
        )
        return screen

TumaApp().run()