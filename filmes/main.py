import flet as ft
from src.views.lista_cartoes import ListaCartoes
from src.views.formulario import Formulario
from pathlib import Path
from src.data.database import Database
from src.data.filmes_db import FilmeDB

ROOT_DIR = Path(__file__).parent
DB_NAME = "filme.sqlite3"
DB_FILE: Path = ROOT_DIR / DB_NAME

class App:

    def __init__(self, page: ft.Page):
        self.page = page
        self.page.theme_mode = ft.ThemeMode.LIGHT      
        # Código para FLET 0.22.1
        self.page.window_width = 340
        self.page.window_height = 610      
        # Código para FLET 0.23.2
        # self.page.window.width = 340
        # self.page.window.height = 610
        self.dbs = Database(DB_FILE=DB_FILE)
        self.filme_db = FilmeDB(self.dbs)
        # Conectar um manipulador de eventos ao page.on_route_change
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop
        self.page.go("/")

    def route_change(self, route: ft.RouteChangeEvent):

        troute = ft.TemplateRoute(self.page.route)

        if troute.match("/"):
            self.page.views.clear()
            self.page.views.append(
                ListaCartoes(
                    page=self.page, 
                    filme_db=self.filme_db,
                    rota="/", 
                    titulo_appbar="Minha lista de filmes"
                )
            )
            
        elif troute.match("/formulario"):
            self.page.views.clear()
            self.page.views.append(
                Formulario(
                    page=self.page, 
                    filme_db=self.filme_db
                )
            )
            
        elif troute.match("/formulario/:id"):
            self.page.views.clear()
            self.page.views.append(
                Formulario(
                    page=self.page, 
                    filme_db=self.filme_db,
                    filme_id=troute.id
                )
            )            

        elif self.page.route == "/reload":
            self.page.views.clear()            
            self.page.go("/")

        self.page.update()


    def view_pop(self, e):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)
        self.page.update()


def main(page: ft.Page):
    App(page)


if __name__ == "__main__":
    ft.app(target=main)