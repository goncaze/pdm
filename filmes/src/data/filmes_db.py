from src.modelo.filme import Filme
from src.data.database import Database


class FilmeDB:

    def __init__(self, dbs: Database) -> None:
        self.dbs = dbs
        self.criar_tabela_filme()

    def criar_tabela_filme(self) -> None:
        """
        Método contendo a instrução de criação da tabela
        no banco de dados, caso não exista.
        """
        sql = """
            CREATE TABLE IF NOT EXISTS 
                filme(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    titulo TEXT NOT NULL,
                    genero TEXT NOT NULL,
                    lancamento INTEGER NOT NULL
                )
        """
        self.dbs.executar_sql(sql)

    # -----------------------------------------------------------------------
    def select_filmes(self) -> list[Filme]:
        """
        Realizar uma consulta ao banco de dados para
        obtenção de todos os registros cadastrados
        """
        lista_filmes: list[Filme] = []
        sql = "SELECT * FROM filme"
        cursor = self.dbs.executar_sql(sql)

        for registro in cursor:
            filme = Filme(
                id=registro[0],
                titulo=registro[1],
                genero=registro[2],
                lancamento=registro[3],
            )
            lista_filmes.append(filme)

        return lista_filmes

    # -----------------------------------------------------------------------
    def select_filme(self, filme_id: int) -> Filme:
        """
        Realizar uma consulta ao banco de dados para
        obtenção de um registro de acordo com o id
        """
        parametros = (filme_id,)

        sql = "SELECT * FROM filme WHERE id = ?"
        cursor = self.dbs.executar_sql(sql, parametros)

        filme = None
        # Desnecessário usar for para um único registro.
        # Necessário refatorar
        for registro in cursor:
            filme = Filme(
                id=registro[0],
                titulo=registro[1],
                genero=registro[2],
                lancamento=registro[3],
            )

        return filme

    # -----------------------------------------------------------------------
    def insert_filme(self, novo_filme: Filme):
        parametros = (novo_filme.titulo, novo_filme.genero, novo_filme.lancamento)
        sql = """
            INSERT INTO 
                filme(titulo, genero, lancamento) 
            VALUES(?, ?, ?)
        """
        self.dbs.executar_sql(sql, parametros)  # .rowcount

    # -----------------------------------------------------------------------
    def delete_filme(self, filme: Filme):
        parametros = (filme.id,)
        sql = "DELETE FROM filme WHERE id = ?"
        self.dbs.executar_sql(sql, parametros)

    # -----------------------------------------------------------------------
    def update_filme(self, filme: Filme):
        parametros = (filme.titulo, filme.genero, filme.lancamento, filme.id)
        sql = """
            UPDATE 
                filme 
            SET 
                titulo = ?, genero = ?, lancamento = ?
            WHERE 
                id = ?        
        """
        self.dbs.executar_sql(sql, parametros)


# Fim do código fonte