import flet as ft
from src.modelo.filme import Filme
from src.data.filmes_db import FilmeDB

class CardCreateUpdate(ft.Card):
    def __init__(self, page:ft.Page, filme_db: FilmeDB, filme_id:int):
        super().__init__()
        self.page = page
        self.filme_db = filme_db
        self.filme_id = filme_id

        self.ttf_titulo = ft.TextField(label="Título", value="")    
        self.ttf_genero = ft.TextField(label="Gênero", value="")
        self.ttf_lancamento = ft.TextField(label="Lançamento", value="")
        self.carregar_dados_filme()

        self.ttb_salvar = ft.TextButton(text="Salvar", on_click=self.salvar)

        self.linha_ttb = ft.Row(
            controls=[
                self.ttb_salvar,
            ],
            alignment=ft.MainAxisAlignment.END
        )

        self.content = ft.Column(
            controls = [
                self.ttf_titulo,
                self.ttf_genero,
                self.ttf_lancamento,
                self.linha_ttb,
            ]
        )

    def limpar_formulario(self):
        self.ttf_titulo.value = ""
        self.ttf_genero.value = ""
        self.ttf_lancamento.value = ""
        self.update()

    def validar(self) -> bool:
        is_valido: bool = True
        if self.ttf_titulo.value == "":
            is_valido = False
            self.ttf_titulo.error_text = "Informe o título."
        if self.ttf_genero.value == "":
            is_valido = False
            self.ttf_genero.error_text = "Informe o gênero."
        if self.ttf_lancamento.value == "":
            is_valido = False
            self.ttf_lancamento.error_text = "Informe o lançamento."                        
        return is_valido

    def salvar(self, e):

        if self.validar():
            filme = Filme(
                id=self.filme_id,
                titulo=self.ttf_titulo.value,
                genero=self.ttf_genero.value,
                lancamento=self.ttf_lancamento.value
            )
            if self.filme_id == 0:
                self.filme_db.insert_filme(filme)     
            else:
                self.filme_db.update_filme(filme)

            self.limpar_formulario()       
            self.page.go("/")            

        else:
            self.update()
     
    def carregar_dados_filme(self):

        filme:Filme = self.filme_db.select_filme(filme_id=self.filme_id)
        
        if filme:
            self.ttf_titulo.value = filme.titulo
            self.ttf_genero.value = filme.genero
            self.ttf_lancamento.value = filme.lancamento