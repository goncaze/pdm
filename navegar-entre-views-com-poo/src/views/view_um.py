import flet as ft


class ViewUm(ft.View):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = "/"
        self.appbar = ft.AppBar(title=ft.Text("View Um"))
        self.page = page

        self.controls = [
            ft.Column(
                controls=[
                    ft.ElevatedButton(
                        text="Ir para View 2 sem dados",
                        on_click=lambda _: self.page.go("/view_dois"),
                    ),
                    ft.ElevatedButton(
                        text="Ir para View 3 sem dados",
                        on_click=lambda _: self.page.go("/view_tres"),
                    ),
                    ft.ElevatedButton(
                        text="Ir para View 2 com dados",
                        on_click=lambda _: self.page.go("/view_dois/2"),
                    ),
                    ft.ElevatedButton(
                        text="Ir para View 3 com dados",
                        on_click=lambda _: self.page.go("/view_tres/3"),
                    ),
                ],
            )
        ]
