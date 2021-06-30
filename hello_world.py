from kivy.app import App
from kivy.uix.label import Label
 
 
class SimpleApp(App):
    def build(self):
        self.title = 'Hello world'
        l = Label(text="Hello World !", font_size=120)
        return l
 
 
if __name__ == "__main__":
    SimpleApp().run()