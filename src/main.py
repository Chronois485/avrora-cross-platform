import flet as ft

import constants as const
import core


def main(page: ft.Page):
    # Basic variables
    page.title = const.PAGE_TITLE
    page.theme_mode = const.PAGE_THEME
    page.vertical_alignment = const.MAIN_AXIS_START
    info_is_open = False
    settings_is_open = False

    # Window settings
    page.window.width = const.WINDOW_WIDTH
    page.window.height = const.WINDOW_HEIGHT
    page.window.max_width, page.window.min_width = const.WINDOW_MAX_WIDTH, const.WINDOW_MIN_WIDTH
    page.window.max_height, page.window.min_height = const.WINDOW_MAX_HEIGHT, const.WINDOW_MIN_HEIGHT
    core.logger.info("Setup of base variables of page is complete.")

    # Functions
    def open_menu(e):
        nonlocal info_is_open
        nonlocal settings_is_open
        if info_is_open:
            info_menu.top = 0
            info_menu.left = const.WINDOW_WIDTH * -1
            info_is_open = False
        else:
            settings_menu.top = 0
            settings_menu.left = const.WINDOW_WIDTH
            settings_is_open = False
            info_menu.top = 0
            info_menu.left = 0
            info_is_open = True
        page.update()

    def open_settings(e):
        nonlocal settings_is_open
        nonlocal info_is_open
        if settings_is_open:
            settings_menu.top = 0
            settings_menu.left = const.WINDOW_WIDTH
            settings_is_open = False
        else:
            settings_menu.top = 0
            settings_menu.left = 0
            settings_is_open = True
            info_menu.top = 0
            info_menu.left = const.WINDOW_WIDTH * -1
            info_is_open = False
        page.update()

    # Assignment of controls
    app_name_label = ft.Text(const.PAGE_TITLE, size=30, text_align=const.TEXT_CENTER, width=const.WINDOW_WIDTH - 120)
    app_name_lower_label = ft.Text(const.FULL_APP_NAME, size=10)
    settings_button = ft.IconButton(const.ICON_SETTINGS, tooltip=const.TOOLTIP_SETTINGS, on_click=open_settings)
    info_button = ft.IconButton(const.ICON_INFO, tooltip=const.TOOLTIP_INFO, on_click=open_menu)
    first_row = ft.Row([info_button, ft.Column([app_name_label, app_name_lower_label]), settings_button],
                       alignment=const.MAIN_AXIS_SPACE_BETWEEN)

    menu_divider = ft.Divider()
    info_menu_header = ft.Text(const.INFO_MENU_HEADER, size=30, text_align=const.TEXT_CENTER)
    info_menu_column = ft.Column([
        ft.Row([info_menu_header], alignment=const.MAIN_AXIS_CENTER),
        menu_divider
    ])
    info_menu = ft.Container(info_menu_column, border=ft.Border.all(width=5, color=const.COLORS["ON_PRIMARY"]),
                             border_radius=10, animate_position=500, top=0, left=const.WINDOW_WIDTH * -1,
                             height=const.MENU_HEIGHT,
                             width=const.MENU_WIDTH, padding=10)

    settings_menu_header = ft.Text(const.SETTINGS_MENU_HEADER, size=30, text_align=const.TEXT_CENTER)
    settings_menu_column = ft.Column([
        ft.Row([settings_menu_header], alignment=const.MAIN_AXIS_CENTER),
        menu_divider
    ])
    settings_menu = ft.Container(settings_menu_column, border=ft.Border.all(width=5, color=const.COLORS["ON_PRIMARY"]),
                                 border_radius=10, animate_position=500, top=0, left=const.WINDOW_WIDTH,
                                 height=const.MENU_HEIGHT,
                                 width=const.MENU_WIDTH, padding=10)

    central_column = ft.Column(
        [first_row, ft.Stack([info_menu, settings_menu], height=const.MENU_HEIGHT, width=const.MENU_WIDTH)])

    page.add(central_column)


ft.run(main)
