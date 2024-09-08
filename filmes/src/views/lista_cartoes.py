import flet as ft
from src.views.container_lista import ContainerLista
from src.views.cartao_filme import CartaoFilme
from src.data.filmes_db import FilmeDB

class ListaCartoes(ft.View):

    def __init__(self, page: ft.Page, filme_db: FilmeDB, rota: str, titulo_appbar: str):
        super().__init__()        
        self.page = page
        self.filme_db = filme_db        
        self.route = rota
        self.appbar = ft.AppBar(title=ft.Text(value=titulo_appbar))        
        self.lista: ContainerLista = self.carregar_filmes()
        self.controls.append(self.lista)

        self.floating_action_button = ft.FloatingActionButton(
            icon=ft.icons.ADD,
            on_click=lambda _: self.page.go("/formulario"),
        )



    def carregar_filmes(self) -> list[ft.Container]:
        lista_containers = ContainerLista()

        for filme in self.filme_db.select_filmes():

            new_card = CartaoFilme(self.page, self.filme_db)

            new_card.content.content.controls[0] = ft.Column(
                controls = [
                    ft.Text(filme.titulo, theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                    ft.Text(filme.genero, theme_style=ft.TextThemeStyle.BODY_LARGE),
                    ft.Text(filme.lancamento, theme_style=ft.TextThemeStyle.BODY_LARGE),
                ]            
            )
            new_card.data = filme

            lista_containers.content.controls.append(new_card)
        return lista_containers