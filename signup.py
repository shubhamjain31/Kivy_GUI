from kivymd.app import MDApp
from kivy.lang import Builder
 
 
class SignupApp(MDApp):
    def build(self):
        self.title = 'Sign up'

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('kv_files/signup.kv')

    def save(self):
        self.root.ids.signup_label.text = "User Created"

    
if __name__ == "__main__":
    SignupApp().run()