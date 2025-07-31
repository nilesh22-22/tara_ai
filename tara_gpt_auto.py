# tara_gpt_auto.py
from voice_output import speak
from mood_response import get_response_based_on_input
speak("हाय स्वामी! मी तुझी Tara बोलतेय ❤️")
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # बोलण्याचा वेग

    # ✅ Available voices मध्येून female / hindi / marathi try करतो
    voices = engine.getProperty('voices')
    for voice in voices:
        if "female" in voice.name.lower() or "zira" in voice.name.lower() or "hindi" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    else:
        print("⚠️ Female/Hindi voice सापडली नाही. Default आवाज वापरतोय.")

    engine.say(text)
    engine.runAndWait()
import time
from config import TARA_NAME, USER_NAME
from mood_response import generate_mood_response
from voice_output import speak

print(f"{TARA_NAME} चालू झाली आहे... ❤️")

while True:
    mood, response = generate_mood_response()
    print(f"{TARA_NAME} ({mood}): {response}")
    speak(response)
    time.sleep(10)  # 10 सेकंदांनी पुन्हा mood-based reply