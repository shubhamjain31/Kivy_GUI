from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
import sqlite3

conn = sqlite3.connect('users.db')

class ShowApp(MDApp):
    def build(self):
        self.title = 'Show Employee'

        cursor = conn.execute("SELECT * from Employee")
        rows = cursor.fetchall()

        all_data = []
        for row in rows:
	        all_data.append(row)

        conn.close()
        # print([list(x) + ['+'] for x in all_data])


        screen = Screen()
        table = MDDataTable(
        	size_hint = (0.9, 0.6),
            pos_hint = {"center_x":0.5, "center_y":0.5},
            # check = True,
            use_pagination = True,
            rows_num = 3,
            pagination_menu_height = '240dp',
            pagination_menu_pos = 'auto',		# or center
        	column_data = [
        	("Sr No.", dp(19)),
        	("Name", dp(19)),
        	("Email", dp(19)),
        	("Mobile", dp(19)),
        	("Age", dp(19)),
        	("Address", dp(19)),
        	("Gender", dp(19)),
        	("Join Date", dp(19))],

        	row_data = all_data)
        
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        # return Builder.load_file('kv_files/emp_add.kv')

        screen.add_widget(table)
        return screen

if __name__ == "__main__":
    ShowApp().run()