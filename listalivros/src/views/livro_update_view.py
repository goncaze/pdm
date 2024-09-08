import flet as ft
from src.modelo.livro import Livro
from src.data.database import Database
from src.data.livro_db import LivroDB


class LivroUpdateView(ft.View):

    def __init__(self, livro_id: int, page: ft.Page, dbs: Database):
        super().__init__()
        self.route = "/livro_update"
        self.page: ft.Page = page
        self.livroDB: LivroDB = LivroDB(dbs)
        self.appbar = ft.AppBar(title=ft.Text(value="Editar livro"))

        self.livro: Livro = self.livroDB.select_livro(livro_id)

        self.ttf_livro_titulo = ft.TextField(
            value=self.livro.titulo,
            label="Título",
            hint_text="Título",
        )

        self.btn_registrar = ft.ElevatedButton(text="Salvar", on_click=self.registrar)

        self.btn_limpar_formulario = ft.ElevatedButton(
            text="Limpar", on_click=self.limpar_formulario
        )

        self.formulario_categoria_create = ft.Column(
            controls=[
                self.ttf_livro_titulo,
                ft.Container(margin=ft.margin.all(5)),
                ft.Row(
                    controls=[
                        self.btn_limpar_formulario,
                        self.btn_registrar,
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
            ]
        )

        self.controls = [
            ft.Container(margin=ft.margin.only(top=10)),
            self.formulario_categoria_create,
        ]

    def limpar_formulario(self, e: ft.ControlEvent):
        self.ttf_livro_titulo.value = None
        self.page.update()

    def validar(self) -> bool:
        is_valido: bool = True
        if self.ttf_livro_titulo.value == "":
            is_valido = False
            self.ttf_livro_titulo.error_text = "Informe o título."
        return is_valido

    def registrar(self, e):
        if self.validar():
            self.livro.titulo = self.ttf_livro_titulo.value
            self.livroDB.update_livro(self.livro)
            self.page.go("/livros_reload")
        else:
            self.page.update()
