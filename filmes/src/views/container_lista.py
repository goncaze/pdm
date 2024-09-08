import flet as ft

class ContainerLista(ft.Container):
    def __init__(self):
        super().__init__()
        self.lista = ft.ListView(auto_scroll = True, expand = True)
        self.expand = True
        self.content = self.lista
        # self.update()

        # """
        #     ADVERTÊNCIA!
        #     Segue a configuração do tema que permite 
        #     ocultar a barra de rolagem da ListView.
        # """
        # self.theme=ft.Theme(
        #     scrollbar_theme=ft.ScrollbarTheme(
        #         thumb_visibility = False,
        #         track_visibility = False,
        #         interactive = False,
        #         thumb_color=ft.colors.TRANSPARENT,
        #     )
        # )
       