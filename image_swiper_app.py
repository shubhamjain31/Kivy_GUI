from kivymd.app import MDApp
from kivy.lang import Builder
 
 
class MainApp(MDApp):
    
    def build(self):
        self.title = 'Image Swiper'
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('kv_files/swiper.kv')
 
 
MainApp().run()