class Filme:
    def __init__(
            self, 
            id:int = 0, 
            titulo:str = None, 
            genero:str = None, 
            lancamento:int = 0
            ) -> None:
        self._id:int = id
        self._titulo:str = titulo 
        self._genero:str = genero
        self._lancamento:int = lancamento


    @property
    def id(self)-> int:
        return self._id

    @property
    def titulo(self)->str:
        return self._titulo

    @property
    def genero(self)->str:
        return self._genero

    @property
    def lancamento(self)->int:
        return self._lancamento

    @id.setter
    def id(self, novo_id)-> None:
        self._id = novo_id
        # return "Id não deve ser alterado!"
    
    @titulo.setter
    def titulo(self, novo_titulo)->None:
        self._titulo = novo_titulo

    @genero.setter
    def genero(self, novo_genero)->None:
        self._genero = novo_genero

    @lancamento.setter
    def lancamento(self, novo_lancamento)->None:
        self._lancamento = novo_lancamento

    def __str__(self) -> str:
        return f"""
            {self._titulo = }, {self._genero = }, {self._lancamento = }
        """
