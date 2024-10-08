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
                    ft.Text(
                        value=f"Dado recebido = {self.id}",
                        visible=True if self.id else False,
                        size=20,
                    ),
                ],
            )
        ]
