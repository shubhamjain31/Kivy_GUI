from kivymd.app import MDApp
from kivy.lang import Builder
 
 
class LoginApp(MDApp):
    def build(self):
        self.title = 'Login'

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('kv_files/login.kv')

    def logger(self):
        self.root.ids.welcome_label.text = f'Sup {self.root.ids.user.text}!'

    def clear(self):
        self.root.ids.welcome_label.text = "LOGIN"
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""
 
 
if __name__ == "__main__":
    LoginApp().run()