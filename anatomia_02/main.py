import flet as ft


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    page.window_height = 600
    page.window_width = 350
    page.add(ft.Text("Tema de cor clara!"))


ft.app(main)
