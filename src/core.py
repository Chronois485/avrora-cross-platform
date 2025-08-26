import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import logging
import constants as const
import numpy as np
import os

logging.basicConfig(filename=const.LOGGING_FILENAME, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


def record_voice(record_filename):
    logger.info("Recording audio.")
    recording = sd.rec(int(const.DURATION * const.FREQUENCY), samplerate=const.FREQUENCY, channels=1, dtype="float32")
    sd.wait()
    logger.info("Record complete.")

    recording_int16 = np.int16(recording * 32767)

    if not os.path.exists(const.AUDIO_FILES_FOLDER):
        logger.warning("Unknown path to audio file. Creating path")
        os.makedirs(const.AUDIO_FILES_FOLDER)

    write(record_filename, const.FREQUENCY, recording_int16)
    logger.info(f"Output saved into {record_filename}")

def speech_to_text(audio_file):
    r = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)

    try:
        recognized_text = r.recognize_google(audio, language="uk-UA")
        logger.info(f"Recognized text: {recognized_text}")
        return recognized_text
    except sr.UnknownValueError:
        logger.warning("Could not understand audio")
    except sr.RequestError as e:
        logger.error(f"Could not request results from Google Speech Recognition service; {e}")

