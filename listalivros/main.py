import flet as ft
from pathlib import Path
from src.data.database import Database
from src.views.livros_view import LivrosView
from src.views.livro_update_view import LivroUpdateView
from src.views.livro_create_view import LivroCreateView

ROOT_DIR = Path(__file__).parent
DB_NAME = "livro.sqlite3"
DB_FILE: Path = ROOT_DIR / DB_NAME


class App:

    # Método de inicialização com parâmetro page
    def __init__(self, page: ft.Page):
        # Page é o principal Comtainer do FLET
        self.page = page
        # Definição de tema da Page
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Definição de largura da Page
        self.page.window_width = 380
        # Definição de altura da Page
        self.page.window_height = 530
        self.dbs = Database(DB_FILE=DB_FILE)
        # Conectar um manipulador de eventos ao page.on_route_change
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop
        # self.page.go(self.page.route)
        self.page.go("/")

    # ----------------------------------------------------------------------
    ##
    # Rotas para as views
    ##
    def route_change(self, route: ft.RouteChangeEvent):
        troute = ft.TemplateRoute(self.page.route)

        if troute.match("/"):
            self.page.views.clear()
            self.page.views.append(LivrosView(self.page, self.dbs))
        elif troute.match("/livro_create"):
            self.page.views.append(LivroCreateView(self.page, self.dbs))
        elif troute.match("/livro_update/:livro_id"):
            self.page.views.append(
                LivroUpdateView(int(troute.livro_id), self.page, self.dbs)
            )

        elif troute.match("/livros_reload"):
            list_size = len(self.page.views)
            for i in range(list_size):
                if self.page.views[i].route == "/":
                    for _ in range(list_size - i):
                        self.page.views.pop()
                    break

            self.page.views.append(LivrosView(self.page, self.dbs))

        self.page.update()

    def view_pop(self, e):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)


def main(page: ft.Page):
    App(page)


if __name__ == "__main__":
    ft.app(target=main)
