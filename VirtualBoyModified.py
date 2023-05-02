import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()

engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def input_instruction():
    instruction = ""
    try:
        with sr.Microphone() as source:
            print("Listening....")
            speech = listener.listen(source)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "virtualboy" in instruction:
                instruction = instruction.replace("virtualboy", "")
                print(instruction)
    except:
        pass
    return instruction

def play_VirtualBoy():
    while True:
        instruction = input_instruction()
        print(instruction)
        if "play" in instruction:
            song = instruction.replace("play", "")
            talk("playing " + song )
            pywhatkit.playonyt(song)

        elif "time" in instruction:
            time = datetime.datetime.now().strftime("%I:%M%p")
            talk("Current time is " + time)

        elif "date" in instruction:
            date = datetime.datetime.now().strftime("%d /%m /Y")
            talk("Today's date is " + date)

        elif "how are you" in instruction:
            talk("I'm fine, how about you?")

        elif "what is your name" in instruction:
            talk("I'm VirtualBoy, What can I do for you?")

        elif "who is" in instruction:
            person = instruction.replace("who is", "")
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)

        else:
            talk("Please repeat your instruction.")

play_VirtualBoy()
