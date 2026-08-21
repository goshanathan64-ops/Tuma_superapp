from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
MDScreen:
    MDLabel:
        text: 'TUMA Super App V23.3'
        halign: 'center'
        font_style: 'H3'
'''

class TumaApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

TumaApp().run()