import datetime
import flet as ft


def main(page: ft.Page):

    # Configurar a localizaçao regional do app
    # Neste caso, o Locale é PT de Português
    page.locale_configuration = ft.LocaleConfiguration(
        supported_locales=[
            ft.Locale("pt", "PT"),
        ],
        current_locale=ft.Locale("pt", "PT"),
    )

    # Função será invocada quando o botão 'Ok' for clicado
    def change_date(e: ft.ControlEvent):
        # Incluir uma mensagem na Page contendo a data selecionada
        page.add(
            ft.Text(
                f"Data selecionada ao clicar OK: {date_picker.value.strftime('%d-%m-%Y')}"
            )
        )

    # 'Esta função será invocada quando o usuário clicar fora do
    # DatePicker ou clicar no botão 'Cancelar'.
    def date_picker_dismissed(e: ft.ControlEvent):
        # Incluir uma mensagem na Page contendo a data selecionada anteriormente
        page.add(
            ft.Text(
                f"Ao ser dispensado, a data era:  {date_picker.value.strftime('%d-%m-%Y')}"
            )
        )

    # Componente DatePicker é um compoente selecionador de data
    date_picker = ft.DatePicker(
        # Associar uma função manipuladora de evento
        # 'handle_change' será invocada quando o usuário clicar no
        # botão 'OK'.
        on_change=change_date,
        # Associar uma função manipuladora de evento
        # 'handle_dismissal' será invocada quando o usuário clicar fora do
        # DatePicker ou clicar no botão 'Cancelar'.
        on_dismiss=date_picker_dismissed,
        # Define o limite inferior para seleção de data
        first_date=datetime.datetime(2023, 10, 1),
        # Define o limite superior para seleção de data
        last_date=datetime.datetime(2024, 10, 1),
    )

    # Botão cuja função é invocar o componente DatePicker (selecionador de data)
    date_button = ft.ElevatedButton(
        # Rótulo do botão
        text="Selecionador de data",
        # Ícone do botão
        icon=ft.icons.CALENDAR_MONTH,
        # Ao ser clicado invoca o componente DatePicker (selecionador de data)
        on_click=lambda _: page.open(date_picker),
    )

    # Incluir os componentes na page
    page.add(date_picker, date_button)


# Porta de entrada do aplicativo Flet
ft.app(target=main)
