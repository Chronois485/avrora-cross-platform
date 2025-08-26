import logging

import flet as ft
import core
import constants as const


def main(page: ft.Page):
    # Basic variables
    page.title = const.PAGE_TITLE
    page.theme_mode = const.PAGE_THEME
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Window settings
    page.window.width = const.WINDOW_WIDTH
    page.window.height = const.WINDOW_HEIGHT
    page.window.max_width, page.window.min_width = const.WINDOW_MAX_WIDTH, const.WINDOW_MIN_WIDTH
    page.window.max_height, page.window.min_height = const.WINDOW_MAX_HEIGHT, const.WINDOW_MIN_HEIGHT
    core.logger.info("Setup of base variables of page is complete.")



    page.add()


ft.run(main)
