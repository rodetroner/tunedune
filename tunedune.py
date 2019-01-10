import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

kivy.require('1.10.1')

Builder.load_file('sidebar.kv')

class LoginScreen(Screen):
    def clearLogin(self, instance, *args):
        if self.login_input.text == 'Username':
            self.login_input.text = ''
    def clearPassword(self, instance, *args):
        if self.password_input.text == 'Password':
            self.password_input.text = ''
            self.password_input.password = True

class MainScreen(Screen):
    pass


class TuneDuneApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login_scr'))
        sm.add_widget(MainScreen(name='main_scr'))
        return sm

if __name__ == '__main__':
    TuneDuneApp().run()
