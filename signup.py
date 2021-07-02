from kivymd.app import MDApp
from kivy.lang import Builder
 
 
class SignupApp(MDApp):
    def build(self):
        self.title = 'Sign up'

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('kv_files/signup.kv')

    def save(self):
        self.root.ids.signup_label.text = f'Sup {self.root.ids.name.text}!'

    def clear(self):
        pass
        # self.root.ids.welcome_label.text = "WELCOME"
        # self.root.ids.user.text = ""
        # self.root.ids.password.text = ""
 
 
if __name__ == "__main__":
    SignupApp().run()