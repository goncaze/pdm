class Livro:

    def __init__(self, id: int = 0, titulo: str = None) -> None:
        self._id = id
        self._titulo = titulo

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        self._titulo = novo_titulo

    def __str__(self) -> str:
        return f"""
            Dados do livro:
            {self.id = }
            {self.titulo = }
        """
