import flet as ft


class ViewUm(ft.View):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = "/"
        self.appbar = ft.AppBar(title=ft.Text("View Um"), bgcolor="green")
        self.page = page
        self.ttf_dado = ft.TextField(expand=True)

        self.controls = [
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            self.ttf_dado,
                            ft.ElevatedButton(
                                text="Enviar",
                                on_click=lambda _: self.page.go(
                                    f"/view_dois/{self.ttf_dado.value}"
                                ),
                            ),
                        ]
                    ),
                    ft.ElevatedButton(
                        text="Ir para View 2 sem dados",
                        on_click=lambda _: self.page.go("/view_dois"),
                    ),
                ],
            )
        ]
