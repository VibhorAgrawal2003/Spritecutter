import flet as ft
from style import *
from process import *

# Environment Values
mode = "dark"
spritesheet_path = " "

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

    # Interaction Functions

    def split_automatically(e):
        if spritesheet_path != " ":
            process_spritesheet(spritesheet_path, "output")
            success_label.value = "Image successfully split!\nPlease check output folder."

        else:
            success_label.value = "Please select an image first."

        success_label.update()


    def show_browse_window(e):
        browse_wizard.pick_files(
            allow_multiple = False, 
            allowed_extensions=["jpg", "png"],
            dialog_title="Choose a spritesheet"
            )

    def get_file(e: ft.FilePickerResultEvent):
        global spritesheet_path

        # User picked a file
        if e.files:
            spritesheet_path = e.files[0].path
            print(spritesheet_path)

            prompt_label.value = "Picked file(s): "
            prompt_label.value += (", ".join(map(lambda f: f.name, e.files)))

            # Call function from process script
            # process_spritesheet(spritesheet_path, "output")

        # Update page objects
        display_image.src = spritesheet_path
        display_image.update()
        prompt_label.update()


    # Window Settings
    page.window_width = 360   
    page.window_height = 640   
    page.window_resizable = False
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "Spritecutter"
    page.update()

    # Extracting Theme
    theme = ft.Theme()
    page.theme = theme

    # Adding Hero Section
    hero: object = Hero(page)
    page.add(hero)

    # Page Objects
    prompt_label = ft.Text(value = "\t\tStart by loading an image!")
    success_label = ft.Text()
    browse_wizard = ft.FilePicker(on_result=get_file)
    display_image = ft.Image(src = spritesheet_path, **preview_image)

    page.overlay.append(browse_wizard)


    page.add(ft.Row(
        [
            ft.IconButton(on_click = show_browse_window, **add_style_sheet),
            prompt_label,
        ]))
    
    page.add(ft.Container(
        content = display_image,
        **preview_panel,
    ))

    page.add(ft.Column(
    [
        ft.ElevatedButton("Split into poses automatically", on_click = split_automatically),
        success_label,
    ]))

    page.update()


# Driver Code
if __name__ == "__main__":
    ft.app(target = main)