# importa a biblioteca Flet
import flet as ft

# A função main()é um ponto de entrada em um aplicativo Flet.
# Ele está sendo chamado em um novo thread para cada sessão de
# usuário com uma instância Page passada para ele.
def main(page: ft.Page):

    # Page é como uma "tela" específica para um usuário, um estado
    # visual de uma sessão de usuário. Para construir uma UI de
    # aplicativo, você adiciona e remove controles de uma página e
    # atualiza suas propriedades. No exemplo a seguir o componente Text
    # é adicionado à página.
    page.add(ft.Text(value="Hello World!"))

# Um programa Flet típico termina com uma chamada para flet.app()
# onde o aplicativo começa a aguardar novas sessões de usuário.
ft.app(port=8550, target=main)
