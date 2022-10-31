import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 81)
engine.say("M")
engine.runAndWait()
