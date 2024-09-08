import flet as ft


def main(page: ft.Page):

    def incluir_item(e):
        lista_view.controls.append(ft.Checkbox(label=novo_item.value))
        novo_item.value = ""
        visao.update()

    # Componente para entrada de novo item
    novo_item = ft.TextField(hint_text="Novo item de supermercado", expand=True)

    # Componente para simular a lista de itens
    lista_view = ft.Column()

    # Componente para organizar o layout
    visao = ft.Column(
        width=600,
        controls=[
            ft.Row(  # Componente linha
                controls=[
                    novo_item,  # Insere componente TextFiel criado anteriormente
                    # Insere um componente de botão
                    ft.FloatingActionButton(icon=ft.icons.ADD, on_click=incluir_item),
                ],
            ),  # Insere a lista de supermercado no componente de organização
            lista_view,
        ],
    )

    # def incluir_item(e):
    #     lista_view.controls.append(ft.Checkbox(label=novo_item.value))
    #     novo_item.value = ""
    #     visao.update()

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(visao)


ft.app(target=main)
