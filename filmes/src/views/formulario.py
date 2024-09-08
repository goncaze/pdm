import flet as ft
from src.data.filmes_db import FilmeDB
from src.views.card_create_update import CardCreateUpdate


class Formulario(ft.View):

    def __init__(self, page: ft.Page, filme_db: FilmeDB, filme_id:str = '0'):
        super().__init__()
        self.route = "/formulario"
        self.page: ft.Page = page
        self.filme_db: FilmeDB = filme_db
        self.filme_id:int = int(filme_id)
        self.formulario = CardCreateUpdate(self.page, self.filme_db, self.filme_id)
        self.controls.append(self.formulario)
        self.appbar = ft.AppBar(title=ft.Text(value="Filme"))
