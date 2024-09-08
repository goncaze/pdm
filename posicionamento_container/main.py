# importa a biblioteca FLET
import flet as ft

# Função principal
def main(page: ft.Page):
    # Determinar tema claro
    page.theme_mode = ft.ThemeMode.LIGHT

    page.window_width = 350 # Largura da janela
    page.window_height = 600 # Altura da janela

    # Um texto qualquer
    rotulo = ft.Text("Hello, Flet!")

    # Função chamada pelo btn AVS
    def avs(e):
        # Altera valor do rótulo
        rotulo.value = "Alinhamento Vertical Start"
        # Altera o alinhamento vertical de page
        page.vertical_alignment = ft.MainAxisAlignment.START
        # Reflete as alterações em page
        page.update()

    # Componente botão
    btn_avs = ft.ElevatedButton(
        # Texto do componente botão
        text = "A.V.S.",
        # Evento click/chamada de função
        on_click=avs
    )
    
    # Função chamada pelo btn AVC
    def avc(e):
        # Altera valor do rótulo
        rotulo.value = "Alinhamento Vertical Center"
        # Altera o alinhamento vertical de page
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        # Reflete as alterações em page
        page.update()

    # Componente botão
    btn_avc = ft.ElevatedButton(
        # Texto do componente botão
        text = "A.V.C.",
        # Evento click/chamada de função
        on_click=avc
    )

    # Função chamada pelo btn AVE
    def ave(e):
        # Altera valor do rótulo
        rotulo.value = "Alinhamento Vertical End"
        # Altera o alinhamento vertical de page
        page.vertical_alignment = ft.MainAxisAlignment.END
        # Reflete as alterações em page
        page.update()

    # Componente botão
    btn_ave = ft.ElevatedButton(
        # Texto do componente botão
        text = "A.V.E.",
        # Evento click/chamada de função
        on_click=ave
    )    

    # Função chamada pelo btn AVSA
    def avsa(e):
        # Altera valor do rótulo
        rotulo.value = "Alinhamento Vertical Space Around"
        # Altera o alinhamento vertical de page
        page.vertical_alignment = ft.MainAxisAlignment.SPACE_AROUND
        # Reflete as alterações em page
        page.update()

    # Componente botão
    btn_avsa = ft.ElevatedButton(
        # Texto do componente botão
        text = "A.V.S.A.",
        # Evento click/chamada de função
        on_click=avsa
    ) 

    # Função chamada pelo btn AVSB
    def avsb(e):
        # Altera valor do rótulo
        rotulo.value = "Alinhamento Vertical Space Between"
        # Altera o alinhamento vertical de page
        page.vertical_alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        # Reflete as alterações em page
        page.update()

    # Componente botão
    btn_avsb = ft.ElevatedButton(
        # Texto do componente botão
        text = "A.V.S.B.",
        # Evento click/chamada de função
        on_click=avsb
    ) 

    # Função chamada pelo btn AVSE
    def avse(e):
        # Altera valor do rótulo
        rotulo.value = "Alinhamento Vertical Space Evenly"
        # Altera o alinhamento vertical de page
        page.vertical_alignment = ft.MainAxisAlignment.SPACE_EVENLY
        # Reflete as alterações em page
        page.update()

    # Componente botão
    btn_avse = ft.ElevatedButton(
        # Texto do componente botão
        text = "A.V.S.E.",
        # Evento click/chamada de função
        on_click=avse
    ) 

    popup_ali_verticais = ft.PopupMenuButton(
        content=ft.Icon(name=ft.icons.SWAP_VERT_CIRCLE_OUTLINED),
        items = [
            ft.PopupMenuItem(text="A.V.S.", on_click=avs),        
            ft.PopupMenuItem(text="A.V.C.", on_click=avc),            
            ft.PopupMenuItem(text="A.V.E.", on_click=ave),
            ft.PopupMenuItem(text="A.V.S.A.", on_click=avsa),
            ft.PopupMenuItem(text="A.V.S.B.", on_click=avsb),
            ft.PopupMenuItem(text="A.V.S.E", on_click=avse)
        ]
    )

    # Função chamada pelo btn AHS
    def ahs(e):
        # Altera valor do rótulo
        rotulo.value = "Alinhamento Horizontal Start"
        # Altera o alinhamento horizontal de page
        page.horizontal_alignment = ft.CrossAxisAlignment.START
        # Reflete as alterações em page
        page.update()

    # Função chamada pelo btn AHC
    def ahc(e):
        # Altera valor do rótulo
        rotulo.value = "Alinhamento Horizontal Center"
        # Altera o alinhamento horizontal de page
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        # Reflete as alterações em page
        page.update()

    # Função chamada pelo btn AHE
    def ahe(e):
        # Altera valor do rótulo
        rotulo.value = "Alinhamento Horizontal End"
        # Altera o alinhamento horizontal de page
        page.horizontal_alignment = ft.CrossAxisAlignment.END
        # Reflete as alterações em page
        page.update()

    # Função chamada pelo btn AHST
    def ahst(e):
        # Altera valor do rótulo
        rotulo.value = "Alinhamento Horizontal Stretch"
        # Altera o alinhamento horizontal de page
        page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
        # Reflete as alterações em page
        page.update()

    # Função chamada pelo btn AHB
    def ahb(e):
        # Altera valor do rótulo
        rotulo.value = "Alinhamento Horizontal Baseline"
        # Altera o alinhamento horizontal de page
        page.horizontal_alignment = ft.CrossAxisAlignment.BASELINE
        # Reflete as alterações em page
        page.update()        

    popup_ali_horizontais = ft.PopupMenuButton(
        content=ft.Icon(name=ft.icons.SWAP_HORIZONTAL_CIRCLE_OUTLINED),
        items = [
            ft.PopupMenuItem(text="A.H.S.", on_click=ahs),
            ft.PopupMenuItem(text="A.H.C.", on_click=ahc),
            ft.PopupMenuItem(text="A.H.E.", on_click=ahe),
            ft.PopupMenuItem(text="A.H.ST.", on_click=ahst),
        ]
    )

    
    # Um container de linha
    linha_de_botoes = ft.Row(
        # Lista de controles
        controls = [
            popup_ali_verticais,
            popup_ali_horizontais,            
        ],
        wrap = True,
    )

    ##
    # Desenho dos quadros usando componete Container
    ##
    qd_amarelo = ft.Container( # Quadrado amarelo
        bgcolor = ft.colors.YELLOW, # cor de fundo
        width = 50, # largura
        height = 50 # altura
    )

    qd_verde = ft.Container( # Quadrado verde
        bgcolor=ft.colors.GREEN, # cor de fundo
        width = 50, # largura
        height = 50 # altura
    )

    qd_blue = ft.Container( # Quadrado azul
        bgcolor=ft.colors.BLUE, # cor de fundo
        width = 50, # largura
        height = 50 # altura
    )


    # Adicionar componentes em page
    page.add(
        rotulo, 
        linha_de_botoes,
        qd_amarelo, 
        qd_verde, 
        qd_blue
    )


ft.app(main)
