from src.modelo.livro import Livro
from src.data.database import Database


class LivroDB:

    def __init__(self, dbs: Database) -> None:
        self.dbs = dbs
        self.criar_tabela_livro()

    def criar_tabela_livro(self) -> None:
        """
        Método contendo a instrução de criação da tabela
        no banco de dados caso não exista.
        """
        sql = """
            CREATE TABLE IF NOT EXISTS 
                livro(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    titulo TEXT NOT NULL
                )
        """
        self.dbs.executar_sql(sql)

    # -----------------------------------------------------------------------
    def select_livros(self) -> list[Livro]:
        """
        Realizar uma consulta ao banco de dados para
        obtenção de todos os registros cadastrados
        """
        lista_livros: list[Livro] = []
        sql = "SELECT * FROM livro"
        cursor = self.dbs.executar_sql(sql)

        for registro in cursor:
            livro = Livro(
                id=registro[0],
                titulo=registro[1],
            )
            lista_livros.append(livro)

        return lista_livros

    # -----------------------------------------------------------------------
    def select_livro(self, livro_id: int) -> list[Livro]:
        """
        Realizar uma consulta ao banco de dados para
        obtenção de um registro de acordo com o id
        """
        parametros = (livro_id,)

        sql = "SELECT * FROM livro WHERE id = ?"
        cursor = self.dbs.executar_sql(sql, parametros)

        # Desnecessário usar for para um único registro.
        # Necessário refatorar
        for registro in cursor:
            livro = Livro(
                id=registro[0],
                titulo=registro[1],
            )

        return livro

    # -----------------------------------------------------------------------
    def insert_livro(self, novo_livro: Livro):
        parametros = (novo_livro.titulo,)
        sql = """
            INSERT INTO 
                livro(titulo) 
            VALUES(?)
        """
        self.dbs.executar_sql(sql, parametros)  # .rowcount

    # -----------------------------------------------------------------------
    def delete_livro(self, livro: Livro):
        parametros = (livro.id,)
        sql = "DELETE FROM livro WHERE id = ?"
        self.dbs.executar_sql(sql, parametros)

    # -----------------------------------------------------------------------
    def update_livro(self, livro: Livro):
        parametros = (livro.titulo, livro.id)
        sql = """
            UPDATE 
                livro 
            SET 
                titulo = ?
            WHERE 
                id = ?        
        """
        self.dbs.executar_sql(sql, parametros)


# Fim do código fonte
