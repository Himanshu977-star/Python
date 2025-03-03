import pyttsx3
import os

def text_to_speech(text):
  #Initialize the engine
  engine=pyttsx3.init()

  # Set properties
  engine.setProperty('rate', 140)  # Slow speed
  engine.setProperty('volume', 1.0)  # Full volume

  # Change voice
  voices = engine.getProperty('voices')
  engine.setProperty('voice', voices[0].id)  # Female voice:1 and Male Voice:0

  #Text to speech
  engine.say(text) #Adds text to the queue for speaking
  engine.runAndWait() #Processes the queue and speaks the text

  # Save as a file
  engine.save_to_file(text,"text to speech\\output.mp3")
  engine.runAndWait()

if __name__=="__main__":
  text=input("Enter what you want:")
  text_to_speech(text)

#now understand this code step by step
#1.Import module pyttsx3
#2.initialize the engine
#3.Use setPropert() to change rate and volume of voice
#4.change the voice into male or female by initialize voices using getProperty
#5.take text as input from user, use say() function and runAndWait() function
#6.use save_to_file(,"") function to save the voice
