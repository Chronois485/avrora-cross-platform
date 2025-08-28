import os
import platform
import subprocess
import tempfile
import shutil
import json

import constants as const

try:
    from piper import PiperVoice
    HAS_PIPER_API = True
except ImportError:
    HAS_PIPER_API = False


class VoiceAssistant:
    def __init__(self):
        self.model_path = const.PIPER_MODEL_PATH
        self.binary_path = const.PIPER_BINARY_PATH
        self.config_path = const.PIPER_MODEL_CONFIG_PATH
        self.system = platform.system()

        self.speaker_id_map = {}
        if self.config_path and os.path.exists(self.config_path):
            with open(self.config_path, "r", encoding="utf-8") as f:
                cfg = json.load(f)
                self.speaker_id_map = cfg.get("speaker_id_map", {})
        else:
            self.speaker_id_map = {"default": 0}

    def speak(self, text: str, speaker: str="default"):
        """Offline TTS with piper"""
        spk_id = self.speaker_id_map.get(speaker, 0)

        if shutil.which(self.binary_path):
            tmp_file = tempfile.NamedTemporaryFile(
                delete=False, suffix=const.TEMP_WAV_SUFFIX
            )
            tmp_file.close()

            subprocess.run([
                self.binary_path,
                "--model", self.model_path,
                "--output_file", tmp_file.name,
                text
            ], check=True)

            self._play_audio(tmp_file.name)
            os.remove(tmp_file.name)

        elif HAS_PIPER_API:
            voice = PiperVoice.load(self.model_path)
            tmp_file = tempfile.NamedTemporaryFile(
                delete=False, suffix=const.TEMP_WAV_SUFFIX
            )
            tmp_file.close()

            with open(tmp_file.name, "wb") as f:
                voice.synthesize(text, f, speaker_id=spk_id)

            self._play_audio(tmp_file.name)
            os.remove(tmp_file.name)
        else:
            raise RuntimeError(
                "Piper not found."
                "Download 'piper' binary, or python library 'piper-tts'."
            )

    def _play_audio(self, file_path: str):
        """Simple audio playing"""
        system = self.system

        if system == "Linux":
            subprocess.run([const.AUDIO_PLAYER_LINUX, file_path])
        elif system == "Darwin":
            subprocess.run([const.AUDIO_PLAYER_MACOS, file_path])
        elif system == "Windows":
            import winsound
            winsound.PlaySound(file_path, winsound.SND_FILENAME)
        else:
            print(f"Cannot play audio file: {file_path}")


if __name__ == "__main__":
    va = VoiceAssistant()
    va.speak("привіт! я твій голосовий помічник.", speaker="mykyta")