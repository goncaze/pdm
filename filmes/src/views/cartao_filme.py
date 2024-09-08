import flet as ft
from src.views.cartao import Cartao
from src.data.filmes_db import FilmeDB

class CartaoFilme(Cartao):
    
    def __init__(self, page: ft.Page, filme_db: FilmeDB): 
        super().__init__()
        self.page = page
        self.filme_db = filme_db

        self.icb_editar = ft.IconButton(
            icon=ft.icons.UPDATE,
            icon_color="blue",
            icon_size=25,
            tooltip="Update record",
            on_click=self.editar
        )

        self.icb_excluir = ft.IconButton(
            icon=ft.icons.DELETE_FOREVER_ROUNDED,
            icon_color="pink600",
            icon_size=25,
            tooltip="Delete record",
            on_click=self.excluir
        )

        self.linha_botoes = ft.Row(
            controls=[
                self.icb_editar,
                self.icb_excluir
            ],
            alignment=ft.MainAxisAlignment.END
        )

        self.content.content.controls[1] = self.linha_botoes


    def excluir(self, e):
        self.filme_db.delete_filme(self.data)
        self.page.go("/reload")  


    def editar(self, e):
        self.page.go(f"/formulario/{self.data.id}")          