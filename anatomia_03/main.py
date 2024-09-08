import flet as ft


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_height = 600
    page.window_width = 320

    texto = ft.Text(
        size=30,
        text_align=ft.TextAlign.RIGHT,
        value="Olá turma de TDS, bora estudar moçada!!",
        color=ft.colors.AMBER_500,  # Cor da fonte "Named colors"
    )
    texto2 = ft.Text(
        size=25,  # Alinhamento não funciona com fonte <= 20
        text_align=ft.TextAlign.CENTER,
        value="Aqui vai de uma outra cor!!",
        color="green",
    )

    page.add(texto, texto2)
    # page.add(texto2)


ft.app(main)
