from kivymd.app import MDApp
from kivy.lang import Builder
import sqlite3

conn = sqlite3.connect('users.db')
 
class AddApp(MDApp):
    def build(self):
        self.title = 'Add Employee'

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return Builder.load_file('kv_files/emp_add.kv')

    def save(self):
        name        = self.root.ids.name.text
        email       = self.root.ids.email.text
        mobile      = self.root.ids.mobile.text
        age         = self.root.ids.age.text
        address     = self.root.ids.address.text
        male_gender = self.root.ids.chk_male
        female_gender    = self.root.ids.chk_female
        date             = self.root.ids.date.text

        if male_gender.active:
            gender = 'Male'
        elif female_gender.active:
            gender = 'Female'
        else:
            gender = 'No gender selected'

        # # insert data
        cur = conn.cursor()
        cur.execute("INSERT INTO EMPLOYEE (NAME, EMAIL, MOBILE, AGE, ADDRESS, GENDER, JOINING_DATE) VALUES (?, ?, ?, ?, ?, ?, ?)",(name, email, mobile, age, address, gender, date));
        conn.commit()
        cur.close()

        # create message
        self.root.ids.add_label.text = "Employee Added!"

        # clear fields
        self.root.ids.name.text             = ""
        self.root.ids.email.text            = ""
        self.root.ids.mobile.text           = ""
        self.root.ids.age.text              = ""
        self.root.ids.address.text          = ""
        self.root.ids.date.text             = ""




    
if __name__ == "__main__":
    AddApp().run()