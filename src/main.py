import flet as ft

import constants as const
import core


def main(page: ft.Page):
    # Basic variables
    page.title = const.PAGE_TITLE
    page.theme_mode = const.PAGE_THEME
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Window settings
    page.window.width = const.WINDOW_WIDTH
    page.window.height = const.WINDOW_HEIGHT
    page.window.max_width, page.window.min_width = const.WINDOW_MAX_WIDTH, const.WINDOW_MIN_WIDTH
    page.window.max_height, page.window.min_height = const.WINDOW_MAX_HEIGHT, const.WINDOW_MIN_HEIGHT
    core.logger.info("Setup of base variables of page is complete.")

    # Assignment of controls
    app_name_label = ft.Text(const.PAGE_TITLE, size=30)
    app_name_lower_label = ft.Text(const.FULL_APP_NAME, size=10)
    settings_button = ft.IconButton(const.ICON_SETTINGS, tooltip=const.TOOLTIP_SETTINGS)
    info_button = ft.IconButton(const.ICON_INFO, tooltip=const.TOOLTIP_INFO)
    first_row = ft.Row([info_button, ft.Column([app_name_label, app_name_lower_label]), settings_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    central_column = ft.Column([first_row])

    page.add(central_column)


ft.run(main)
