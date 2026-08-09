import sqlite3
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.utils import get_color_from_hex
import datetime

Window.clearcolor = get_color_from_hex("#0A0A0A")

KV = '''
ScreenManager:
    HomeScreen:
    WalletScreen:
    ChatScreen:
    ReelsScreen:
    DatingScreen:
    AIAgentScreen:
    AdminScreen:

<HomeScreen>:
    name: "home"
    BoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "TUMA Super App V23.3"
            md_bg_color: 0.05, 0.05, 0.05, 1
        ScrollView:
            MDList:
                MDCard:
                    size_hint:.9, None
                    height: "120dp"
                    pos_hint: {"center_x":.5}
                    md_bg_color: 0.1, 0.6, 0.3, 1
                    MDLabel:
                        text: "Balance: US$ 0.00 | ZIG 0.00"
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: 1,1,1,1
                        font_size: "20sp"
                MDRaisedButton:
                    text: "Send $5"
                    pos_hint: {"center_x":.5}
                    on_release: app.root.current = "wallet"
                MDRaisedButton:
                    text: "Chat"
                    pos_hint: {"center_x":.5}
                    on_release: app.root.current = "chat"
                MDRaisedButton:
                    text: "Reels"
                    pos_hint: {"center_x":.5}
                    on_release: app.root.current = "reels"
                MDRaisedButton:
                    text: "Dating"
                    pos_hint: {"center_x":.5}
                    on_release: app.root.current = "dating"
                MDRaisedButton:
                    text: "AI Agent"
                    pos_hint: {"center_x":.5}
                    on_release: app.root.current = "aiagent"
                MDRaisedButton:
                    text: "Admin Panel"
                    pos_hint: {"center_x":.5}
                    on_release: app.root.current = "admin"

<WalletScreen>:
    name: "wallet"
    BoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Wallet"
            left_action_items: [["arrow-left", lambda x: app.go_home()]]
        MDLabel:
            text: "Save Money & Send Tips"
            halign: "center"
        MDRaisedButton:
            text: "Tip Creator US$1"
            pos_hint: {"center_x":.5}
        MDRaisedButton:
            text: "Save to Jar"
            pos_hint: {"center_x":.5}

<ChatScreen>:
    name: "chat"
    BoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Chat"
            left_action_items: [["arrow-left", lambda x: app.go_home()]]
        MDLabel:
            text: "TUMA Chat Coming Soon"
            halign: "center"

<ReelsScreen>:
    name: "reels"
    BoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Reels"
            left_action_items: [["arrow-left", lambda x: app.go_home()]]
        MDLabel:
            text: "Short Videos"
            halign: "center"

<DatingScreen>:
    name: "dating"
    BoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "TUMA Dating"
            left_action_items: [["arrow-left", lambda x: app.go_home()]]
        MDLabel:
            text: "Find Matches"
            halign: "center"

<AIAgentScreen>:
    name: "aiagent"
    BoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "TUMA AI Agent"
            left_action_items: [["arrow-left", lambda x: app.go_home()]]
        MDLabel:
            text: "Ask me anything..."
            halign: "center"

<AdminScreen>:
    name: "admin"
    BoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "Admin Panel"
            left_action_items: [["arrow-left", lambda x: app.go_home()]]
        MDLabel:
            text: "Users | Transactions | Reports"
            halign: "center"
'''

class HomeScreen(Screen): pass
class WalletScreen(Screen): pass
class ChatScreen(Screen): pass
class ReelsScreen(Screen): pass
class DatingScreen(Screen): pass
class AIAgentScreen(Screen): pass
class AdminScreen(Screen): pass

class TumaApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        self.init_db()
        return Builder.load_string(KV)

    def go_home(self):
        self.root.current = "home"

    def init_db(self):
        conn = sqlite3.connect('tuma.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, balance_usd REAL, balance_zig REAL)''')
        conn.commit()
        conn.close()

TumaApp().run()
