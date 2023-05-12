from gtts import gTTS
import playsound as play
import speech_recognition as sr


def speak(text):
    speaker = gTTS(text=text)
    filename = "voice.mp3"
    speaker.save(filename)
    play.playsound(filename)

def listen():
        LISTENER = sr.Recognizer()

        with sr.Microphone() as source:
            print('Listening...')
            voice = LISTENER.listen(source)
            LISTENER.adjust_for_ambient_noise(source, duration=1)

        try:
            command = LISTENER.recognize_google(voice)
            print(f'You said: {command}')

        except:
            print("Oops Error!!")
            command = "Could not listen. Please try again"
        
        return command
