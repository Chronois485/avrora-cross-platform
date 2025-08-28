import flet as ft

# ==== PAGE SETTINGS ====
PAGE_TITLE = "A.V.R.O.R.A"
PAGE_THEME = ft.ThemeMode.DARK

# ==== LOGGING ====
LOGGING_FILENAME = "avrora.log"

# ==== TEXT TO SPEACH SETTINGS ====
PIPER_MODEL_PATH = "./assets/tts-model/uk_UA-ukrainian_tts-medium.onnx"
PIPER_MODEL_CONFIG_PATH = "./assets/tts-model/uk_UA-ukrainian_tts-medium.onnx.json"
PIPER_BINARY_PATH = "piper"
TEMP_WAV_SUFFIX = ".wav"
AUDIO_PLAYER_LINUX = "aplay"
AUDIO_PLAYER_MACOS = "afplay"

# ==== WINDOW SETTINGS ====
WINDOW_WIDTH = 450
WINDOW_HEIGHT = 665
WINDOW_MIN_WIDTH = 450
WINDOW_MAX_WIDTH = 450
WINDOW_MAX_HEIGHT = 665
WINDOW_MIN_HEIGHT = 665

# ==== MENU SETTINGS ====
MENU_WIDTH = 430.4
MENU_HEIGHT = 565

# ==== ALIGNMENTS ====
TEXT_CENTER = ft.TextAlign.CENTER
TEXT_RIGHT = ft.TextAlign.RIGHT
TEXT_LEFT = ft.TextAlign.LEFT
MAIN_AXIS_CENTER = ft.MainAxisAlignment.CENTER
MAIN_AXIS_SPACE_BETWEEN = ft.MainAxisAlignment.SPACE_BETWEEN
MAIN_AXIS_SPACE_EVENLY = ft.MainAxisAlignment.SPACE_EVENLY
MAIN_AXIS_SPACE_AROUND = ft.MainAxisAlignment.SPACE_AROUND
MAIN_AXIS_END = ft.MainAxisAlignment.END
MAIN_AXIS_START = ft.MainAxisAlignment.START

# ==== RECORDING ====
AUDIO_FILENAME = "record.wav"
AUDIO_FILES_FOLDER = "./audio/"
FREQUENCY = 44100
DURATION = 5

# ==== COLORS ====
COLORS = {
    "ON_PRIMARY": ft.Colors.ON_PRIMARY,
    "ON_PRIMARY_CONTAINER": ft.Colors.ON_PRIMARY_CONTAINER
}

# ==== ICONS ====
ICON_SETTINGS = ft.Icons.SETTINGS
ICON_INFO = ft.Icons.INFO

# ==== UI TEXT ====
FULL_APP_NAME = "Advanced Voice-Activated Robot for Optimized Reliable Assistance"
TOOLTIP_SETTINGS = "Налаштування"
TOOLTIP_INFO = "Інформація"
INFO_MENU_HEADER = "Інформація"
SETTINGS_MENU_HEADER = "Налаштування"
