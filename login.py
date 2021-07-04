from kivymd.app import MDApp
from kivy.lang import Builder
import sqlite3
 
 
class LoginApp(MDApp):
    def build(self):
        self.title = 'Login'

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('kv_files/login.kv')

    def logger(self):

        username    = self.root.ids.user.text
        password    = self.root.ids.password.text

        # add database
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        statement = f"SELECT * from COMPANY WHERE NAME='{username}' AND PASSWORD = '{password}';"
        cur.execute(statement)
        if not cur.fetchone():  # An empty result evaluates to False.
            self.root.ids.welcome_label.text = f'Login failed !'
        else:
            self.root.ids.welcome_label.text = f'Welcome !'
        conn.close()

    def clear(self):
        self.root.ids.welcome_label.text = "LOGIN"
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""
 
 
if __name__ == "__main__":
    LoginApp().run()