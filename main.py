
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar

KV = '''
MDScreen:
    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "TUMA Super App V23.3"
            elevation: 4
            md_bg_color: 0, 0.3, 0.7, 1
            right_action_items: [["qr-code-scanner", lambda x: app.show_snack("QR Scanner")]]

        MDBottomNavigation:
            id: bottom_nav
            panel_color: 0.05, 0.05, 0.05, 1
            text_color_active: 0, 0.5, 1, 1

            MDBottomNavigationItem:
                name: "home"
                text: "Home"
                icon: "home"
                MDScrollView:
                    MDBoxLayout:
                        orientation: "vertical"
                        padding: 12
                        spacing: 12
                        adaptive_height: True
                        MDCard:
                            orientation: "vertical"
                            padding: 12
                            spacing: 8
                            size_hint_y: None
                            height: 120
                            md_bg_color: 0.1, 0.1, 0.2, 1
                            radius: [16]
                            MDLabel:
                                text: "Welcome back, CEO"
                                font_style: "H6"
                            MDLabel:
                                text: "Level 12 | 2,450 TUMA Points"
                                theme_text_color: "Secondary"
                            MDLabel:
                                text: "Balance: $125.50 USD | 3,200 ZWL | 540 T-Coin"
                                theme_text_color: "Primary"
                        MDLabel:
                            text: "Quick Actions"
                            font_style: "Subtitle1"
                        MDGridLayout:
                            cols: 3
                            spacing: 10
                            size_hint_y: None
                            height: 100
                            MDRaisedButton:
                                text: "Send Money"
                                on_release: app.show_snack("Send Money")
                            MDRaisedButton:
                                text: "Buy Airtime"
                                on_release: app.show_snack("Buy Airtime")
                            MDRaisedButton:
                                text: "Scan QR"
                                on_release: app.show_snack("QR Scanner")

            MDBottomNavigationItem:
                name: "wallet"
                text: "Wallet"
                icon: "wallet"
                MDList:
                    TwoLineListItem:
                        text: "TUMA Balance"
                        secondary_text: "$125.50 USD | 3,200 ZWL"
                    TwoLineListItem:
                        text: "Send / Receive"
                        secondary_text: "Phone number or QR"
                    TwoLineListItem:
                        text: "Buy Airtime & Data"
                        secondary_text: "Econet, NetOne, Telecel"

            MDBottomNavigationItem:
                name: "chat"
                text: "Chat"
                icon: "chat"
                MDLabel:
                    text: "TUMA Chat - E2E Encrypted"
                    halign: "center"

            MDBottomNavigationItem:
                name: "reels"
                text: "Reels"
                icon: "video"
                MDLabel:
                    text: "TUMA Reels - Creator Fund"
                    halign: "center"

            MDBottomNavigationItem:
                name: "dating"
                text: "Dating"
                icon: "heart"
                MDLabel:
                    text: "TUMA Dating - Verified + Safe"
                    halign: "center"

            MDBottomNavigationItem:
                name: "ai"
                text: "AI"
                icon: "robot"
                MDLabel:
                    text: "TUMA AI Agent"
                    halign: "center"

            MDBottomNavigationItem:
                name: "admin"
                text: "Admin"
                icon: "shield-account"
                MDList:
                    TwoLineListItem:
                        text: "Analytics"
                        secondary_text: "Views, Wallet, Followers"
                    TwoLineListItem:
                        text: "Withdraw"
                        secondary_text: "Cash out to Bank/EcoCash"
'''

class TumaApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.title = "TUMA V23.3"
        return Builder.load_string(KV)

    def show_snack(self, message):
        Snackbar(text=message, duration=1.5).open()

if __name__ == "__main__":
    TumaApp().run()