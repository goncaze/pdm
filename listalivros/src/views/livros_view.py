import flet as ft
from src.modelo.livro import Livro
from src.data.database import Database
from src.data.livro_db import LivroDB


class LivrosView(ft.View):

    def __init__(self, page: ft.Page, dbs: Database):
        super().__init__()
        self.route = "/"
        self.appbar = ft.AppBar(title=ft.Text("Livros registrados"))
        self.page = page
        self.livro_db = LivroDB(dbs)
        self.lw_livros = ft.ListView(
            # Os itens serão organizados verticalmente
            horizontal=False,
            # Um espaçamento para componentes do entorno
            spacing=20,
            # Espessura do divisor entre os itens da ListView
            divider_thickness=2,
            controls=self.carregar_livros(),
        )

        self.floating_action_button = ft.FloatingActionButton(
            icon=ft.icons.ADD,
            on_click=lambda _: self.page.go("/livro_create"),
        )

        self.controls = [
            ft.Column(
                controls=[self.lw_livros],
                scroll=ft.ScrollMode.ALWAYS,
                expand=True,
            )
        ]

    def carregar_livros(self) -> list[ft.Container]:
        lista_containers: list[ft.Container] = []
        for livro in self.livro_db.select_livros():
            txt_livro_titulo = ft.Text(
                spans=[
                    ft.TextSpan(
                        text=livro.titulo,
                        data=livro,
                    )
                ],
                weight=ft.FontWeight.BOLD,
                color=ft.colors.BLUE,
            )
            lista_containers.append(self.add_livro_linha(txt_livro_titulo))
        return lista_containers

    def add_livro_linha(self, txt_livro_titulo: ft.Text) -> ft.Container:
        linha1 = ft.Row(
            controls=[
                txt_livro_titulo,
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.EDIT_DOCUMENT,
                            tooltip="Editar",
                            on_click=self.editar_livro,
                            data=txt_livro_titulo.spans[0].data,
                        ),
                        ft.IconButton(
                            icon=ft.icons.DELETE,
                            on_click=self.deletar_livro,
                            data=txt_livro_titulo.spans[0].data,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        coluna = ft.Column(controls=[linha1], spacing=1)

        container_categorias = ft.Container(
            content=coluna, margin=ft.margin.only(right=15, left=15)
        )

        return container_categorias

    def deletar_livro(self, e: ft.ControlEvent):
        livro: Livro = e.control.data
        self.livro_db.delete_livro(livro)
        self.lw_livros.controls = self.carregar_livros()
        self.lw_livros.update()

    def editar_livro(self, e: ft.ControlEvent):
        livro: Livro = e.control.data
        rota = "/livro_update/" + str(livro.id)
        self.page.go(rota)
