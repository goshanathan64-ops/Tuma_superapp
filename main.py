from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem

KV = '''
MDScreen:
    MDBottomNavigation:
        panel_color: "#0066FF"
        text_color_active: "white"
        text_color_normal: "#B3D1FF"
        
        MDBottomNavigationItem:
            name: 'home'
            text: 'Home'
            icon: 'home'
            MDLabel:
                text: 'TUMA Super App V23.3'
                halign: 'center'
                font_style: 'H3'
        
        MDBottomNavigationItem:
            name: 'wallet'
            text: 'Wallet'
            icon: 'wallet'
            MDLabel:
                text: 'Wallet Coming Soon'
                halign: 'center'
                font_style: 'H3'
        
        MDBottomNavigationItem:
            name: 'profile'
            text: 'Profile'
            icon: 'account'
            MDLabel:
                text: 'Profile Coming Soon'
                halign: 'center'
                font_style: 'H3'
'''

class TumaApp(MDApp):
    def build(self):
        self.title = "TUMA"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

if __name__ == '__main__':
    TumaApp().run()