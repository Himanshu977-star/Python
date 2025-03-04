import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        audio = recognizer.listen(source)  # Capture audio

    try:
        text = recognizer.recognize_google(audio)  # Convert speech to text
        print("You said:", text)
        return text  # Return the recognized text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio")
        return None
    except sr.RequestError:
        print("Could not request results, check your internet connection")
        return None

# Call the function
if __name__ == "__main__":
    speech_to_text()

#now understand this code step by step
#1.import speech recognition as sr
#2.initialize recognizer
#3.with sr.Microphone() as source: in this step we are reducing background noise and capture audio
#4.Using try and except
#5.using .recognize_google(audio) to recognize the voice