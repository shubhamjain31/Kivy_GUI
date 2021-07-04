from kivymd.app import MDApp
from kivy.lang import Builder
from subprocess import Popen, PIPE
 
class MainApp(MDApp):
    def build(self):
        self.title = 'Home'

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('kv_files/main.kv')

    def createAccount(self):
        MainApp().get_running_app().stop() # close the current window
        process = Popen(['python3', 'signup.py'], stdout=PIPE, stderr=PIPE)

    def login(self):
        MainApp().get_running_app().stop()
        process = Popen(['python3', 'login.py'], stdout=PIPE, stderr=PIPE)

    
if __name__ == "__main__":
    MainApp().run()