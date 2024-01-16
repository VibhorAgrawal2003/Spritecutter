import flet as ft
import process

def main(page: ft.Page):

    global spritesheet_path

    # Picking a file from wizard
    def show_browse_window(e):
        browse_wizard.pick_files(
            allow_multiple = False, 
            allowed_extensions=["jpg", "png"],
            dialog_title="Choose a spritesheet"
            )

    # After file has been picked
    def get_file(e: ft.FilePickerResultEvent):

        global spritesheet_path
        spritesheet_path = e.files[0].path
        print(spritesheet_path)

        if e.files:
            picked_files.value = (", ".join(map(lambda f: f.name, e.files)))
            status.value = "The spritesheet has been processed successfully!"

            # User picked a file
            process.process_spritesheet(spritesheet_path, "output")

        picked_files.update()
        preview_load()

    # Window Settings
    page.window_width = 640     
    page.window_height = 480   
    page.window_resizable = False
    page.theme_mode = ft.ThemeMode.DARK
    page.update()

    # Window Elements
    browse_wizard = ft.FilePicker(on_result=get_file)
    picked_files = ft.Text()
    status = ft.Text()

    status.value = "Select a spritesheet to process it."

    page.overlay.append(browse_wizard)

    page.add(ft.Row(
        [
            ft.ElevatedButton("Browse for spritesheet", on_click=show_browse_window),
            picked_files,
        ]))
    
    page.add(ft.Row(
        [
            status,
        ]))
        
    # Preview Window

    def preview_load():
        
        global spritesheet_path
        global spritesheet

        if spritesheet_path != "":

            spritesheet = ft.Image(
                src = spritesheet_path,
                # src = str(browse_wizard.result.path),
                width = 240,
                height = 240,
                fit=ft.ImageFit.CONTAIN,
            )

            page.add(ft.Row([
                spritesheet,
            ]))


ft.app(target=main)