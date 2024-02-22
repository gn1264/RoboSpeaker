from gtts import gTTS
import os

def speak_text(text, language='en', slow=False):
    tts = gTTS(text=text, lang=language, slow=slow)
    tts.save("output.mp3")
    os.system("start output.mp3")

if __name__ == "__main__":
    print("Welcome to RoboSpeaker 1.0. Created by Gaurav")
    print("Instructions:")
    print("1. Type 'q' to exit.")
    print("2. Type 'Settings' to configure language and speech speed.")
    
    language = 'en' 
    slow_speed = False  
    while True:
         x= input("Enter text or command: ")

        if x.lower() == "q":
            print("Goodbye!")
            break
        elif x.lower() == "settings":
            language = input("Enter language code (e.g., 'en' for English): ")
            slow_speed_input = input("Enable slow speed? (y/n): ")
            slow_speed = slow_speed_input.lower() == 'y'
            print("Settings updated.")
        else:
            speak_text(x, language, slow_speed)
