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
                font_style: 'H4'
                
        MDBottomNavigationItem:
            name: 'wallet'
            text: 'Wallet'
            icon: 'wallet'
            MDLabel:
                text: 'Send Money, Pay Bills, EcoCash'
                halign: 'center'
                
        MDBottomNavigationItem:
            name: 'chat'
            text: 'Chat'
            icon: 'chat'
            MDLabel:
                text: 'TUMA Chat + Dating'
                halign: 'center'
                
        MDBottomNavigationItem:
            name: 'reels'
            text: 'Reels'
            icon: 'video'
            MDLabel:
                text: 'TUMA Reels'
                halign: 'center'
'''

class TumaApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Amber" # Gold accent
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

TumaApp().run()