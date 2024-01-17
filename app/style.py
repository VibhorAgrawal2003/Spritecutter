import flet as ft

_dark: str = ft.colors.with_opacity(0.5, "white")
_light: str = ft.colors.with_opacity(1, "black")

toggle_style_sheet: dict = {
    "icon": ft.icons.DARK_MODE_ROUNDED,
    "icon_size": 18,
    }

add_style_sheet: dict = {
    "icon": ft.icons.ADD_ROUNDED,
    "icon_size": 18,
    }

heading_style_sheet: dict = {
    "value": "Spritecutter",
    "size": 20,
    "weight": "w400",
    }

preview_image: dict = {
    "width": "240",
    "height": "240",
    "error_content": ft.Icon(ft.icons.QUESTION_MARK),
}