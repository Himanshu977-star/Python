import speech_recognition as sr
import pyttsx3

def tts(text):
    if text:
        engine = pyttsx3.init()
        engine.setProperty('volume', 1.0)
        engine.setProperty('rate', 150)

        voices = engine.getProperty('voices')
        if len(voices) > 1:
            engine.setProperty('voice', voices[0].id)

        engine.say(text)
        engine.runAndWait()

def stt():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return f'Himanshu, you said: {text}'
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio")
        return None
    except sr.RequestError:
        print("Could not request results, check your internet connection")
        return None  

if __name__ == "__main__":
    choice=input("Voice Assistance/Write(1/2):")
    if choice=="1":
        text = stt()
        print(text)
        tts(text)
    elif choice=="2":
        text=input("Enter what you want:")
        tts(f'Himanshu, you said: {text}')
        print(f'Himanshu, you said: {text}')
    else:
      print("Invalid Choice")        
