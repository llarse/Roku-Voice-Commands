import speech_recognition as sr
import json

from voice_controller import VoiceController


def new_audio(mic, r):
    ''' Reset/Create the audio stream '''
    with mic as source:
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

    # Start listening for commands
    print('Audio commands started. Press Ctrl+C to exit')
    audio = new_audio(mic, r)

    # Require keyboard interupt to stop
    while True:
        try:
            text = r.recognize_google(audio)
            print(text)
        except sr.UnknownValueError:
            print("Could not understand audio")
            continue
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))
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

        # Listen for a new command
        audio = new_audio(mic, r)


if __name__ == '__main__':
    main()
