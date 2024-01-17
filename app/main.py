import flet as ft
from style import *

# Values
mode = "dark"
preview_border_color = ft.colors.WHITE

# Containers
class Hero(ft.SafeArea):

    # Switch View Mode Function
    def switch(self, e) -> None:
                global mode
                if self.page.theme_mode == ft.ThemeMode.DARK:
                    self.page.theme_mode = ft.ThemeMode.LIGHT
                    self.toggle.icon = ft.icons.LIGHT_MODE_ROUNDED
                    mode = "light"

                else:
                    self.page.theme_mode = ft.ThemeMode.DARK
                    self.toggle.icon = ft.icons.DARK_MODE_ROUNDED
                    mode = "dark"
                
                self.page.update()

    # Class Constructor
    def __init__(self, page: ft.Page) -> None:
        super().__init__(minimum=10, maintain_bottom_view_padding=True)
        self.page = page
        self.title = ft.Text(**heading_style_sheet)
        self.toggle = ft.IconButton(**toggle_style_sheet, on_click = lambda e: self.switch(e))
        
        # Hero Layout
        self.main: ft.Column = ft.Column(
            controls = [
                ft.Row(
                    alignment = "spaceBetween",
                    controls = [
                        self.title,
                        self.toggle,
                    ],
                )
            ]
        )

        self.content = self.main


# Main Page
def main(page: ft.Page) -> None:

    # Window Settings
    page.window_width = 360   
    page.window_height = 640   
    page.window_resizable = False
    page.theme_mode = ft.ThemeMode.DARK
    page.update()

    # Extracting Theme
    theme = ft.Theme()
    page.theme = theme

    # Adding Hero Section
    hero: object = Hero(page)
    page.add(hero)

    # Page Objects
    prompt_label = "\t\tStart by loading an image!"

    page.add(ft.Row(
        [
            ft.IconButton(**add_style_sheet),
            ft.Text(value=prompt_label),
        ]))
    

    page.add(ft.Container(
        content=ft.Image(src = " ", **preview_image),
        border=ft.border.all(2, ft.colors.LIGHT_BLUE),
        alignment=ft.alignment.center,
        padding=5,
        height=280,
        width=360,
    ))

    page.update()


# Driver Code
if __name__ == "__main__":
    ft.app(target = main)