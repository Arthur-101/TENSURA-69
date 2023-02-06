import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice',voice.id)
    engine.say("Hello World! Hello. World! Hello, World!")
    engine.runAndWait()
    print(voice.name)
engine.stop()
