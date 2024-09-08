import sqlite3
from pathlib import Path


class Database:

    def __init__(self, DB_FILE: Path) -> None:
        self.DB_FILE = DB_FILE
        self.conexao: sqlite3.Connection = None
        self.cursor: sqlite3.Cursor = None

    # -----------------------------------------------------------------------
    def executar_sql(self, sql: str, parametros: tuple = ()) -> sqlite3.Cursor:
        """
        Método que executa as instruções SQL
        Retorna um cursor com o resultado do banco de dados
        """
        # Cria uma conexão com o arquivo de banco de dados
        with sqlite3.connect("./livros.db", check_same_thread=True) as self.conexao:
            # Obter um cursor a partir da conexão
            self.cursor = self.conexao.cursor()
            # Executa a instrução sql com os parâmetros fornecidos
            self.cursor.execute(sql, parametros)
            # Confirma a alteração de estado do banco de dados
            self.conexao.commit()
        # Retorna o cursor contendo o resultado da execução sql/parâmetros
        return self.cursor
