from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.screenmanager import Screen

KV = r"""
#:import dp kivy.metrics.dp

<MainButton@Button>:
    size_hint_y: None
    height: dp(52)
    background_normal: ""
    background_color: 0.10, 0.12, 0.18, 1
    color: 0.95, 0.95, 1, 1
    font_size: "16sp"

<NavButton@Button>:
    background_normal: ""
    background_color: 0.07, 0.08, 0.12, 1
    color: 0.75, 0.78, 0.88, 1
    font_size: "12sp"

<GuildScreen>:
    BoxLayout:
        orientation: "vertical"
        canvas.before:
            Color:
                rgba: 0.035, 0.045, 0.075, 1
            Rectangle:
                pos: self.pos
                size: self.size

        ScrollView:
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
                padding: dp(18)
                spacing: dp(14)

                Label:
                    text: "⚔ GUILDVERSE"
                    font_size: "28sp"
                    bold: True
                    color: 0.9, 0.75, 0.25, 1
                    size_hint_y: None
                    height: dp(55)

                Label:
                    text: "NIGHT RAIDERS"
                    font_size: "24sp"
                    bold: True
                    color: 1, 1, 1, 1
                    size_hint_y: None
                    height: dp(42)

                Label:
                    text: "🏰 Guilde niveau 12   •   👥 37 membres   •   🟢 8 en ligne"
                    font_size: "13sp"
                    color: 0.65, 0.7, 0.8, 1
                    size_hint_y: None
                    height: dp(35)

                MainButton:
                    text: "💬  Ouvrir le chat général"
                    on_release: root.manager.current = "chat"

                MainButton:
                    text: "👥  Voir les membres"
                    on_release: root.manager.current = "members"

                MainButton:
                    text: "⚔  Activités & défis"
                    on_release: root.manager.current = "activities"

                MainButton:
                    text: "👤  Mon profil"
                    on_release: root.manager.current = "profile"

                Label:
                    text: "📢 ANNONCE DU MAÎTRE"
                    font_size: "17sp"
                    bold: True
                    color: 0.9, 0.75, 0.25, 1
                    size_hint_y: None
                    height: dp(40)

                Label:
                    text: "Tournoi 1 VS 1 samedi à 20h !\\nInscrivez-vous dans Activités."
                    font_size: "15sp"
                    color: 0.9, 0.9, 0.95, 1
                    text_size: self.width, None
                    size_hint_y: None
                    height: dp(65)

        BoxLayout:
            size_hint_y: None
            height: dp(62)
            NavButton:
                text: "🏰\\nAccueil"
                on_release: root.manager.current = "home"
            NavButton:
                text: "💬\\nChat"
                on_release: root.manager.current = "chat"
            NavButton:
                text: "👥\\nMembres"
                on_release: root.manager.current = "members"
            NavButton:
                text: "👤\\nProfil"
                on_release: root.manager.current = "profile"

<ChatScreen>:
    BoxLayout:
        orientation: "vertical"
        padding: dp(14)
        spacing: dp(10)
        canvas.before:
            Color:
                rgba: 0.035, 0.045, 0.075, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: "💬 CHAT DE LA GUILDE"
            font_size: "23sp"
            bold: True
            color: 0.9, 0.75, 0.25, 1
            size_hint_y: None
            height: dp(48)

        ScrollView:
            id: messages_scroll
            do_scroll_x: False
            Label:
                id: messages
                text: root.messages
                font_size: "15sp"
                color: 0.92, 0.92, 0.97, 1
                text_size: self.width, None
                halign: "left"
                valign: "top"
                size_hint_y: None
                height: self.texture_size[1] + dp(20)
                padding: dp(8), dp(8)

        BoxLayout:
            size_hint_y: None
            height: dp(52)
            spacing: dp(8)
            TextInput:
                id: message_input
                hint_text: "Écrire un message..."
                multiline: False
                on_text_validate: root.send_message()
            Button:
                text: "➤"
                size_hint_x: None
                width: dp(58)
                on_release: root.send_message()

        MainButton:
            text: "← Retour à l'accueil"
            on_release: root.manager.current = "home"

<MembersScreen>:
    BoxLayout:
        orientation: "vertical"
        padding: dp(18)
        spacing: dp(12)
        canvas.before:
            Color:
                rgba: 0.035, 0.045, 0.075, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: "👥 MEMBRES"
            font_size: "25sp"
            bold: True
            color: 0.9, 0.75, 0.25, 1
            size_hint_y: None
            height: dp(50)
        Label:
            text: "👑 LordYami     Maître     •  2450 XP\\n🛡 ShadowFox    Officier   •  1840 XP\\n⚔ DarkKnight    Vétéran   •  1320 XP\\n🔥 Akuma        Élite      •   980 XP\\n🌙 Genki        Membre     •   420 XP"
            font_size: "16sp"
            color: 0.92, 0.92, 0.97, 1
            text_size: self.width, None
            valign: "top"
        Widget:
        MainButton:
            text: "← Accueil"
            on_release: root.manager.current = "home"

<ActivitiesScreen>:
    BoxLayout:
        orientation: "vertical"
        padding: dp(18)
        spacing: dp(12)
        canvas.before:
            Color:
                rgba: 0.035, 0.045, 0.075, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: "⚔ ACTIVITÉS"
            font_size: "25sp"
            bold: True
            color: 0.9, 0.75, 0.25, 1
            size_hint_y: None
            height: dp(50)
        MainButton:
            text: "🥊  Tournoi 1 VS 1\\nSamedi — 20h"
        MainButton:
            text: "🏆  Défi XP de la semaine\\nObjectif : 500 XP"
        MainButton:
            text: "⚔  Guerre de guilde\\nBientôt disponible"
        Widget:
        MainButton:
            text: "← Accueil"
            on_release: root.manager.current = "home"

<ProfileScreen>:
    BoxLayout:
        orientation: "vertical"
        padding: dp(18)
        spacing: dp(12)
        canvas.before:
            Color:
                rgba: 0.035, 0.045, 0.075, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: "👤 MON PROFIL"
            font_size: "25sp"
            bold: True
            color: 0.9, 0.75, 0.25, 1
            size_hint_y: None
            height: dp(50)
        Label:
            text: "⚔\\nLordYami\\n\\nRang : Maître\\nNiveau : 18\\nXP : 2450\\nRéputation : 97"
            font_size: "19sp"
            color: 0.95, 0.95, 1, 1
            halign: "center"
            valign: "middle"
        MainButton:
            text: "← Accueil"
            on_release: root.manager.current = "home"

ScreenManager:
    GuildScreen:
        name: "home"
    ChatScreen:
        name: "chat"
    MembersScreen:
        name: "members"
    ActivitiesScreen:
        name: "activities"
    ProfileScreen:
        name: "profile"
"""

class GuildScreen(Screen):
    pass

class ChatScreen(Screen):
    messages = StringProperty(
        "[b]🛡 ShadowFox[/b] : Bienvenue à tous !\n\n"
        "[b]⚔ DarkKnight[/b] : Le tournoi est confirmé ?\n\n"
        "[b]👑 Maître[/b] : Oui, samedi à 20h 🔥\n\n"
        "[b]🔥 Akuma[/b] : Je serai présent !\n\n"
    )

    def send_message(self):
        field = self.ids.message_input
        msg = field.text.strip()
        if not msg:
            return
        self.messages += f"[b]👤 Moi[/b] : {msg}\n\n"
        field.text = ""

class MembersScreen(Screen):
    pass

class ActivitiesScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class GuildVerseApp(App):
    title = "GuildVerse"

    def build(self):
        return Builder.load_string(KV)

if __name__ == "__main__":
    GuildVerseApp().run()
