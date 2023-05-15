from functools import partial

import numpy as np
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen


class Menu(Screen):
    game_size = 4

    def __init__(self, game_size=4, **kwargs):
        super().__init__(**kwargs)
        self.game_size = game_size
        self.layout = BoxLayout(orientation='vertical')
        title = Label(text='memory tile game', font_size=48)
        start_button = Button(text='Start', on_press=self.start_game, font_size=48)
        exit_button = Button(text='Exit', on_press=App.get_running_app().stop, font_size=48)

        self.layout.add_widget(title)
        self.layout.add_widget(start_button)
        self.layout.add_widget(exit_button)
        self.add_widget(self.layout)

    def start_game(self, value):
        self.manager.transition.direction = 'left'
        self.manager.current = 'game'


class Tile(Button):

    def __init__(self, tile_color, **kwargs):
        super().__init__(**kwargs)
        self.tile_color = tile_color
        # self.color = [1, 1, 1, 1]
        self.background_normal = ''
        self.background_down = ''
        self.background_disabled_normal = ''


class Game(Screen):
    current_color = None
    before_tile = None
    in_game_tiles = None

    def __init__(self, size, **kwargs):
        super().__init__(**kwargs)
        layout = GridLayout(cols=size, spacing=2)
        self.add_widget(layout)
        empty_tiles_indexes = list(range(size**2))
        tiles = [None for _ in range(size ** 2)]
        for i in range(int((size ** 2) / 2)):
            color = list(np.random.choice(np.arange(0, 1.1, 0.1), size=3))
            color.append(1)
            for _ in range(2):
                index = np.random.choice(empty_tiles_indexes)
                tiles[index] = Tile(tile_color=color, on_press=self.tile_press_show_color)
                self.ids['tile' + str(index)] = tiles[index]
                empty_tiles_indexes.remove(index)
        for tile in tiles:
            layout.add_widget(tile)
        self.in_game_tiles = tiles

    def tile_press_show_color(self, instance):
        instance.background_color = instance.tile_color
        instance.disabled = True
        if self.current_color is not None:
            self.disable_tiles(True)
            Clock.schedule_once(partial(self.check_color, instance, self.before_tile), 1)
        else:
            self.current_color = instance.tile_color
            self.before_tile = instance

    def check_color(self, instance, before_tile, dt):
        self.disable_tiles(False)
        if self.current_color == instance.background_color:
            print('same color')
            instance.disabled = True
            before_tile.disabled = True
            self.in_game_tiles.remove(instance)
            self.in_game_tiles.remove(before_tile)
        else:
            print('different color')
            before_tile.disabled = False
            instance.disabled = False
            instance.background_color = [1, 1, 1, 1]
            before_tile.background_color = [1, 1, 1, 1]
        self.current_color = None
        self.check_win()

    def disable_tiles(self, switch):
        for tile in self.in_game_tiles:
            if switch:
                tile.disabled = True
            else:
                tile.disabled = False

    def check_win(self):
        if len(self.in_game_tiles) == 0:
            layout = GridLayout(cols=1)
            layout.add_widget(Label(text='You win!!!'))
            return_button = Button(text='return to menu')
            layout.add_widget(return_button)
            popup = Popup(title='Congratulations',
                          content=layout,
                          size_hint=(None, None), size=(400, 400))
            popup.bind(on_dismiss=self.return_to_menu)
            return_button.bind(on_press=popup.dismiss)
            popup.open()

    def return_to_menu(self, instance):
        self.manager.transition.direction = 'left'
        self.manager.current = 'menu'


class MyApp(App):

    def build(self):
        sm = ScreenManager()
        menu = Menu(name='menu')
        game = Game(size=4, name='game')
        sm.add_widget(menu)
        sm.add_widget(game)
        sm.current = 'menu'
        return sm


if __name__ == '__main__':
    MyApp().run()
