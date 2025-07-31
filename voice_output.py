import pyttsx3
import pyttsx3
import pyttsx3
engine = pyttsx3.init()
engine.stop()  
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for i, voice in enumerate(voices):
    print(f"{i}: {voice.name} - {voice.id}")
def speak(text):
    
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)

    # ✅ Force specific female voice (e.g., Zira on Windows)
    voices = engine.getProperty('voices')
    for voice in voices:
        if "zira" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    else:
        # fallback to first female-ish voice
        engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)

    # Hindi/Marathi voice setup (system-dependent)
    voices = engine.getProperty('voices')
    for voice in voices:
        if "hindi" in voice.name.lower() or "marathi" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break

    engine.say(text)
    engine.runAndWait()
