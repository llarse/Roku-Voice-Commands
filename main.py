import speech_recognition as sr
import json
from vosk import Model, KaldiRecognizer
import sys
import os

from voice_controller import VoiceController

# Load Vosk model
if not os.path.exists("model"):
    print("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit(1)
model = Model("model")


def new_audio(mic, r, recognizer):
    ''' Reset/Create the audio stream '''
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    return audio


def main():
    # Load the configuration file
    with open('config.json', 'r') as f:
        config = json.load(f)

    # Establish microphone and recognizer
    r = sr.Recognizer()
    mic = sr.Microphone()

    # Initialize the voice controller
    vc = VoiceController()

    # Initialize Vosk recognizer
    recognizer = KaldiRecognizer(model, 16000)

    print('Audio commands started. Press Ctrl+C to exit')

    while True:
        audio = new_audio(mic, r, recognizer)
        if recognizer.AcceptWaveform(audio.get_wav_data()):
            try:
                text = recognizer.Result()
            except sr.UnknownValueError:
                if config["Verbose"]:
                    print("Could not understand audio")
                continue

            # Output the text to the console if what they said was recognized
            if config["Verbose"]:
                print("You said: {}".format(text))

            # Let the voice controller know what they said
            try:
                # Executes the command if it is a valid command
                vc.execute(text)
            except KeyError:
                # What they said was not a valid command, we dont care
                pass


if __name__ == '__main__':
    main()
