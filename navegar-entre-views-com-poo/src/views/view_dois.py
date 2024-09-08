import flet as ft


class ViewDois(ft.View):

    def __init__(self, page: ft.Page, id=None):
        super().__init__()
        self.route = "/view_dois"
        self.appbar = ft.AppBar(title=ft.Text("View Dois"))
        self.page = page
        self.id = id

        self.controls = [
            ft.Column(
                controls=[
                    ft.ElevatedButton(
                        text="Ir para View 1",
                        on_click=lambda _: self.page.go("/"),
                    ),
                    ft.ElevatedButton(
                        text="Ir para View 3",
                        on_click=lambda _: self.page.go("/view_tres"),
                    ),
                    ft.Text(
                        value=f"Dado id = {self.id}",
                        visible=True if self.id else False,
                        size=20,
                    ),
                ],
            )
        ]
