from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem

KV = '''
MDScreen:
    MDBottomNavigation:
        panel_color: "#0066FF"
        text_color_active: "white"
        
        MDBottomNavigationItem:
            name: 'home'
            text: 'Home'
            icon: 'home'
            MDLabel:
                text: 'TUMA Super App V23.3'
                halign: 'center'
                font_style: 'H3'  # CHANGED FROM H4
'''

class TumaApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

TumaApp().run()