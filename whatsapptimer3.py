from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.uix.button import Button
# from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder

# from kivy.core.window import Window

from kivymd.uix.label import MDLabel

import time
from datetime import datetime

import emoji

from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.dialog import MDDialog

username_helper = """
MDTextField:
   hint_text:" WhatsApp Number"
   helper_text:"+947xxxxxxxx"
   helper_text_mode:"persistent"
   icon_right:"whatsapp"
   icon_right_color:app.theme_cls.primary_color   #mekenthamai thirane wenne patA
   pos_hint:{'center_x':0.5,'center_y':0.67}
   size_hint_x:None
   font_size:26

   width:600
"""
massage = """
MDTextField:
   hint_text:"Type Massege"
   icon_right:"pencil"
   icon_right_color:app.theme_cls.primary_color   #mekenthamai thirane wenne patA
   pos_hint:{'center_x':0.5,'center_y':0.52}
   size_hint_x:None
   font_size:26
   width:600

"""
hour1 = """
MDTextField:
   hint_text:"Time(hour)"
   helper_text:"In just 24 hours"
   icon_right:"hours-24"
   icon_right_color:app.theme_cls.primary_color   #mekenthamai thirane wenne patA
   pos_hint:{'center_x':0.5,'center_y':0.4}
   size_hint_x:None
   font_size:29
   width:220
"""
minute1 = """
MDTextField:
   hint_text:"Time(minutes)"
   icon_right_color:app.theme_cls.primary_color   #mekenthamai thirane wenne patA
   pos_hint:{'center_x':0.5,'center_y':0.26}
   size_hint_x:None
   font_size:29
   width:220
"""


class DemoApp(MDApp):

    def build(self):
        # Window.size = [220, 440]
        screen = Screen()
        self.theme_cls.primary_palette="Green"
        self.toolbar = MDToolbar(title="WhatsAppTimer")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [
            ["send-clock", lambda x: self.show_data(object)]]

        self.theme_cls.primary_palette = "Red"  # methani thamaimpata maru karanne
        # username = MDTextField(text='Enter number',pos_hint={'center_x':0.5,'center_y':0.5},
        #                       size_hint=(0.5,1))
        button = MDRectangleFlatButton(text='SEND MESSAGE', pos_hint={'center_x': 0.5, 'center_y': 0.15},
                                       on_release=self.show_data)
        self.username = Builder.load_string(username_helper)
        self.message = Builder.load_string(massage)

        self.hour = Builder.load_string(hour1)
        self.minute = Builder.load_string(minute1)
        self.label = MDLabel(
            text="Sending a message on time",
            font_style='H6',
            halign="center",
            size_hint=(0.8, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.81},
            theme_text_color="Secondary"

        )
        self.label.right_action_items = [
            ["send-clock", lambda x: self.show_data(object)]]

        screen.add_widget(self.toolbar)
        screen.add_widget(self.message)
        screen.add_widget(self.username)
        screen.add_widget(self.hour)
        screen.add_widget(self.minute)
        screen.add_widget(button)
        screen.add_widget(self.label)

        return screen

    def show_data(self, obj):
        # 1 mulinma balanawa internet thiyenawada kiyala
        # 2 internet naththan deweni adirayen thamai apita kivy window display karanne

        var = self.username.text.count('')  # akuru ganana labaganima
        print(var)
        if self.username.text is "":

            check_string = 'Please enter WhatsApp number'
            close_button = MDFlatButton(text='close',
                                        on_release=self.close_dialog)  # bttonsadima dialog box sadaha
            more_button = MDFlatButton(text='More')
            self.dialog = MDDialog(title='Your Misstech...!', text=check_string,
                                   size_hint=(0.7, 1),
                                   buttons=[close_button])
            self.dialog.open()
            print(5)
            start = True
        elif var != 13:

            check_string = ' Please check your phone number '
            close_button = MDFlatButton(text='close',
                                        on_release=self.close_dialog)  # bttonsadima dialog box sadaha
            more_button = MDFlatButton(text='More')
            self.dialog = MDDialog(title='Your Misstech...!', text=check_string,
                                   size_hint=(0.7, 1),
                                   buttons=[close_button])
            self.dialog.open()

        elif self.hour.text is "":
            check_string = ' Please enter time in hour '
            close_button = MDFlatButton(text='close',
                                        on_release=self.close_dialog)  # bttonsadima dialog box sadaha
            more_button = MDFlatButton(text='More')
            self.dialog = MDDialog(title='Your Misstech...!', text=check_string,
                                   size_hint=(0.7, 1),
                                   buttons=[close_button])
            self.dialog.open()
            start = True





        elif self.minute.text is "":
            check_string = ' Please enter time in minute '
            close_button = MDFlatButton(text='close',
                                        on_release=self.close_dialog)  # bttonsadima dialog box sadaha
            more_button = MDFlatButton(text='More')
            self.dialog = MDDialog(title='Your Misstech...!', text=check_string,
                                   size_hint=(0.7, 1),
                                   buttons=[close_button])
            self.dialog.open()
            start = True

        else:
            try:
                import pywhatkit
                sithmi = 0
                print(self.username.text)
                print(self.message.text)
                print(sithmi)
                name1 = int(self.hour.text)
                name2 = int(self.minute.text)
                pywhatkit.sendwhatmsg(self.username.text, self.message.text, name1, name2)
                check_string = f'{self.username.text}Your message was sent to WhatsApp number'
                close_button = MDFlatButton(text='close',
                                            on_release=self.close_dialog)  # bttonsadima dialog box sadaha
                self.dialog = MDDialog(title='User name', text=check_string, size_hint=(0.7, 1),
                                       buttons=[close_button])
                self.dialog.open()
                print("rr")
                start = True

            except:
                check_string = 'Plece active your internet connection'
                close_button = MDFlatButton(text='close',
                                            on_release=self.close_dialog)

                self.dialog = MDDialog(title='Plece active your internet connection', text=check_string,
                                       size_hint=(0.7, 1), buttons=[close_button])
                self.dialog.open()
                print(12)
                close_button = MDFlatButton(text='close',
                                            on_release=self.close_dialog)

                self.dialog = MDDialog(title='Plece active your internet connection', text=check_string,
                                       size_hint=(0.7, 1), buttons=[close_button])

                check_string = 'Plece active your internet connection'

                send_button = MDFlatButton(text='SEND',
                                           on_release=self.show_data)

                self.dialog = MDDialog(title='Plece active your internet connection', text=check_string,
                                       size_hint=(0.7, 1), buttons=[send_button])

                self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


DemoApp().run()