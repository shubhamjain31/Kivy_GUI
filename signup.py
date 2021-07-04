from kivymd.app import MDApp
from kivy.lang import Builder
import sqlite3

conn = sqlite3.connect('users.db')
 
class SignupApp(MDApp):
    def build(self):
        self.title = 'Sign up'

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('kv_files/signup.kv')

    def save(self):
        username    = self.root.ids.name.text
        email       = self.root.ids.email.text
        mobile      = self.root.ids.mobile.text
        password    = self.root.ids.password.text

        # insert data
        cur = conn.cursor()
        cur.execute("INSERT INTO COMPANY (NAME,EMAIL,MOBILE,PASSWORD) VALUES (?, ?, ?, ? )",(username, email, mobile, password));
        conn.commit()
        cur.close()

        # create message
        self.root.ids.signup_label.text = "User created!"

        # clear fields
        self.root.ids.name.text     = ""
        self.root.ids.email.text    = ""
        self.root.ids.mobile.text   = ""
        self.root.ids.password.text = ""




    
if __name__ == "__main__":
    SignupApp().run()