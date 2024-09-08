import flet as ft

class Cartao(ft.Card):
    
    def __init__(self): 
        super().__init__()
        self.color = ft.colors.AMBER_100
        self.shadow_color = ft.colors.GREEN
        self.surface_tint_color = ft.colors.YELLOW_100
        self.elevation = 8.0
        self.show_border_on_foreground = True
        self.coluna_conteudo = ft.Column()
        self.coluna_botoes = ft.Column()

        self.colunas = ft.Column(
            controls = [None, None]
        )

        self.contentor = ft.Container(
            content = self.colunas,
            padding = ft.padding.all(10)
        )

        self.content = self.contentor

