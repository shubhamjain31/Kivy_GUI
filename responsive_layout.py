from kivy.app import App
from kivy.lang import Builder
from kivy.properties import OptionProperty
from kivy.core.window import Window
from kivy.factory import Factory


KV = '''
#:import A kivy.animation.Animation
<RLabel@Label>:
    font_size:
        (
        sp(20) if app.media in ('XS', 'S') else
        sp(40)
        )

FloatLayout:
    BoxLayout:
        orientation: 'vertical'
        pos_hint: {'center_x': .5}
        padding: dp(20)
        size_hint_x: 1 if app.media in ('XS', 'S') else None
        width: dp(300) if app.media in ('XS', 'S') else dp(500) if app.media in ('M', 'L') else dp(800)

        Header:
        Content:
        Footer:
    Menu:

<Menu@BoxLayout>:
    orientation: 'vertical'
    size_hint: None, None
    pos_hint: {'top': 1}
    height: self.minimum_height
    width: 100 if app.media in ('XS', 'S') else 200
    toggle: app.media in ('XS', 'S', 'M')
    hidden: self.toggle and show.state == 'normal'
    hidden_ratio: 1
    x: -(self.width - show.width) * (self.hidden_ratio or 0)

    on_hidden:
        A.cancel_all(self, 'x')
        A(hidden_ratio=1 if self.hidden else 0, t='out_quad', d=.3).start(self)

    MenuToggleButton:
        id: show
        size_hint_y: None if root.toggle else 0
        size_hint_x: None
        opacity: 1 if root.toggle else 0
        pos_hint: {'right': 1}
        text: 'M'
        width: dp(20)

    MenuButton:
        text: 'test'
    MenuButton:
        text: 'test'
    MenuButton:
        text: 'test'
    MenuButton:
        text: 'test'
    MenuButton:
        text: 'test'

<MenuButton@Button,MenuToggleButton@ToggleButton>:
    size_hint_y: None
    height:
        (
        dp(20) if app.media in ('XS', 'S') else
        dp(30) if app.media in ('M', 'L') else
        dp(40)
        )
    font_size:
        (
        sp(20) if app.media in ('XS', 'S') else
        sp(40)
        )

<Header@Label>:
    text: 'Hello world'
    size_hint_y: None
    height: self.texture_size[1]
    font_size:
        (
        sp(40) if app.media in ('XS', 'S') else
        sp(80)
        )

<Content@BoxLayout>:
    ScrollView:
        RLabel:
            text: 'text ' * 100
            text_size: self.width, None
            size_hint_y: None
            height: self.texture_size[1]

<Footer@BoxLayout>:
    RLabel:
        text: app.media
'''


class ResponsiveApp(App):
    media = OptionProperty('M', options=('XS', 'S', 'M', 'L', 'XL'))

    def build(self):
        Window.bind(size=self.update_media)
        return Builder.load_string(KV)

    def update_media(self, win, size):
        width, height = size
        self.media = (
            'XS' if width < 250 else
            'S' if width < 500 else
            'M' if width < 1000 else
            'L' if width < 1200 else
            'XL'
        )

if __name__ == "__main__":
    ResponsiveApp().run()